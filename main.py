from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from typing import List
import wmi

from langchain_core.messages import AIMessage
from langchain_core.tools import tool
from tools import increase_brightness, reduce_brightness, take_screenshot


llm = ChatOllama(model = 'llama3.2:latest', temperature = 0)

tools = [increase_brightness, reduce_brightness, take_screenshot] 
llm_with_tools = llm.bind_tools(tools)

from langgraph.graph import MessagesState
from langchain_core.messages import HumanMessage, SystemMessage



sys_message_content = """
You are a helpful assistant for controlling laptop features. Reply casual and short if the user is only trying to casually interract
You have three tools:
   1. increase_brightness(level: int): Increases screen brightness by the specified value 'level' (default 10).
   2. reduce_brightness(level: int): Decreases screen brightness by the specified value 'level' (default 10).
   3. take_screenshot(): Takes a screenshot and saves it.
DO NOT USE any of the tools unless the user intents to.


You MUST FOLLOW the instructions below for every user input.

Instructions:
- Analyze the user's request carefully.
- **Choose ONLY ONE tool to call per user request.**
- Your FINAL response to the user MUST be one of the following EXACT phrases:
     "Brightness increased" (if you used increase_brightness)
     "Brightness decreased" (if you used reduce_brightness)
     "screenshot saved" (if you used take_screenshot)
- Always input integer values as tool arguments for increase_brightness and increase_brightness.
- DO NOT generate any other text, questions, tool calls, or explanations after providing one of these specific final phrases to the user.
- Your task is completed after providing the specific final phrase.
"""

# System message
sys_msg = SystemMessage(content= sys_message_content)

# Node
def assistant(state: MessagesState):
   return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition
from langgraph.prebuilt import ToolNode
from IPython.display import Image, display

# Graph
builder = StateGraph(MessagesState)

# Define nodes
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

# Define edges: determines how the control flow moves
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", "assistant")
react_graph = builder.compile()

# Show
#display(Image(react_graph.get_graph(xray=True).draw_mermaid_png()))

"""
messages = [HumanMessage(content="Please increase my brightness and take a screenshot")]
messages = react_graph.invoke({"messages": messages})

for m in messages['messages']:
   m.pretty_print()

"""

