# LLM Agent for PDF Querying and Multi-Tool Integration

This project leverages cutting-edge language models (LLMs) and intelligent agents to process uploaded PDF documents, answer related queries, and integrate a variety of tools to enhance the user's experience. It includes functionalities like querying documents, performing calculations, looking up word definitions, and utilizing DuckDuckGo for web searches.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Overview

This system allows users to upload PDF documents, query them using natural language, and receive insightful answers. The LLM agent also interacts with external tools to extend its capabilities beyond document-based responses, including performing calculations, looking up word definitions, and retrieving real-time information via web search.

## Features

- **PDF Querying**: Users can upload a PDF and query the document with natural language. The system will retrieve context from the document and provide the relevant answer.
- **Tool Integration**:
  - **Calculator**: Perform basic calculations directly from user queries.
  - **Dictionary**: Look up word definitions using PyDictionary.
  - **DuckDuckGo Search**: Perform real-time searches via DuckDuckGo.
- **LLM Agent**: The agent intelligently selects the necessary tool(s) to answer queries based on the context.

## Technologies Used

- **Streamlit**: Used to build the interactive web UI.
- **LangChain**: For chaining multiple tools and creating intelligent agents.
- **Groq API**: A powerful LLM backend to process queries and documents.
- **PyMuPDF (fitz)**: Used for extracting text from PDF documents.
- **FAISS**: For efficient similarity search on the document content.
- **Sentence-Transformer**: For embedding document content into vector space.
- **Simpleeval**: A lightweight mathematical expression evaluator.
- **PyDictionary**: For retrieving word definitions.
- **DuckDuckGo**: For web searches in response to user queries.

## Installation

### Prerequisites

Ensure that you have Python 3.7 or higher installed. You will also need an API key for Groq and possibly other services.

### Steps to Install

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kishan444444/RAG-Powered-Multi-Agent-Q-A-Assistant.git
   cd RAG-Powered-Multi-Agent-Q-A-Assistant
Set up the virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables:
Create a .env file in the root of the project and add your API keys, such as the GROQ_API_KEY.

Example .env file:

bash
Copy
Edit
GROQ_API_KEY=your_groq_api_key
Usage
Once the application is set up, you can run it using Streamlit to interact with the web interface.

Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Interacting with the Web UI:

Upload a PDF: Use the file uploader widget to upload a PDF document.

Enter a Query: Type a query related to the PDF into the input field.

View Results: The app will display:

The tools/agents used for processing the query.

The retrieved context snippets from the document (if applicable).

The final answer to your query.

Example Query:
"What are the key points of the document on LLMs?"

Available Tools:
Calculator: Perform basic calculations.

Dictionary: Look up word definitions.

DocumentQA: Query the uploaded document.

DuckDuckGo Search: Conduct web searches.

File Structure
bash
Copy
Edit
Assignment-2/
├── app.py               # Main Streamlit app
├── requirements.txt      # Python package dependencies
├── .env                  # Environment variables (API keys)
└── src/
    └── llm_agent_project/
        ├── utils/
        │   └── utils.py  # Utility functions for LLM Agent and tool integration
        ├── exception.py  # Custom exception handling
        ├── logger.py     # Logging configuration
        └── ...
Environment Variables
Create a .env file in the root directory and add the following keys:

bash
Copy
Edit
GROQ_API_KEY=your_groq_api_key
Replace your_groq_api_key with your actual Groq API key.

Contributing
We welcome contributions! If you’d like to improve the project, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Make your changes.

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature-name).

Create a new Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

yaml
Copy
Edit

---

### Instructions:

1. Copy the above content and paste it into a new file named `README.md` in your project’s root directory.
2. Save the file and commit it to your repository.
3. Push the changes to GitHub using the following commands:

```bash
git add README.md
git commit -m "Add professional README"
git push origin main