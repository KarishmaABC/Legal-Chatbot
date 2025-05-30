# Legal Assistant Chatbot

A simple **Legal Assistant Chatbot** web application built using **Flask** and powered by OpenAI's **GPT-3.5-turbo** model.  
Users can ask legal questions and receive concise, relevant answers in a chat-based interface.

---

## Features

- Interactive chat-based legal assistant interface  
- Powered by OpenAI’s GPT-3.5-turbo model  
- Basic greeting handling  
- Clean, responsive frontend UI  
- CORS-enabled API for seamless frontend-backend communication  

---

## Tech Stack

| Backend                 | Frontend                   | Others           |
|------------------------|----------------------------|------------------|
| Python, Flask          | HTML, CSS, JavaScript (Vanilla) | Flask-CORS       |
| OpenAI API             |                            |                  |

---

## Project Structure

```text
legal_chatbot/
│
├── app.py                 # Flask backend application
├── templates/
│   └── index.html         # Main frontend HTML page
├── static/
│   └── style.css          # CSS styling
├── .env                   # (Optional) Store your API key securely
└── README.md              # Project documentation

## Prerequisites

- Python 3.7 or later  
- OpenAI API key ([Get yours here](https://platform.openai.com/account/api-keys))

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/legal-assistant-chatbot.git
   cd legal-assistant-chatbot


### Install Dependencies

```bash
pip install -r requirements.txt
```
### Set your OpenAI API key
```
export OPENAI_API_KEY="your-openai-api-key"      # macOS/Linux

set OPENAI_API_KEY="your-openai-api-key"         # Windows
```
Running the App
```
python app.py
```

![Screenshot (175)](https://github.com/user-attachments/assets/8aa4610f-2b15-448d-8c52-b6d4796ed2a2)

Open your browser and visit: http://127.0.0.1:5000
