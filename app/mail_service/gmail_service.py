import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

# Области доступа - это права, которые запрашивает ваше приложение
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

BASE_DIR = Path(__file__).resolve().parent.parent  # Получаем базовую директорию проекта

def get_gmail_service(interactive=False):
    """Создает сервис Gmail API, выполняя аутентификацию при необходимости"""
    creds = None
    token_path = BASE_DIR / 'token.json'
    credentials_path = BASE_DIR / 'credentials.json'

    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                logger.warning(f"Не удалось обновить токен: {e}")
                creds = None
        if not creds:
            if interactive:
                if credentials_path.exists():
                    flow = InstalledAppFlow.from_client_secrets_file(str(credentials_path), SCOPES)
                    creds = flow.run_local_server(port=8080)  # Устанавливаем фиксированный порт
                    with open(token_path, 'w') as token:
                        token.write(creds.to_json())
                    logger.info("Новый токен сохранен в token.json")
                else:
                    raise FileNotFoundError(f"Файл credentials.json не найден по пути {credentials_path}.")
            else:
                raise Exception("Токен недействителен и интерактивная аутентификация не разрешена.")

    service = build('gmail', 'v1', credentials=creds)
    return service

def send_mail(service, sender, recipient, subject, message):
    """Отправляет письмо с помощью Gmail API"""
    try:
        mime_message = MIMEMultipart()
        mime_message['To'] = recipient
        mime_message['From'] = sender
        mime_message['Subject'] = subject
        mime_message.attach(MIMEText(message, 'plain'))

        raw_message = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()
        message_body = {'raw': raw_message}

        service.users().messages().send(userId='me', body=message_body).execute()
        logger.info(f"Письмо успешно отправлено на {recipient}")
    except Exception as e:
        logger.error(f"Ошибка при отправке письма на {recipient}: {str(e)}", exc_info=True)
        raise e  # Повторно бросаем исключение для обработки в вызывающем коде
