# johnstage1-api

# Number Classification API 🌟

A REST API that classifies numbers into interesting mathematical properties (prime, perfect, Armstrong, etc.) and fetches fun facts from an external API. Built with Python, FastAPI, and deployed on Heroku.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)

## Features 🚀
- **Input Validation**: Rejects non-integer inputs with 400 Bad Request
- **CORS Support**: Configured to allow cross-origin requests
- **Mathematical Checks**:
  - Prime number detection
  - Perfect number validation
  - Armstrong number check
  - Odd/even classification
  - Digit sum calculation
- **Async Fun Fact Fetching**: Integrates with [NumbersAPI](http://numbersapi.com)
- **JSON Responses**: Standardized output format

## Installation 💻
```bash
# Clone repository
git clone https://github.com/yourusername/number-classification-api.git
cd number-classification-api

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run server locally
uvicorn main:app --reload

Access API docs at http://localhost:8000/docs

API Endpoint 🔍
GET /api/classify-number?number={integer}

 Successful Response (200 OK)

{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

..........................

Error Response (400 Bad Request)
{
    "number": "abc",
    "error": true
}

Usage Examples 📖
# Test with curl
curl "https://your-heroku-app.herokuapp.com/api/classify-number?number=28"

# Sample output
{
    "number": 28,
    "is_prime": false,
    "is_perfect": true,
    "properties": ["even"],
    "digit_sum": 10,
    "fun_fact": "28 is the only known number that can be expressed as a sum of the first 5 primes..."
}

Deployment 🌐
Live URL: https://your-heroku-app.herokuapp.com/api/classify-number

Deployed using Heroku with:

Automatic Git integration

CORS configured for all origins

FastAPI production-ready server

Technologies Used 🛠️
Python 3.9+: Core programming language

FastAPI: Web framework with automatic OpenAPI docs

Heroku: Cloud platform for deployment

NumbersAPI: Fun fact data source

Poetry: Dependency management (optional)

Contributing 🤝
Fork the repository

Create feature branch (git checkout -b feature/amazing-feature)

Commit changes (git commit -m 'Add amazing feature')

Push to branch (git push origin feature/amazing-feature)

Open Pull Request

License 📄
This project is licensed under the MIT License - see LICENSE for details.