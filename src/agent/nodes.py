from email import message
from langchain_ollama import ChatOllama

from .state import AgentState
from ..utils.llm import response

model = ChatOllama(model="qwen3.5:4b",temperature=0.2)

def initial(state:AgentState) -> list[dict]:
    
    
    sys_prompt = {"role": "System",
                  "content":"You are a simple agent do as you are told"
                }
    user_prompt = {"role": "User",
                  "content": query
                }
    return [sys_prompt,user_prompt]

def call_model(state:AgentState) -> dict:
    
    response = model.invoke(state.messages)

    print(f"LLM: {response}")
    return {"messages": [response]}



    

