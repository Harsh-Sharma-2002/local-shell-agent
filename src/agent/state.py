from pickletools import int4
from pydantic import BaseModel
from typing import Annotated, Sequence
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage,BaseMessage



class AgentState(BaseModel):
    memory: Annotated[Sequence[HumanMessage],add_messages]

    

  


