from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv

import asyncio

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

async def main():
  agent = Agent(
    task="Compare the price of gpt-4o and Gemini 2.5 pro and give me the results in dollars",
    llm=llm,
  )
  result = await agent.run()
  # print(result)
  print(result.final_result)

asyncio.run(main())
