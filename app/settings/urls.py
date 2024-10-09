from django.urls import path
from mail_service.views import send_email_view

urlpatterns = [
    path('', send_email_view, name='send_email'),
]

