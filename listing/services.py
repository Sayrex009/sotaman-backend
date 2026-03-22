import google.generativeai as genai
from django.conf import settings
from .models import announcement, AIGeneration

genai.configure(api_key=settings.GEMINI_API_KEY)

def evaluate_property(listing_id, user):
    try:
        listing = announcement.objects.get(id=listing_id)
    except announcement.DoesNotExist:
        return {"error": "E'lon topilmadi"}

    prompt = f"""
    Siz ko'chmas mulkni baholash bo'yicha eksportsiz. Ushbu obyektni 1 dan 100 gacha bo'lgan shkalada baholang (bunda 100 - narx, maydon va joylashuv nisbati bo'yicha bozordagi ideal taklif).
    
    Obyekt ma'lumotlari:
    - Nomi: {listing.title}
    - Tavsifi: {listing.description}
    - Narxi: {listing.price}
    - Shahar: {listing.city}
    - Manzili: {listing.address}
    - Maydoni: {listing.area} kv.m.
    - Xonalar soni: {listing.rooms}
    
    Sizning vazifangiz:
    1. Birinchi qatorda FAQAT 1 dan 100 gacha bo'lgan raqamni yozing (masalan: 85).
    2. Ikkinchi qatorda baholashning qisqacha asosini yozing (2-3 ta gap).
    """

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        ai_text = response.text.strip()
        
        ai_gen = AIGeneration.objects.create(
            user=user,
            listing=listing,
            prompt=prompt,
            result=ai_text
        )
        
        return {"success": True, "result": ai_text, "generation_id": ai_gen.id}
        
    except Exception as e:
        return {"error": str(e)}