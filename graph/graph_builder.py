from langgraph.graph import StateGraph, START, END
from graph.nodes import generate_response
from graph.nodes import update_history
from graph.state import State


#Define the state graph using the State TypedDict
graph = StateGraph(State)

graph.add_node("generate_response", generate_response)
graph.add_node("update_history", update_history)
graph.add_edge(START, "generate_response")
graph.add_edge("generate_response", "update_history")
graph.add_edge("update_history", END)

workflow = graph.compile()