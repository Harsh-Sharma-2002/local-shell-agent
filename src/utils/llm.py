import ollama
import json
#from .state import User

from pickletools import int4
from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name:str
    age: int

    @field_validator('age')
    @classmethod
    def validate_age(cls,value):
        if value <= 0:
            raise ValueError(f"age must be postive: {value}")
        return value


def call_local_llm(prompt: str, model_name: str = "qwen3.5:4b") -> str:
    try:
        # Querying your local Ollama instance running on localhost:11434
        response = ollama.chat(
            model=model_name,
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                }
            ],
            think = False,
            response_format=User,
            options={
                'temperature': 0.7,
                'num_predict': 1000, # Restricts output token length, similar to max_tokens
                
            }
        )
        return response['message']['content']
        
    except Exception as e:
        return f"Local inference error: {e}"

# Test it out
response = call_local_llm("I am Flashy and I am 34 years old")

print(response)
