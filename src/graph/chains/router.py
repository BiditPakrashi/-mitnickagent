from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import AzureChatOpenAI
import os


class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""

    datasource: Literal["vectorstore", "websearch"] = Field(
        ...,
        description="Given a user question choose to route it to web search or a vectorstore.",
    )


llm = AzureChatOpenAI(
    azure_endpoint=os.environ['OPENAI_API_BASE'],
    azure_deployment=os.environ['OPENAI_API_IMAGE'],
    api_version=os.environ['OPENAI_API_VERSION'],
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)
structured_llm_router = llm.with_structured_output(RouteQuery)

system = """You are an expert at routing a user question to a vectorstore or web search.
The vectorstore contains documents related to Cyber security , code scan , Jira , cloud Inferstructure."""
route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

question_router = route_prompt | structured_llm_router