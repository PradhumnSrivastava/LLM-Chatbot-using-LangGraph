from graph.graph_builder import workflow


config = {
    "configurable": {
        "thread_id": "thread_1"
    }
}


result1 = workflow.invoke(
    {
        "message": "My name is Pradhumn Srivastava.",
        "history": []
    },
    config=config
)

print("First:", result1)


result2 = workflow.invoke(
    {
        "message": "What is my name?"
    },
    config=config
)

print("Second:", result2)