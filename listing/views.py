from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .services import evaluate_property
from .models import announcement

@login_required
def generate_ai_evaluation(request, listing_id):
    user = request.user
    
    if user.ai_credits < 1:
        return JsonResponse({"error": "Balanсda yeterli mablag' yo'q."}, status=402)
    
    response = evaluate_property(listing_id, user)
    
    if response.get("success"):
        user.ai_credits -= 1
        user.save()
        
        return JsonResponse({
            "message": "Baxolash muvaffaqiyatli yaratildi",
            "result": response["result"]
        })
    else:
        return JsonResponse({"error": response.get("error")}, status=400)