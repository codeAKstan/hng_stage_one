import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@require_GET
def classify_number(request, number):
    # Input validation
    if not isinstance(number, int):
        return JsonResponse({
            "number": number,
            "error": True
        }, status=400)

    # Check if the number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(abs(n)**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Check if the number is a perfect number
    def is_perfect(n):
        if n < 2:
            return False
        divisors = [i for i in range(1, abs(n)) if n % i == 0]
        return sum(divisors) == abs(n)

    # Check if the number is an Armstrong number
    def is_armstrong(n):
        digits = [int(d) for d in str(abs(n))]
        length = len(digits)
        return sum(d**length for d in digits) == abs(n)

    # Calculate the sum of digits
    digit_sum = sum(int(d) for d in str(abs(number)))

    # Determine properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    # Fetch fun fact from Numbers API
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math")
        fun_fact = response.text if response.status_code == 200 else "No fun fact available"
    except requests.RequestException:
        fun_fact = "No fun fact available"

    # Prepare response
    response_data = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact,
    }
    return JsonResponse(response_data)