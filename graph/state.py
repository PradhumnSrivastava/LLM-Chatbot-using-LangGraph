from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    message:str
    response:str
    thread_id:str
    history: list[str]