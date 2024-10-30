from celery import shared_task
from mail_service.gmail_service import get_gmail_service, send_mail  # Импортируем send_mail отсюда
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_email_task(sender, recipient, subject, message):
    """Задача отправки письма через Gmail API в фоне"""
    try:
        logger.info(f"Отправка письма на {recipient}")
        service = get_gmail_service()
        send_mail(service, sender, recipient, subject, message)
        logger.info(f"Письмо отправлено на {recipient}")
        return f"Email sent to {recipient}"
    except Exception as e:
        logger.error(f"Ошибка при отправке письма: {str(e)}", exc_info=True)
        raise e  # Повторно бросаем исключение для корректной обработки Celery
