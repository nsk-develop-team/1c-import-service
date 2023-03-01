import requests.exceptions
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport


def auth_to_1c(service_url, user, password):
    """Авторизация в сервисе 1С по переданным параметрам."""
    session = Session()
    session.auth = HTTPBasicAuth(user, password)
    transport = Transport(session=session)
    try:
        client = Client(service_url, transport=transport)
    except requests.exceptions.HTTPError as err:
        print(f"Ошибка авторизации: {err}")

        return False

    except Exception as err:
        print(f"Непредвиденная ошибка при авторизации: {err}")

        return False

    if client.service.TestConnection():
        print("AUTH_OK")
        return client

    return False