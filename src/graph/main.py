from dotenv import load_dotenv, find_dotenv
from graph import app
from langchain_core.messages import BaseMessage, HumanMessage
load_dotenv(find_dotenv())

if __name__ == "__main__":
    print("--------- Agentic Framework ----------------")
    result = (app.invoke(input={"question": "Implement code scanner Snyk and uninstall  Checkmarx"}))
    print(result['generation'])