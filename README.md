# AI Desktop Assistant

This project implements a desktop chatbot capable of understanding natural language commands to perform system actions like adjusting screen brightness and taking screenshots. [cite_start]It is built using Python, Flask for the web interface, and LangChain/LangGraph for the AI agent workflow, powered by a local Large Language Model[cite: 1].

## Objective

The primary objective of this project is to create a fully offline desktop chatbot that can:
* [cite_start]Run entirely without cloud APIs[cite: 1].
* [cite_start]Utilize a local LLM (specifically designed to run without GPU dependencies)[cite: 2].
* [cite_start]Interpret natural language commands for system interactions[cite: 3].
* [cite_start]Execute predefined system actions (brightness control, screenshot capture)[cite: 4].
* [cite_start]Leverage LangChain/LangGraph for robust AI agent workflows[cite: 4].

## Features

* [cite_start]**Local LLM Integration**: Uses `llama3.2:latest` (via Ollama) for natural language understanding and command processing, ensuring offline capability[cite: 2, 5, 9].
* **System Control Functions**:
    * [cite_start]Adjusts screen brightness (Windows compatible)[cite: 6].
    * [cite_start]Takes screenshots and saves them locally with a timestamp[cite: 6].
* [cite_start]**LangChain/LangGraph Agent**: An intelligent agent orchestrates the interaction between the LLM and system tools, deciding which tool to call based on user input[cite: 7].
* [cite_start]**Web-based Chat Interface**: A simple and intuitive chat interface built with Flask allows users to interact with the assistant via a web browser[cite: 7].

## Supported Commands

[cite_start]The chatbot is designed to process natural language queries [cite: 5] and respond to the following types of commands:

* **Brightness Control:**
    * [cite_start]"Please increase my brightness" [cite: 5] (increases by 10% by default)
    * "Increase brightness by 20" (increases by a specified amount)
    * [cite_start]"Please decrease my brightness" [cite: 5] (decreases by 10% by default)
    * "Decrease brightness by 5" (decreases by a specified amount)
* **Screenshot:**
    * [cite_start]"Please take a screen shot" [cite: 5]
    * "Take a screenshot"

## Setup Instructions

To get this AI Desktop Assistant up and running on your local machine, follow these steps:

### Prerequisites

* **Python 3.x**: Ensure you have Python installed.
* **Git**: For cloning the repository.
* **Ollama**: This project uses `llama3.2:latest` locally. You need to install Ollama and pull the model.
    1.  Download and install Ollama from [ollama.com](https://ollama.com/).
    2.  Open your terminal/command prompt and pull the `llama3.2:latest` model:
        ```bash
        ollama pull llama3.2:latest
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
