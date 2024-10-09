from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import EmailForm


def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в базу данных
            return redirect('success')  # Перенаправление на страницу успеха (нужно создать или заменить)
    else:
        form = EmailForm()

    return render(request, 'home.html', {'form': form})