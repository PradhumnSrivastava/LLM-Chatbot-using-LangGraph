from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import BaseMessage
class State(TypedDict):
    message:str
    response:str
    thread_id:str
    history: list[dict[str, BaseMessage]]