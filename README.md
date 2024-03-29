# Project Title

A brief description of your project.


# Project Title

This project develops a FastAPI application designed to automate the process of answering user questions by leveraging a combination of web scraping and advanced natural language processing (NLP) techniques. Here's a breakdown of its core functionality and components:

Core Functionality:
Automated Question Answering: Users can submit questions through an API endpoint. The application then programmatically searches Google to find relevant text snippets that can serve as context for the question.
Integration of NLP and Web Scraping: By utilizing the transformers library, specifically a pre-trained BERT model (bert-large-uncased-whole-word-masking-finetuned-squad), the application analyzes the context to generate accurate answers to the user's questions. This process is supported by web scraping techniques implemented with requests and BeautifulSoup to retrieve the necessary context from Google search results.
Technical Components:
FastAPI Framework: Chosen for its simplicity and performance, FastAPI provides the backbone for creating RESTful endpoints, handling requests, and returning responses to users in real-time.
BERT Model: A cutting-edge NLP model that understands the context of words in search queries. This project uses a version of BERT that has been fine-tuned for question-answering tasks, making it highly effective at generating relevant answers.
Web Scraping: Implemented with the requests library to fetch HTML content from Google and BeautifulSoup to parse and extract the specific text snippets that provide context for the question asked.
Pydantic: Utilized for data validation and settings management, ensuring that the questions received through the API meet the expected format.
How It Works:
Receiving Questions: Through the /ask endpoint, users can submit their questions in a structured format, thanks to Pydantic models.
Context Retrieval: The application searches Google with the user's question and extracts a snippet of text that likely contains the information needed to answer the question.
Answer Generation: Leveraging the power of the pre-trained BERT model, the application analyzes the context snippet and the question to pinpoint the most relevant answer.
Delivering Answers: The generated answer is then returned to the user as a response from the API.
This project exemplifies the innovative integration of web scraping with state-of-the-art NLP to create a dynamic question-answering system. It demonstrates practical applications of machine learning, providing a template for developing advanced AI-driven solutions that can navigate and interpret vast amounts of web content to deliver precise information on demand.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.x
- pip (Python package manager)

### Setting Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies for your project. Here's how you can set one up:

#### For Windows

```bash
# Navigate to your project directory
cd path/to/your/project

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate

### # Navigate to your project directory
cd path/to/your/project

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

### Intall dependancies

pip install -r requirements.txt

### Run Project

uvicorn main:app  --port 8001

@Clever Project