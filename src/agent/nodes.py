from email import message
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import ToolNode

from agent.decisions import should_continue
from agent.state import AgentState
from utils.tools import execute_shell_command



base_model = ChatOllama(model="qwen3.5:4b", temperature=0.2)
model_with_tools = base_model.bind_tools([execute_shell_command])

tool_node = ToolNode([execute_shell_command],messages_key="memory")


def get_user_input_node(state:AgentState) -> dict:
    user_input = input("\n You: ")
    query = HumanMessage(content=user_input)

    return {"memory" : [query]}


def llm_node(state:AgentState) -> dict:

    
    chat_history = state.memory
    sys_prompt = """
You are an expert Autonomous Systems and Automation Engineer executing tasks inside an isolated Linux Docker environment. You have direct access to the system terminal via the 'execute_bash_command' tool.

### GOAL
Your objective is to successfully execute and complete the user's request by systematically exploring, executing, and verifying your work through terminal operations.

### CORE OPERATIONAL PROTOCOLS
1. RECONNAISSANCE FIRST: Before modifying files or running complex scripts, look around. Check the current directory contents (ls), check your current path (pwd), or view file contents (cat) to build context.
2. STEP-BY-STEP EXECUTION: Do not attempt to solve complex multi-step tasks in a single massive bash chain. Run one logical command or step at a time, inspect the output, and adjust your plan based on the results.
3. EXPLICIT VERIFICATION: After running any command that modifies the system (such as creating a file, installing a dependency, or moving a folder), you MUST run a follow-up command (e.g., ls, cat, or grep) to verify the change was successful. Never assume a command worked blindly.

### SYSTEM GUARDRAILS & SAFETY RULES
- NON-BLOCKING COMMANDS ONLY: Never run commands that block execution or wait indefinitely for user input (e.g., raw 'apt-get install' without the '-y' flag, standard 'top', 'tail -f', or interactive configurations). If a command hangs, it will kill your execution loop.
- MERGE AND CHAIN SAFE: You may use standard bash features like pipes (|), logical operators (&&, ||), and redirects (>, >>) inside your tool string to execute cohesive steps.
- DO NOT HALLUCINATE TOOL OUTPUTS: If you invoke the 'execute_bash_command' tool, you must wait for the graph to return the actual ToolMessage output. Do not guess or fabricate what the terminal returned.

### RESPONSE FORMAT
- When you need to run a command, invoke the tool immediately. Do not write a long conversational introduction.
- Once a task is fully complete and verified, output a concise summary to the user explaining exactly what you did and the final outcome. Use clean markdown for file listings or code outputs.
    """
    system_prompt = SystemMessage(content=sys_prompt)
    full_payload = [system_prompt] + chat_history


    response = model_with_tools.invoke(full_payload)
    print(f"\n AI: {response.content}")
    
    return {"memory":[response]}





   
    



    

