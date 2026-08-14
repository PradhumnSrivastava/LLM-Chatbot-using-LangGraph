from graph.state import State
from llm.huggingface import llm
from langchain.messages import HumanMessage, AIMessage, SystemMessage

def generate_response(state: State) -> State:

    temp_history = []

    for turn in state.get("history", []):
        temp_history.append(turn["HumanMessage"])
        temp_history.append(turn["AIMessage"])

    temp_history.append(
        HumanMessage(content=state["message"])
    )

    response = llm.invoke(temp_history)

    return {
        "response": response
    }


def update_history(state: State) -> State:
    """
    Update conversation history with the current
    HumanMessage and AIMessage.
    """

    new_history = {
        "HumanMessage": HumanMessage(
            content=state["message"]
        ),
        "AIMessage": AIMessage(
            content=state["response"]
        )
    }

    return {
        "history": [new_history]
    }