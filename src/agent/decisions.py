from langchain_core.messages.tool import tool_call
from agent.state import AgentState

def should_continue(state:AgentState) -> str:
    chat_history = state.memory

    if chat_history[-1].content.strip().lower() == "exit":
        return "exit"
    
    return "continue"

def need_tool(state:AgentState) -> str:
    chat_history = state.memory
    if hasattr(chat_history[-1],"tool_calls") and chat_history[-1].tool_calls:
        return "yes"
    
    return "no"