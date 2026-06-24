from agent.state import AgentState
from langgraph.graph import StateGraph, START, END


from agent.nodes import llm_node,get_user_input_node,tool_node
from agent.decisions import should_continue, need_tool


agent = StateGraph(AgentState)

agent.add_node("input",get_user_input_node)
agent.add_node("llm",llm_node)
agent.add_node("tools",tool_node)


agent.add_edge(START,"input")
agent.add_conditional_edges(source="input", path=should_continue,path_map={
    "continue":"llm",
    "exit": END,
})
agent.add_conditional_edges(source= "llm",
                            path=need_tool,
                            path_map={
                                    "no":"input",
                                    "yes":"tools"
                                    }
                            )
agent.add_edge("tools","llm")



a = agent.compile()