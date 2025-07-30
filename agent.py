# LangChain agent definition
from langchain.agents import initialize_agent, Tool
# from langchain.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import PandasTool
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
def get_agent(df):
    pandas_tool = PandasTool(df)

    tools = [
        Tool(
            name="PythonPandasTool",
            func=pandas_tool.run_code,
            description="""
                Use this tool to run Python pandas code on a DataFrame named `df`.
                Always store output in variable 'result' if you want it returned.
            """
        )
    ]

    # llm = ChatOpenAI(temperature=0, model_name="gpt-4")  # Or "gpt-3.5-turbo"
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",google_api_key=api_key)
    # llm = ChatGoogleGenerativeAI(model="")
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
    return agent
