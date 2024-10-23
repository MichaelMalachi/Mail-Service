from django.shortcuts import render, redirect
from .forms import EmailForm
from .gmail_service import get_gmail_service, send_email

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

            # Отправляем письмо через Gmail API
            service = get_gmail_service()
            send_email(
                service=service,
                sender=sender,  # Используем фиксированный email
                to=recipient,
                subject="Новое письмо от Django",
                message_text=message
            )

            # Сохраняем данные после отправки
            email_instance.sender = sender  # Сохраняем отправителя в базу данных, если это нужно
            email_instance.save()

            return redirect('success')
    else:
        form = EmailForm()

    return render(request, 'home.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')