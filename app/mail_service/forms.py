from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['sender', 'recipient', 'message']
        labels = {
            'sender': 'От кого',
            'recipient': 'Кому',
            'message': 'Текст письма',
        }
        widgets = {
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }
