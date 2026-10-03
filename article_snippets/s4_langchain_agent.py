import os

from langchain.agents import create_agent
from langchain_scrapingbee import ScrapeUrlTool

scrape = ScrapeUrlTool(api_key=os.environ["SCRAPINGBEE_API_KEY"])
agent = create_agent(
    "anthropic:claude-haiku-4-5",
    tools=[scrape],
    system_prompt=(
        "Use scrape_url with return_content=true and params "
        '{"render_js": true, "return_page_markdown": true} to read pages before answering.'
    ),
)
result = agent.invoke({"messages": [{
    "role": "user",
    "content": "Read https://docsify.js.org/#/quickstart. Which command previews a Docsify site locally, and on which port?",
}]})
print(result["messages"][-1].content)
