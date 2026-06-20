from agent.state import AgentState
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode

from agent.nodes import call_model
from agent.decisions import should_continue
from utils import llm

agent = StateGraph(AgentState)

agent.add_node("llm",call_model)
agent.add_edge(START,"llm")
agent.add_conditional_edges(source="llm", path=should_continue,path_map={
    "continue":"llm",
    "exit": END
})


a = agent.compile()