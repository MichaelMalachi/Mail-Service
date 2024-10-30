from django.shortcuts import render, redirect
from .forms import EmailForm
from mail_service.tasks import send_email_task  # Импортируем задачу отсюда

import logging

logger = logging.getLogger(__name__)

def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            # Сохраняем данные в базу данных
            email_instance = form.save(commit=False)

            # Устанавливаем фиксированный email отправителя
            sender = 'vadym.halivets@gmail.com'
            recipient = email_instance.recipient
            message = email_instance.message

            # Отправляем письмо асинхронно через Celery
            send_email_task.delay(
                sender=sender,
                recipient=recipient,
                subject="Новое письмо от Django",
                message=message
            )
            logger.info(f"Задача send_email_task отправлена для получателя {recipient}")
            # Сохраняем данные после отправки
            email_instance.sender = sender  # Сохраняем отправителя в базу данных, если это нужно
            email_instance.save()

            return redirect('success')
    else:
        form = EmailForm()

    return render(request, 'home.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')
