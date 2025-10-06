# AI Agent

A minimal, extensible agent framework that enables a language model to invoke Python tools and perform real actions — bridging natural language reasoning with execution.

## Overview

ai_agent is a Python-based agent architecture that integrates a language model with a curated set of tools. Rather than embedding all logic in code, the LLM reasons about which tool to call (e.g. file I/O, code execution, calculator), and the framework executes those calls reliably, returning structured outputs. The design emphasizes clarity, extensibility, and correctness in orchestrating function calls.

## Key Features

Function-calling orchestration
- The agent sends prompts to the LLM with descriptions of available tools (schemas). The model may respond with structured function calls rather than freeform text. The framework captures those calls, executes them, and returns results back into the loop.
- Tool abstractions
  - Core tools include:

    - File listing (get_files_info)
    
    - File reading (get_file_content)
    
    - Python execution (run_python_file)
    
    - File writing (write_file)
    
    - Arithmetic evaluation (the calculator module)

- Looping until resolution
- The agent continues requesting tool invocations until the model signals it is done, at which point it issues a final natural language response.
- Test suite & validation
- The repository includes end-to-end tests (tests.py) that check both correct tool invocation sequences and final outputs given specific prompts.
- Verbose and debug support
- Optional verbose logging allows inspection of token usage, chosen function calls, arguments, and internal message state during development.


## Execution Flow

### Prompt → LLM
A system prompt describes the available tools and their schemas. The user’s query is sent along.

### LLM decides
The model may return a function call with an explicit tool and arguments, rather than plain text.

### Tool execution
The framework receives function calls, runs the corresponding Python function locally, and wraps the result in a structured response.

### Loop or conclude
The response is fed back to the model. The loop continues until the model returns no more function calls — at which point it outputs a final answer.

### Final output
The agent prints or returns the final result in natural language.

## RUN & PREREQUISITIES

1. via terminal python3 -m main " User query " 
2. .env file containing GEMINI_API_KEY and git_token
