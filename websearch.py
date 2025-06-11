from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool

def wikisearch(query:str)->str:
    api_wrapper = WikipediaAPIWrapper()
    wiki = WikipediaQueryRun(api_wrapper=api_wrapper)
    return wiki.run(query)

WikiTool = Tool(
    name= "Wikisearch",
    func= wikisearch,
    description="Use this tool to find information online"
)