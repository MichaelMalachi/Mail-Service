from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Указываем настройки Django по умолчанию для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')


# Создаем экземпляр приложения Celery
app = Celery('mail_service')

# Задаем конфигурацию Celery из настроек Django, используя префикс CELERY
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение задач в приложениях
app.autodiscover_tasks()
