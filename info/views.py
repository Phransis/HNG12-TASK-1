# from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timezone

# Create your views here.

def get_info(requests):
    email = "duofrancis11@gmail.com"
    current_datetime = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    github_url = "https://github.com/Phransis/HNG12-INTERNSHIP.git"
    response = {"email": email, "current_datetime": current_datetime, "github_url": github_url}
    return JsonResponse(response)
