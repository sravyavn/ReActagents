from langchain_core.tools import Tool
from langchain.prompts import PromptTemplate
from langchain-ChatGroq import ChatGroq

def calculator(query):
    prompt="""
    you are a math assistant. perform operations and only return final answer.
    """
    Prompt = PromptTemplate(input_variables=["Question"],template=prompt)
    
    llm= ChatGroq(model="llama-3.1-8b-instant",temperature=1)
    
    chain= Prompt | llm
    result= chain.invoke({"Question":query})
    
calculator_Tool = Tool(
    name="Calculator",
    func=calculator,
    description="use this tool for mathematical calculations"
)