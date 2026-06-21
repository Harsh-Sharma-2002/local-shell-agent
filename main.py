from inspect import currentframe
from agent.state import AgentState
from langchain_core.messages import HumanMessage
from agent.graph import a

if __name__ == "__main__":
    print("Starting Agent Loop (Type 'exit' to quit)")

    current_state = {"memory":[]} 
    current_state = a.invoke(current_state)

    print("ending agent loop")