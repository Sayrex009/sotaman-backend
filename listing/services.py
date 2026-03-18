import google.generativeai as genai
from django.conf import settings
from .models import announcement, AIGeneration

# Настройка API ключа (лучше хранить его в .env и брать из settings)
genai.configure(api_key=settings.GEMINI_API_KEY)

def evaluate_property(listing_id, user):
    try:
        listing = announcement.objects.get(id=listing_id)
    except announcement.DoesNotExist:
        return {"error": "Объявление не найдено"}

    # Формируем жесткий промпт, чтобы ИИ дал четкий ответ
    prompt = f"""
    Ты эксперт по оценке недвижимости. Оцени этот объект по шкале от 1 до 100 (где 100 - идеальное предложение на рынке по соотношению цены, площади и расположения).
    
    Данные объекта:
    - Название: {listing.title}
    - Описание: {listing.description}
    - Цена: {listing.price} у.е.
    - Город: {listing.city}
    - Адрес: {listing.address}
    - Площадь: {listing.area} кв.м.
    - Количество комнат: {listing.rooms}
    
    Твоя задача:
    1. На первой строке напиши ТОЛЬКО число от 1 до 100 (например: 85).
    2. На второй строке напиши краткое обоснование оценки (2-3 предложения).
    """

    try:
        # Используем модель flash, она быстрая и дешевая/бесплатная
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        ai_text = response.text.strip()
        
        # Сохраняем в твою базу данных
        ai_gen = AIGeneration.objects.create(
            user=user,
            listing=listing,
            prompt=prompt,
            result=ai_text
        )
        
        return {"success": True, "result": ai_text, "generation_id": ai_gen.id}
        
    except Exception as e:
        return {"error": str(e)}