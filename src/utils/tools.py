import subprocess as sp

def execute_shell_command(command:str) -> str:
    """
    Executes a raw bash command inside the terminal and returns the results.
    Use this to read directories (ls), read files (cat), write files (echo), or run scripts.
    
    Args:
        command (str): The exact bash command string to execute (e.g., 'ls -la' or 'cat main.py').
    """
    try:
        print(f"Tool running command: {command}")
        result = sp.run(command, 
                        shell=True, 
                        capture_output=True,
                        text=True, 
                        timeout=10
                        )

        output = result.stdout
        if result.stderr:
            output += f"\n[STDERR]: {result.stderr}"

        if not output.strip():
            return "[Success: Command executed with no output text returned]"

        print(f"Terminal output: {output}")
        return  output

    except sp.TimeoutExpired:
        return "[ERROR]: Command execution timed out after 10 seconds. Do not run blocking commands."
    except Exception as e:
        return f"[ERROR]: System failed to execute command: {str(e)}"