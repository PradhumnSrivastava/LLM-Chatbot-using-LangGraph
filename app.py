from graph.graph_builder import workflow

result = workflow.invoke({
    "message": "Hello My Name is Pradhumn Srivastava",
    "thread_id": "thread_1",
    "history": []
})

print(result)