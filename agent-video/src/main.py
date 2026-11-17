import ollama
import json
from pathlib import Path
from agent_tools import multiply, save_result, projectile_simulation, plot_trajectories
from agent_utils import load_history, save_history

MODEL = "qwen3:8b"
PATH_HISTORY = Path("histories/history.json")


TOOLS = {
    func.__name__: func for func in [multiply, save_result, projectile_simulation, plot_trajectories]
}


def main():

    messages = load_history()

    while True:

        user_input = input("user:\n")

        if user_input == "/bye":
            break

        if user_input == "/clear":
            messages = []
            save_history(messages)

            print("clear contenxt ... \n")
            continue

        messages.append({"role":"user", "content": user_input})

        for i in range(5): 
            response = ollama.chat(
                model=MODEL,
                messages=messages,
                think=False,
                tools=list(TOOLS.values()),
                options={"temperature": 0}
            )

            messages.append(response.message.model_dump(exclude_none=True))

            if not response.message.tool_calls:
                break
                
            for tool in response.message.tool_calls or []:
                name = tool.function.name
                arguments = tool.function.arguments

                print("name: ", name)
                print("arguments: ", arguments)

                try:
                    result = TOOLS[name](**arguments)
                except Exception as e:
                    result = {"error": f"{type(e).__name__}: {e}"}

                print("result: ", result)

                messages.append(
                    {"role": "tool", "tool_name": name, "content": json.dumps(result)}
                )

        print(f"\nassistant:\n{response.message.content}\n")
        save_history(messages)

if __name__== "__main__":
    main()