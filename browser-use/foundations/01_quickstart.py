from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv

import asyncio

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

async def main():
  agent = Agent(
    task="Give the latest stock price of NVIDIA",
    llm=llm
  )
  result = await agent.run()

asyncio.run(main())
