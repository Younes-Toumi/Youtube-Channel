import ollama
import json
from pathlib import Path

MODEL = "qwen3:8b"


PATH_HISTORY = Path("histories/history.json")

def load_history():
    if PATH_HISTORY.exists():
        return json.loads(PATH_HISTORY.read_text())

    return []

def save_history(history):
    PATH_HISTORY.write_text(json.dumps(history, indent=4, ensure_ascii=False))  

def main():

    messages = load_history()

    while True:

        user_input = input("user:\n")

        if user_input == "/bye":
            break

        messages.append({"role":"user", "content": user_input})

        response = ollama.chat(
            model=MODEL,
            messages=messages,
            think=False
        )

        messages.append(response.message.model_dump(exclude_none=True))

        print(f"\nassistant:\n{response.message.content}\n")
        save_history(messages)

if __name__== "__main__":
    main()