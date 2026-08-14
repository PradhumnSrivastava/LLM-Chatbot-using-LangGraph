from graph.state import State
from llm.huggingface import llm

def generate_response(state: State) -> State:
    """
    Generate a response using the configured LLM and
    update the graph state with the generated response.
    """
    response = llm.invoke(state['message'])
    state['response'] = response
    return state

