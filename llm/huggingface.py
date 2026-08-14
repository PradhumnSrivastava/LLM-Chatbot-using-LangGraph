from langchain.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

import os


load_dotenv()


class HuggingFaceLLM:

    def __init__(
        self,
        model_name="Qwen/Qwen2.5-7B-Instruct",
        api_key=None,
    ):
        self.model_name = model_name

        self.client = InferenceClient(
            api_key=api_key or os.getenv("HF_TOKEN")
        )

    def invoke(self, messages: list) -> str:

        formatted_messages = []

        for message in messages:

            if isinstance(message, HumanMessage):
                formatted_messages.append({
                    "role": "user",
                    "content": message.content
                })

            elif isinstance(message, AIMessage):
                formatted_messages.append({
                    "role": "assistant",
                    "content": message.content
                })

            elif isinstance(message, SystemMessage):
                formatted_messages.append({
                    "role": "system",
                    "content": message.content
                })

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=formatted_messages
        )

        return response.choices[0].message.content


llm = HuggingFaceLLM()