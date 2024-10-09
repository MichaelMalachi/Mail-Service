from django.db import models

from django.db import models

class Email(models.Model):
    sender = models.EmailField(max_length=254, verbose_name="От кого")
    recipient = models.EmailField(max_length=254, verbose_name="Кому")
    message = models.TextField(verbose_name="Текст письма")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    def __str__(self):
        return f"Email от {self.sender} к {self.recipient}"

