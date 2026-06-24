# src/utils/mcp_client.py
import sys
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_core.tools import StructuredTool

server_params = StdioServerParameters(
    command=sys.executable,
    args=["src/utils/mcp_server.py"]
)

# Global persistent session state
_shared_session = None

async def get_mcp_tools_as_langchain():
    global _shared_session
    langchain_tools = []
    
    # 1. Initialize the background process ONCE and keep it alive globally
    if _shared_session is None:
        # Enter the stdio client transport layer context programmatically
        transport_ctx = stdio_client(server_params)
        read_stream, write_stream = await transport_ctx.__aenter__()
        
        # Initialize the JSON-RPC Client Session
        session_ctx = ClientSession(read_stream, write_stream)
        _shared_session = await session_ctx.__aenter__()
        await _shared_session.initialize()

    # 2. Query available tools from the live connection
    mcp_tools = await _shared_session.list_tools()
    
    for mcp_tool in mcp_tools.tools:
        def make_tool(t_name=mcp_tool.name, t_desc=mcp_tool.description):
            
            # The tool execution block now reuses the running background session
            async def dynamic_tool_async(command: str) -> str:
                response = await _shared_session.call_tool(t_name, arguments={"command": command})
                return response.content[0].text

            def dynamic_tool_sync(command: str) -> str:
                return asyncio.run(dynamic_tool_async(command))

            return StructuredTool.from_function(
                func=dynamic_tool_sync,
                coroutine=dynamic_tool_async,
                name=t_name,
                description=t_desc
            )
        
        langchain_tools.append(make_tool())
        
    return langchain_tools