from django.contrib import admin
from django.urls import path
from app.views import LoginAPI, RegisterEmailAPI, VerifyEmailOTPAPI

urlpatterns = [
    path("register/", RegisterEmailAPI.as_view()),
    path("verify/", VerifyEmailOTPAPI.as_view()),
    path("login/", LoginAPI.as_view()),
    path('admin/', admin.site.urls),
]

