# mini-agent, A local Engineering Agent from Python and Ollama

Code for Part 1 and 2 of the Younes Lab series on building a small engineering agent from scratch. This part runs a language model locally with Ollama and talks to it from Python.

🎥 Video Part 1: [link](https://youtu.be/nn2BSO19iOk)
🎥 Video Part 2: [link](https://youtu.be/D-xk3d0v7bk)

## What you'll learn

How a local model is served by Ollama and queried over HTTP, why chat models are stateless, how the `system`, `user` and `assistant` roles shape a conversation, and why the message list you resend on every call is the model's only memory.

## Requirements

Python 3.10+, [Ollama](https://ollama.com) installed and running, and a model pulled locally. The examples use Qwen3 8B.

```bash
ollama pull qwen3:8b
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python src/main.py
```

If the model name differs on your machine, check `ollama list` and update `MODEL` at the top of `src/main.py`.

## Notes

`qwen3:8b` supports switching reasoning off with `think=False`. Thinking-only variants such as the current `qwen3:4b` tag ignore it, and their reasoning ends up in the answer text, so use `qwen3:8b` or an `-instruct` variant.
