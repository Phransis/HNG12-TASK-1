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