from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.

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
    digits = [int(digit) for digit in str(num)]
    power = len(digits)
    return sum(d ** power for d in digits) == num

def get_fun_fact(num):
    url = f"http://numbersapi.com/{num}"
    try:
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Funfact not available"
    except requests.RequestException:
        return "Error returning fact"

# def classify_number(request, num):
#     try:
#         digit_sum = sum(int(digit) for digit in str(num))
#         properties = []

#         # Check if the number is an Armstrong number
#         if is_armstrong(num):

#         # Check if the number is odd or even
#             properties.append("odd" if num % 2 else "even")
#         properties.append("armstrong")
#         properties.append("odd" if num % 2 else "even") 
#         print(properties)

#         # Return the result as a JSON response
#         return JsonResponse({
#             "number": num,
#             "is_prime": is_prime(num),
#             "is_perfect": is_perfect(num),
#             "properties": properties,  # This will be ["armstrong", "odd"] or ["armstrong", "even"]
#             "digit_sum": digit_sum,
#             "fun_fact": get_fun_fact(num)
#         })
#     except ValueError:
#         return JsonResponse({"number": "alphabet", "error": True})
def classify_number(request):
    try:
        num = request.GET.get("number")  # Fetch from query params
        if not num or not num.isdigit():
            return JsonResponse({"number": num, "error": True} , status=400)
        
        digit_sum = sum(int(digit) for digit in str(num))


#         # Check if the number is an Armstrong number
        properties = []
        num = int(num)
        if is_armstrong(num):

#         # Check if the number is odd or even
            # properties.append("odd" if num % 2 else "even")
            properties.append("armstrong")
        properties.append("odd" if num % 2 else "even") 
        print(properties)

        return JsonResponse({
            "number": num,
            "is_prime": is_prime(num),
            "is_perfect": is_perfect(num),
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": get_fun_fact(num)
        })
    except ValueError:
        return JsonResponse({"number": "alphabet", "error": True} )
