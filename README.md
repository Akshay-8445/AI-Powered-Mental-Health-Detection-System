# MindEase - AI Powered Mental Health Detection System

## Overview

MindEase is an AI-powered web application designed to analyze user text and identify potential mental health concerns. The system uses Natural Language Processing (NLP) and Machine Learning techniques to understand user emotions and provide supportive feedback based on the detected mental state.

The project aims to promote mental health awareness by offering a simple and accessible platform where users can express their feelings and receive AI-generated insights.

## Features

* Mental health sentiment analysis
* Emotion detection from user text
* AI-generated supportive responses
* User-friendly web interface
* Fast and accurate text processing
* Real-time analysis
* Secure API integration
* Responsive design

## Technology Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* FastAPI

### AI & Machine Learning

* Google gemini API
* Natural Language Processing (NLP)

### Database (if used)

* SQLite / MySQL

## Project Structure

```text
MindEase/
│
├── frontend/
├── backend/
├── static/
├── templates/
├── main.py
├── requirements.txt
├── .env
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/MindEase.git
```

2. Navigate to the project directory

```bash
cd MindEase
```

3. Create a virtual environment

```bash
python -m venv .venv
```

4. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Create a .env file and add your API key

```env
OPENAI_API_KEY=your_api_key_here
```

7. Run the application

```bash
uvicorn main:app --reload
```

## Future Enhancements

* Multi-language support
* Advanced emotion classification
* User authentication system
* Mental health report generation
* Chat history storage
* Dashboard and analytics

## Disclaimer

This project is intended for educational and research purposes only. It is not a substitute for professional mental health diagnosis, treatment, or medical advice.

## Author

Akshay Pal
