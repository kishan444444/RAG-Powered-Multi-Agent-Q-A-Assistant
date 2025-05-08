# LLM Agent for PDF Querying and Multi-Tool Integration

This project uses Large Language Models (LLMs) and intelligent agents to process and answer queries related to PDF documents. It allows users to upload a PDF, ask questions, and retrieve answers by querying the document, performing calculations, looking up word definitions, and retrieving real-time information via DuckDuckGo search.

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

The system leverages Groq's powerful language models to process PDF documents, perform natural language queries, and integrate with multiple tools. The application is built using **Streamlit** for a user-friendly interface and includes functionalities such as:
- Document query answering
- Math calculation via a simple calculator
- Word definitions through PyDictionary
- Real-time searches using DuckDuckGo

## Features

- **PDF Querying**: Upload a PDF and ask a question related to its content.
- **Tool Integration**:
  - **Calculator**: Handles simple calculations.
  - **Dictionary**: Provides word definitions.
  - **DuckDuckGo Search**: Fetches real-time search results from DuckDuckGo.
- **LLM Agent**: Automatically selects the appropriate tool to respond to queries.
- **Contextual Responses**: Retrieves relevant context snippets from the document to enhance the quality of the answer.

## Technologies Used

- **Streamlit**: For building the interactive web UI.
- **Groq API**: For processing natural language queries.
- **LangChain**: For creating intelligent agents and chaining tools.
- **PyMuPDF (fitz)**: For extracting text from PDF files.
- **FAISS**: For efficient document retrieval and similarity search.
- **Sentence-Transformer**: For converting text into vector embeddings.
- **Simpleeval**: For evaluating basic mathematical expressions.
- **PyDictionary**: For looking up word definitions.
- **DuckDuckGo**: For performing real-time web searches.

## Installation

### Prerequisites

- Python 3.7+ is required.
- API keys for Groq and DuckDuckGo (if needed) should be obtained.

### Steps to Install

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kishan444444/Assignment-2.git
   cd Assignment-2
Set up a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables:
Create a .env file in the root directory and add your Groq API key:

bash
Copy
Edit
GROQ_API_KEY=your_groq_api_key
Usage
Once everything is set up, you can run the app using Streamlit.

Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Interacting with the Web UI:

Upload a PDF: Use the file uploader widget to upload a PDF document.

Enter your Query: Type in a query related to the document.

View Results: The app will display:

The tools/agents used for processing the query.

The retrieved context snippets from the document (if applicable).

The final answer to your query.

Example Query:
"What are the main points of the document?"

Available Tools:
Calculator: Perform basic arithmetic calculations.

Dictionary: Look up word definitions.

DocumentQA: Query the uploaded document for specific information.

DuckDuckGo Search: Perform a search on DuckDuckGo.

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
Create a .env file in the root directory with the following content:

bash
Copy
Edit
GROQ_API_KEY=your_groq_api_key
Replace your_groq_api_key with your actual API key.

Contributing
We welcome contributions to this project! If you'd like to improve the functionality, fix bugs, or add new features, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Make your changes and commit them (git commit -am 'Add new feature').

Push your changes to your fork (git push origin feature-name).

Open a Pull Request to the main repository.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

sql
Copy
Edit

### Instructions:

1. Copy and paste the above content into a `README.md` file in the root of your repository.
2. Save the file and commit it to your repository:

```bash
git add README.md
git commit -m "Add professional README"
git push origin main