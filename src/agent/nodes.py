from email import message
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import ToolNode

from agent.decisions import should_continue
from agent.state import AgentState
from utils.tools import execute_shell_command



model = ChatOllama(model="qwen3.5:4b",temperature=0.2).bind_tools([execute_shell_command])
tool_node = ToolNode([execute_shell_command])


def get_user_input_node(state:AgentState) -> dict:
    user_input = input("\n You: ")
    query = HumanMessage(content=user_input)

    return {"memory" : query}


def llm_node(state:AgentState) -> dict:

    print("Thinking")
    chat_history = state.memory

    system_prompt = SystemMessage(content="You are a simple agent and in given sentence you have to extract the information of the person and return a json file for all info you can find")
    full_payload = [system_prompt] + chat_history

    print("payload ready")
    response = model.invoke(full_payload)
    print(f"\n AI: {response.content}")
    
    return {"memory":[response]}





   
    



    

