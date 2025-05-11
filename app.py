import streamlit as st
from src.llm_agent_project.utils.utils import Utils
import os

#### Initialize the Utils class
utils = Utils()

def process_pdf_and_query(uploaded_file, query):
    try:
        # Save the uploaded file temporarily
        pdf_path = f"temp_{uploaded_file.name}"
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Process the PDF file and initialize the QA chain
        utils.process_pdfs_and_query(pdf_path)
        
        # Run the agent with the provided query and capture results
        result = utils.create_and_run_agent(query)
        
        # Delete the temporary file after processing
        os.remove(pdf_path)

        return result

    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Streamlit App
st.title("PDF Querying with LLM Agent")
st.write("Upload a PDF document and ask a question about it.")

# File uploader widget
uploaded_file = st.file_uploader("Choose a PDF", type=["pdf"])

# Text input for query
query = st.text_input("Enter your question:")

if uploaded_file and query:
    st.write("Processing your request...")

    # Process the PDF and query
    result = process_pdf_and_query(uploaded_file, query)

    if result:
        # Show tools used
        st.subheader("Tools/Agents Used:")
        for tool in result["tools_used"]:
            st.write(f"- {tool}")
        
        # Show context snippets
        st.subheader("Retrieved Context Snippets:")
        for snippet in result["context_snippets"]:
            st.write(f"- {snippet}")

        # Show final answer
        st.subheader("Final Answer:")
        st.write(result["final_answer"])








