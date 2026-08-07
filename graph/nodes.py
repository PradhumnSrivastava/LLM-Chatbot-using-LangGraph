from graph.state import State
from llm.huggingface import llm



def generate_response(state: State) -> State:
    response = llm.invoke(state['message'])
    return tate

