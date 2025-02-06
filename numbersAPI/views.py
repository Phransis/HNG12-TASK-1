from django.http import JsonResponse
import requests

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    return num > 1 and sum(i for i in range(1, num) if num % i == 0) == num

def is_armstrong(num):
    digits = [int(digit) for digit in str(abs(num))]  # Handle negatives correctly
    power = len(digits)
    return sum(d ** power for d in digits) == abs(num)

def get_fun_fact(num):
    url = f"http://numbersapi.com/{num}"
    try:
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Fun fact not available"
    except requests.RequestException:
        return "Error returning fact"

def classify_number(request):
    try:
        num = request.GET.get("number")  # Fetch number from query params
        if num is None or not num.lstrip('-').isdigit():  # Validate input
            return JsonResponse({
                "number": num,
                "is_prime": False,
                "is_perfect": False,
                "properties": [],
                "digit_sum": None,
                "fun_fact": "Invalid number provided",
                "error": True
            }, status=400)

        num = int(num)  # Convert string to integer
        digit_sum = sum(int(digit) for digit in str(abs(num)))  # Sum digits ignoring sign

        # Determine number properties
        properties = []
        if is_armstrong(num):
            properties.append("armstrong")
        properties.append("odd" if num % 2 else "even")

        return JsonResponse({
            "number": num,
            "is_prime": is_prime(num),
            "is_perfect": is_perfect(num),
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": get_fun_fact(num)
        })
    
    except ValueError:
        return JsonResponse({
            "number": None,
            "is_prime": False,
            "is_perfect": False,
            "properties": [],
            "digit_sum": None,
            "fun_fact": "Invalid input",
            "error": True
        }, status=400)
