from pickletools import int4
from pydantic import BaseModel
from typing import Annotated, Sequence, TypedDict
from langgraph.graph.message import add_messages

class message(TypedDict):
    role: str
    content: str

class AgentState(BaseModel):
    messages: Annotated[Sequence[message],add_messages]

    

  


