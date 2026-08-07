from langchain_huggingface import HuggingFaceEndpoint

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

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

    def invoke(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content
    
llm = HuggingFaceLLM()