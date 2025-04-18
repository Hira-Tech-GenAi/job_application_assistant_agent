# Import necessary modules
from langchain_google_genai import GoogleGenerativeAI  # type: ignore #? For integrating Google's Generative AI
from langchain.agents import initialize_agent, AgentType, Tool #type: ignore #? For creating and managing agents
from langchain.memory import ConversationBufferMemory # type: ignore #? For maintaining conversation history
from dotenv import load_dotenv  # For loading environment variables from a .env file
import os  # For interacting with the operating system
import re  # For using regular expressions

# Load environment variables from .env file
load_dotenv()

# Initialize the language model with specified parameters
llm = GoogleGenerativeAI(
  model="gemini-2.0-flash",  # Specify the model to use
  google_api_key=os.environ["GEMINI_API_KEY"]  # Retrieve API key from environment variables
)

# Initialize memory to store conversation history
memory = ConversationBufferMemory(
  memory_key="chat_history",  # Key to identify the memory
  return_messages=True  # Return messages as part of the memory
)

# Dictionary to store user's application information
application_info: dict = {
  "name": None,  # User's name
  "email": None,  # User's email
  "skills": None,  # User's skills
}

# Function to extract application information from user's input
def extract_application_info(text: str) -> str: 
    # Use regular expressions to find name, email, and skills in the input text
    name_match = re.search(r"(?:my name is|i am)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)", text, re.IGNORECASE) 
    email_match = re.search(r"\b[\w.-]+@[\w.-]+\.\w+\b", text)  
    skills_match = re.search(r"(?:skills are|i know|i can use)\s+(.+)", text, re.IGNORECASE) 

    response = []  # List to store response messages

    if name_match: 
        application_info["name"] = name_match.group(1).title()  # Extract and format name
        response.append("✅ Name saved.")  # Add confirmation message

    if email_match:
        application_info["email"] = email_match.group(0)  # Extract email
        response.append("✅ Email saved.")  # Add confirmation message

    if skills_match:
        application_info["skills"] = skills_match.group(1).strip()  # Extract and clean skills
        response.append("✅ Skills saved.")  # Add confirmation message

    # If no information was extracted, prompt the user to provide it
    if not any([name_match, email_match, skills_match]):
        return "❓ I couldn't extract any info. Could you please provide your name, email, or skills?"

    # Return the combined response messages
    return " ".join(response) + " Let me check what else I need."

# Function to check if all application information has been collected
def check_application_goal(_: str) -> str:
    if all(application_info.values()):
        # If all information is present, confirm completion
        return f"✅ You're ready! Name: {application_info['name']}, Email: {application_info['email']}, Skills: {application_info['skills']}."
    else:
        # Identify missing information
        missing = [k for k, v in application_info.items() if not v]
        return f"⏳ Still need: {', '.join(missing)}. Please ask the user to provide this."

# Define tools that the agent can use
tools = [
    Tool(
        name="extract_application_info",  # Name of the tool
        func=extract_application_info,  # Function to execute
        description="Use this to extract name, email, and skills from the user's message."  # Description of the tool
    ),
    Tool(
        name="check_application_goal",  # Name of the tool
        func=check_application_goal,  # Function to execute
        description="Check if name, email, and skills are provided. If not, tell the user what is missing.",  # Description of the tool
        return_direct=True  # Return the result directly without further processing
    )
]

# System prompt to guide the agent's behavior
SYSTEM_PROMPT = """You are a helpful job application assistant. 
Your goal is to collect the user's name, email, and skills. 
Use the tools provided to extract this information and check whether all required data is collected.
Once everything is collected, inform the user that the application info is complete and stop.
"""

# Initialize the agent with specified parameters
agent = initialize_agent(
    tools=tools,  # Tools the agent can use
    llm=llm,  # Language model to use
    memory=memory,  # Memory to maintain conversation history
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,  # Type of agent
    verbose=True,  # Enable verbose output for debugging
    agent_kwargs={"system_message": SYSTEM_PROMPT}  # Additional arguments for the agent
)

# Greet the user and prompt for information
print("📝 Hi! I'm your job application assistant. Please tell me your name, email, and skills.")

# Start an interactive loop to process user input
while True:
    user_input = input("You: ")  # Get input from the user
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Bye! Good luck.")  # Farewell message
        break  # Exit the loop

    response = agent.invoke({"input": user_input})  # Process the input through the agent
    print("Bot:", response["output"])  # Display the agent's response

    # If all information has been collected, confirm completion and exit
    if "you're ready" in response["output"].lower():
        print("🎉 Application info complete!")
        break
    # If the user has provided all required information, exit the loop