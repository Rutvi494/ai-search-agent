import agno
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

agent = Agent(name="basic_agent",
              model= Groq(id="llama-3.3-70b-versatile",
                          api_key=os.getenv("GROQ_API_KEY")),
              description="You are news reporter who reports using a simple language in 3 lines along with date",
              markdown=True
              )

agent.print_response("Tell me the latest political news from USA along with a web url of news")