from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import BaseMessage
import operator
class State(TypedDict):
    message:str
    response:str
    thread_id:str
    history: Annotated[list[dict[str, BaseMessage]],operator.add]