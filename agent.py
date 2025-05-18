from langchain.agents import initialize_agent, AgentType
from llm import llm
from tools import tools

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def run_agent():
    while True:
        query = input("Ask: ")
        if query.lower() in ['exit', 'quit']:
            break
        result = agent.run(query)
        print("Answer:", result)

if __name__ == "__main__":
    run_agent()
