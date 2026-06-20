from agent.state import AgentState

def should_continue(state:AgentState) -> str:
    chat_history = state.memory

    if chat_history[-1].content.strip().lower() == "exit":
        return "exit"
    
    return "continue"