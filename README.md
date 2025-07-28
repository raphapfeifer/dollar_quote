# 📈 Dollar Exchange Rate Notifier via WhatsApp

A Python-based serverless application that retrieves the current USD/BRL exchange rate and sends it as a WhatsApp message using the Meta/Facebook Graph API. Built for deployment on AWS Lambda.

## 🚀 Features

- Fetches real-time USD to BRL exchange rate
- Sends the exchange rate via WhatsApp using the Facebook Graph API
- Uses environment variables for security and configuration
- Designed to run on AWS Lambda with support for local testing

## 🧰 Tech Stack

- Python 3.13+
- [httpx](https://www.python-httpx.org/)
- [FastAPI (optional)](https://fastapi.tiangolo.com/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- AWS Lambda (serverless runtime)
- Facebook Graph API for WhatsApp Business

## 📦 Installation

Clone the repository:

git clone https://github.com/raphapfeifer/dollar_quote.git

Install dependencies:

pip install -r requirements.txt
