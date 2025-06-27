# AI Desktop Assistant

This project implements a desktop chatbot capable of understanding natural language commands to perform system actions like adjusting screen brightness and taking screenshots. [cite_start]It is built using Python, Flask for the web interface, and LangChain/LangGraph for the AI agent workflow, powered by a local Large Language Model[cite: 1].

## Objective

The primary objective of this project is to create a fully offline desktop chatbot that can:
* Run entirely without cloud APIs.
* Utilize a local LLM (specifically designed to run without GPU dependencies).
* Interpret natural language commands for system interactions.
* Execute predefined system actions (brightness control, screenshot capture).
* Leverage LangChain/LangGraph for robust AI agent workflows.

## Features

* **Local LLM Integration**: Uses `llama3.2:latest` (via Ollama) for natural language understanding and command processing, ensuring offline capability.
* **System Control Functions**:
    * Adjusts screen brightness (Windows compatible).
    * Takes screenshots and saves them locally with a timestamp.
* **LangChain/LangGraph Agent**: An intelligent agent orchestrates the interaction between the LLM and system tools, deciding which tool to call based on user input.
* **Web-based Chat Interface**: A simple and intuitive chat interface built with Flask allows users to interact with the assistant via a web browser.

## Supported Commands

The chatbot is designed to process natural language queries [cite: 5] and respond to the following types of commands:

* **Brightness Control:**
    * "Please increase my brightness"  (increases by 10% by default)
    * "Increase brightness by 20" (increases by a specified amount)
    * "Please decrease my brightness"  (decreases by 10% by default)
    * "Decrease brightness by 5" (decreases by a specified amount)
* **Screenshot:**
    * "Please take a screen shot" 
    * "Take a screenshot"
* **Mixed:**
    * "Increase the brightness and take a screenshot" 

     
## Setup Instructions

To get this AI Desktop Assistant up and running on your local machine, follow these steps:

### Prerequisites

* **Python 3.x**: Ensure you have Python installed.
* **Git**: For cloning the repository.
* **Ollama**: This project uses `llama3.2:latest` locally. You need to install Ollama and pull the model.
    1.  Download and install Ollama from [ollama.com](https://ollama.com/).
    2.  Open your terminal/command prompt and pull the `llama3.2:latest` model:
        ```bash
        ollama run llama3.2
        ```

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/silasrajtr/AI-desktop-asistant.git](https://github.com/silasrajtr/AI-desktop-asistant.git)
    cd AI-desktop-asistant
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    This will install Flask, LangChain, WMI, Pillow, and other necessary libraries.

4.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    The application will typically run on `http://127.0.0.1:5000/`.

5.  **Access the Chatbot:**
    Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Project Structure
