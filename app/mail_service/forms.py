from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['recipient', 'message']  # Убираем поле 'sender'
        labels = {
            'recipient': 'Кому',
            'message': 'Текст письма',
        }
        widgets = {
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }
