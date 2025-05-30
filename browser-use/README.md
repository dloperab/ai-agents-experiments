# Browser Use

This module provides tools and examples for browser automation and web interaction using AI Agents. It allows you to create agents that can navigate websites, extract information, and perform various web-based tasks.

## Structure

- `foundations/`: Contains basic examples and quickstart guides
  - `01_quickstart.py`: A minimal example showing how to create and run a browser agent to fetch stock prices
  - `02_agent_settings.py`: Demonstrates various agent configurations including conversation saving, system message customization, history tracking, initial actions, and planner integration

## Features

- Browser automation with AI agents.
- Web scraping and data extraction.
- Price comparison capabilities.
- Asynchronous operation support.

## Quick Start

1. Set up your environment variables in a `.env` file:
Create a `.env` file based on `.env.example`:
```
OPENAI_API_KEY=
```

2. Run the experiments:

    **01 - Quickstart**
    ```bash
    uv run python foundations/01_quickstart.py
    ```

    **02 - Agent Settings**
    ```bash
    uv python run foundations/02_agent_settings.py
    ```

## Resources

- [Browser Use](https://browser-use.com/)
- [Browser Use Docs](https://docs.browser-use.com/introduction)
- [Patchright library](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright)

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.
