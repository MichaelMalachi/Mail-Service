from django.urls import path
from mail_service.views import send_email_view, success_view

urlpatterns = [
    path('', send_email_view, name='send_email'),
    path('success/', success_view, name='success'),
]
