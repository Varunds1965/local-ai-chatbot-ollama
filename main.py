from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()
@tool
def calculator(a: float, b: float) -> str:
    """Useful for basic arithmetic calculations on numbers"""
    print("The tool has been called.")
    return f"sum of {a} and {b} is {a + b}"
def main():
    model = ChatOllama(model="qwen3:latest",temperature=0)
    tools = [calculator]
    agent_executor = create_react_agent(model, tools) 

    print("Welcome to the ReAct Agent! Type 'exit' to quit.")
    print("You can ask me anything, and I'll try to help you with my reasoning abilities.")

    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input == "exit":
            print("Goodbye!")
            break
        
        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()  # Print a newline after the response is complete

if __name__ == "__main__":
    main()

