from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI 


def search(query: str) -> str:
    """A simple search tool that simulates searching for a query.
    
    Args:
        query (str): The search query.  
        Returns:
            str: The search results.
    """
    print(f"Searching for: {query}")
    return "Found some results!"

llm = ChatOpenAI()
tools = [search]
agent = create_agent(model=llm,tools=tools)

def main():
    print("Hellow from langchain-course lesson 2!\n")
    result = agent.invoke({"messages":HumanMessage(content="What is the weather in New York?")})
    print(result)

if __name__ == "__main__":
    main()