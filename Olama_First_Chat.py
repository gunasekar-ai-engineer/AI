from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as slt

custom_css = '''
    <style>
        div.css-1om1ktf.e1y61itm0 {
          width: 800px;
        }
        textarea.st-cl {
          height: 400px;
        }
    </style>
    '''

slt.title("Jarvis - Chat Bot")
input_txt = slt.text_area("Please ask your questions to me", key="user_input", height=40)
prompt = ChatPromptTemplate.from_messages(
    [("system", "You're an AI assistant. Your name is Jarvis. You need to guide the user on his needs."),
     ("user", "user questions:{questions}")
     ])
llm = Ollama(model="llama3.2:latest")
output_parsers = StrOutputParser()
chain = prompt | llm | output_parsers

if slt.button("Please click here to ask me"):
    if input_txt is "":
        slt.write("Please ask your questions in My Chat Box")
    else:
        slt.write(chain.invoke({"questions": input_txt}))
