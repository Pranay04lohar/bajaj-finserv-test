from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re

# User details (replace with actual details)
FULL_NAME = "pranay_lohar"
DOB = "10022004"
EMAIL = "22bai70929@cuchd.in"
ROLL_NUMBER = "22BAI70929"
USER_ID = f"{FULL_NAME}_{DOB}"

@csrf_exempt
def process_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            
            if "data" not in data or not isinstance(data["data"], list):
                return JsonResponse({"is_success": False, "message": "Invalid input format"}, status=400)
            
            numbers = [x for x in data["data"] if x.isdigit()]
            alphabets = [x for x in data["data"] if re.match(r'^[a-zA-Z]$', x)]
            highest_alphabet = max(alphabets, key=lambda c: c.upper(), default="")
            highest_alphabet = [highest_alphabet] if highest_alphabet else []
            
            response = {
                "is_success": True,
                "user_id": USER_ID,
                "email": EMAIL,
                "roll_number": ROLL_NUMBER,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": highest_alphabet
            }
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"is_success": False, "message": str(e)}, status=500)
    
    return JsonResponse({"is_success": False, "message": "Invalid request method"}, status=405)

def get_operation_code(request):
    if request.method == "GET":
        return JsonResponse({"operation_code": 1})
    
    return JsonResponse({"is_success": False, "message": "Invalid request method"}, status=405)
