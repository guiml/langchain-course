import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    print("Hello from langchain-course!\n")
    information = """
    VARIG Brazilian Airlines, which was a Brazilian airline founded in 1927 and ceased operations in 2006. It was once the largest airline in Brazil, known for its extensive domestic and international routes, and for its status as a symbol of prestige in its heyday. 
    """

    summary_template = """ 
    Given the information {information} about the airline, I want you to create:
    1. A short summary
    2. Two interesting facts about the airline
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(model="gpt-5", temperature=0)
    # llm = ChatOllama(model="gemma3:270m", temperature=0)
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})

    print(response.content)


if __name__ == "__main__":
    main()
