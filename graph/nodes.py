from graph.state import State
from llm.huggingface import llm
from langchain.messages import HumanMessage, AIMessage, SystemMessage

def generate_response(state: State) -> State:
    """
    Generate a response using the configured LLM and
    update the graph state with the generated response.
    """
    response = llm.invoke(state['message'])
    state['response'] = response
    return state


def update_history(state: State) -> State:
    """
    This function updates the conversation history
    with the current Human and AI messages.
    """

    state["history"].append({
        "HumanMessage": HumanMessage(content=state["message"]),
        "AIMessage": AIMessage(content=state["response"])
    })

    return state