from email import message
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage

from agent.state import AgentState



model = ChatOllama(model="qwen3.5:4b",temperature=0.2)


def call_model(state:AgentState) -> dict:
    
    chat_history = state.memory

    system_prompt = SystemMessage(content="You are a simple agent and in given sentence you have to extract the information of the person and return a json file for all info you can find")
    full_payload = [system_prompt] + chat_history

    response = model.invoke(full_payload)

    return {"message" : [response]}

   
    



    

