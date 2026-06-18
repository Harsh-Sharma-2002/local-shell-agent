import ollama
from src.agent.state import User



def call_local_llm(prompt: str, model_name: str = "qwen3.5:4b") -> str:
    try:
        response = ollama.chat(
            model=model_name,
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                }
            ],
            think = False,
            format=User.model_json_schema(),
            options={
                'temperature': 0.7,
                'num_predict': 1000, 
                
            }
        )
        return response['message']['content']
        
    except Exception as e:
        return f"Local inference error: {e}"


# temp = """

# You are a strict data extraction engine. Your job is to extract user information and format it exactly according to this JSON schema:

# {
#   "name": "string",
#   "age": "integer"
# }

# CRITICAL RULES:
# 1. Do not include any conversational text, introductory remarks, or explanations.
# 2. Do not wrap the JSON inside markdown code blocks (no ```json).
# 3. Output ONLY the raw JSON string.

# Example Input: "My name is John and I turned 25 last month."
# Example Output: {"name": "John", "age": 25}

# User Input: I am Flashy and I am 34 years old
# """

# response = call_local_llm(temp)

# print(response)




