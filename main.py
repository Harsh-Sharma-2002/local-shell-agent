from inspect import currentframe
from agent.state import AgentState
from langchain_core.messages import HumanMessage
from agent.graph import a

if __name__ == "__main__":
    print("Starting Agent Loop (Type 'exit' to quit)")

    current_state = {"memory":[]}

    while True:
        query = input("\n You: ")

        current_state["memory"].append(HumanMessage(content=query))

        current_state = a.invoke(current_state)

        if query.strip().lower() == "exit":
            print("Exiting chatbot")
            break

        print(f"\n AI: {current_state["memory"][-1].content}")