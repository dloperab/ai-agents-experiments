from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser
from dotenv import load_dotenv

import asyncio

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

async def run_agent_with_save_conversation():
  agent = Agent(
    task="Search and return the latest stock price of NVIDIA",
    llm=llm,
    save_conversation_path="./browser-use/logs/conversations"
  )
  await agent.run()

async def run_agent_with_extend_system_message():
  agent = Agent(
    task="Search and return the latest stock price of NVIDIA",
    llm=llm,
    extend_system_message="You are a financial analyst that always use yahoo finance to get the latest stock price",
  )
  await agent.run()

async def run_agent_showing_history_conversation():
  agent = Agent(
    task="Search and return the latest stock price of NVIDIA",
    llm=llm,
  )
  result = await agent.run()

  print(f"[INFO] URLs: {result.urls()}")
  print(f"[INFO] Model actions: {result.model_actions()}")
  print(f"[INFO] Model thoughts: {result.model_thoughts()}")
  print(f"[INFO] Final result: {result.final_result()}")

async def run_agent_with_initial_actions():
  initial_actions = [
     {"open_tab": {'url': 'https://finance.yahoo.com/quote/NVDA'}},
     {"scroll_down":  {'amount': 100}},
  ]

  agent = Agent(
    task="Search and return the latest stock price of NVIDIA",
    llm=llm,
    initial_actions=initial_actions
  )
  await agent.run()

async def run_agent_with_planner():
  planner_llm = ChatOpenAI(model="o3-mini")

  initial_actions = [
     {"open_tab": {'url': 'https://finance.yahoo.com/quote/NVDA'}}
  ]

  agent = Agent(
    task="Search for the latest stock price of NVIDIA and analyze the data based on the latest 2 days",
    llm=llm,
    initial_actions=initial_actions,
    planner_llm=planner_llm,
    use_vision_for_planner=False,
    planner_interval=2
  )
  result = await agent.run(max_steps=10)
  
  print(f"[INFO] Thoughts: {result.model_thoughts()}")
  print(f"[INFO] Final result: {result.final_result()}")


async def main():
    # Display available agent options
    print("\nAvailable Agent Types:")
    print("1. Agent with save conversation")
    print("2. Agent with extend system message")
    print("3. Agent showing history")
    print("4. Agent with initial actions")
    print("5. Agent with planner")
    
    # Get user choice
    choice = input("\nSelect an agent type (1-5): ")
    
    # Create and run the selected agent
    if choice == "1":
        await run_agent_with_save_conversation()
    elif choice == "2":
        await run_agent_with_extend_system_message()
    elif choice == "3":
        await run_agent_showing_history_conversation()
    elif choice == "4":
        await run_agent_with_initial_actions()
    elif choice == "5":
        await run_agent_with_planner()
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or 5.")
        return

if __name__ == "__main__":
    asyncio.run(main())
