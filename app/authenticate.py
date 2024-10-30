from mail_service.gmail_service import get_gmail_service

if __name__ == '__main__':
    service = get_gmail_service(interactive=True)
    print("Аутентификация завершена. Токен сохранен.")
