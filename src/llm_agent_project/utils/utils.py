from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.prompts import MessagesPlaceholder
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.tools import DuckDuckGoSearchRun
from simpleeval import simple_eval
from PyDictionary import PyDictionary
from langchain.chains import RetrievalQA
from src.llm_agent_project.exception import customexception
from src.llm_agent_project.logger import logging
import sys


import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
load_dotenv()


class Utils:
    def __init__(self):
        self.qa_chain = None
        self.llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=st.secrets["GROQ_API_KEY"])
        self.tools_used = []
        self.context_snippets = []

    def extract_text_from_pdf(self, pdf_path):
        try:
            doc = fitz.open(pdf_path)
            text = ""
            for page in doc:
                text += page.get_text()
            return text
        except Exception as e:
            logging.info("exception occured at data ingestion stage")
            raise customexception(e,sys)
           

    def process_pdfs_and_query(self, uploaded_file):
        try:
            if uploaded_file:
                pdf_contents = self.extract_text_from_pdf(uploaded_file)
                text_splitter = CharacterTextSplitter(separator="\n", chunk_size=800, chunk_overlap=200)
                split_texts = text_splitter.split_text(pdf_contents)

                embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
                db = FAISS.from_texts(split_texts, embeddings)

                retriever = db.as_retriever()
                self.qa_chain = RetrievalQA.from_chain_type(self.llm, retriever=retriever)
        except Exception as e:
            logging.info("exception occured at data ingestion stage")
            raise customexception(e,sys)
           

    def query_document(self, question: str):
        try:
            if self.qa_chain:
                result = self.qa_chain.run(question)
                # Capture the context snippets manually from the chain
                self.context_snippets.append(result)
                return result
            else:
                raise ValueError("QA chain not initialized.")
        except Exception as e:
            logging.info("exception occured at data ingestion stage")
            raise customexception(e,sys)
           

    def simple_calculator(self, query: str):
        try:
            self.tools_used.append("Calculator")
            return simple_eval(query)
        except Exception as e:
            logging.info("exception occured at data ingestion stage")
            raise customexception(e,sys)
           

    def define_word(self, query: str):
        try:
            self.tools_used.append("Dictionary")
            word = query.split("define", 1)[-1].strip()
            dictionary = PyDictionary()
            return dictionary.meaning(word)
        except Exception as e:
            logging.info("exception occured at data ingestion stage")
            raise customexception(e,sys)
           

    def duckduckgo_search(self, query: str):
        try:
            self.tools_used.append("DuckDuckGo Search")
            search_run = DuckDuckGoSearchRun()
            result = search_run.run(query)
            self.context_snippets.append(result)
            return result
        except Exception as e:
            logging.info("exception occured at data ingestion stage")
            raise customexception(e,sys)
           

    def create_and_run_agent(self, query: str):
        try:
            tools = [
                Tool(name="Calculator", func=self.simple_calculator, description="Handles math"),
                Tool(name="Dictionary", func=self.define_word, description="Defines words"),
                Tool(name="DocumentQA", func=self.query_document, description="Answers questions from the uploaded document"),
                Tool(name="DuckDuckGo Search", func=self.duckduckgo_search, description="Searches DuckDuckGo")
            ]

            # Initialize the agent
            agent = initialize_agent(
                tools, self.llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
            )

            # Reset the tools and context each time the agent is called
            self.tools_used = []
            self.context_snippets = []
            
            # Execute the agent
            final_answer = agent.run(query)
            
            # Return the tools used, context snippets, and final answer
            return {
                "tools_used": self.tools_used,
                "context_snippets": self.context_snippets,
                "final_answer": final_answer
            }

        except Exception as e:
            logging.info("exception occured at data ingestion stage")
            raise customexception(e,sys)
           


    
