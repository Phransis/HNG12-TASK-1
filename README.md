# HNG Stage 1 - Number Classification API

This is a simple Number Classification API Django REST API for HNG Stage 1.

# How to Run Locally
git clone https://github.com/Phransis/HNG12-TASK-1.git
cd basic_info
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver


## API Endpoint
- **GET https://hng12-task-1-dubt.onrender.com/classify-number** → Returns number, is_prime, is_perfect, properties, digit_sum and fun_fact

## Response Format:
```json
{
    "number": 435,
    "is_prime": false,
    "is_perfect": false,
    "properties": [
        "armstrong",
        "odd"
    ],
    "digit_sum": 12,
    "fun_fact": "435 is a boring number."
}


{
    "number": "alphabet",
    "error": true
}

## Deployment Link
//hng12-task-1-dubt.onrender.com/classify-number

Learn More About Django

https://hng.tech/hire/python-developers

# HNG Stage 0 - Public API

This is a simple Django REST API for HNG Stage 0.

# How to Run Locally
git clone https://github.com/Phransis/HNG12-TASK-1.git
cd basic_info
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver


## API Endpoint
- **GET https://hng12-task-1-dubt.onrender.com/info** → Returns email, current datetime, and GitHub repo.

## Response Format:
```json
{
    "email": "duofrancis11@gmail.com",
    "current_datetime": "2025-01-30T01:51:02Z",
    "github_url": "https://github.com/Phransis/HNG12-TASK-1.git"
}


## Deployment Link
//hng12-task-1-dubt.onrender.com/info

Learn More About Django

https://hng.tech/hire/python-developers