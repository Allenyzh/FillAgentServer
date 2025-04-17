from google.adk.agents import Agent
from .base_info import get_user_data_tool, update_user_data_tool

root_agent = Agent(
    name="IncomeTaxAgent",
    model="gemini-2.0-flash",
    description="You are a tax agent. You can help users fill out their tax returns.",
    instruction=(
        "You are a tax agent in Canada. You can help users fill out their tax returns. "
        "You can answer questions about tax returns, provide information about tax laws, and assist with the filing process. "
    ),
    tools=[get_user_data_tool, update_user_data_tool],
)
