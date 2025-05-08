🧠 Assignment-2: LLM-Powered PDF Question Answering App
This project is a Streamlit-based web application that leverages LangChain, FAISS, and Groq LLMs to allow users to:

Upload PDF documents

Ask questions based on the content

Receive answers extracted from the document or external tools (e.g., calculator, dictionary, or DuckDuckGo search)

View which tools were used, retrieved context, and the final answer

🚀 Features
📄 PDF Upload: Upload and read text from PDF documents.

💬 Question Answering: Ask natural language questions based on the document content.

🛠️ Tool Integration:

Calculator: Perform basic math operations.

Dictionary: Look up word definitions.

DocumentQA: Query the uploaded document.

DuckDuckGo Search: Search the web for additional information.

📚 Retrieval-Augmented Generation (RAG) using FAISS.

🤖 LangChain Agent orchestration.

🔎 Transparency: Displays which tools were used, the context retrieved, and the final answer.

🛠️ Installation
1. Set up the Virtual Environment (recommended):
bash
Copy
Edit
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate
2. Install the Dependencies:
bash
Copy
Edit
pip install -r requirements.txt
3. Set up Environment Variables:
Create a .env file in the root of the project directory and add the following variables:

ini
Copy
Edit
GROQ_API_KEY=your_groq_api_key
Replace your_groq_api_key with your actual Groq API key.

🧪 Usage
Once the application is set up, you can run it using Streamlit to interact with the web interface.

1. Run the Streamlit App:
bash
Copy
Edit
streamlit run app.py
2. Interacting with the Web UI:
Upload a PDF: Use the file uploader widget to upload a PDF document.

Enter a Query: Type a query related to the PDF into the input field.

View Results: The app will display:

✅ Tools/agents used for processing the query.

📄 Retrieved context snippets from the document (if applicable).

💡 Final answer to your query.

Example Query:
"What are the key points of the document on LLMs?"

Available Tools:
Calculator: Perform basic calculations.

Dictionary: Look up word definitions.

DocumentQA: Query the uploaded document.

DuckDuckGo Search: Conduct web searches.

📁 File Structure
bash
Copy
Edit
Assignment-2/
├── app.py                        # Main Streamlit app
├── requirements.txt              # Python package dependencies
├── .env                          # Environment variables (API keys)
└── src/
    └── llm_agent_project/
        ├── utils/
        │   └── utils.py          # Utility functions for LLM Agent and tool integration
        ├── exception.py          # Custom exception handling
        ├── logger.py             # Logging configuration
        └── ...
🛠️ Environment Variables
Create a .env file in the root directory and add the following keys:

ini
Copy
Edit
GROQ_API_KEY=your_groq_api_key
Replace your_groq_api_key with your actual Groq API key.

🤝 Contributing
We welcome contributions! If you'd like to improve the project, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Make your changes.

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature-name).

Create a new Pull Request.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.