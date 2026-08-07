from langgraph.graph import StateGraph, START, END
from graph.nodes import generate_response
from graph.state import State


#Define the state graph using the State TypedDict
graph = StateGraph(State)

graph.add_node("generate_response", generate_response)
graph.add_edge(START, "generate_response")
graph.add_edge("generate_response", END)

workflow = graph.compile()