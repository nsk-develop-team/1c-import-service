import logging

import requests.exceptions
from exceptions import AuthTo1cError
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport

logger = logging.getLogger('main')


def auth_to_1c(service_url, user, password):
    """Авторизация в сервисе 1С по переданным параметрам."""
    try:
        session = Session()
        session.auth = HTTPBasicAuth(user, password)
        transport = Transport(session=session)
        client = Client(service_url, transport=transport)

        if not client.service.TestConnection():
            logger.error('TestConnection returns FALSE')

            raise AuthTo1cError

        logger.info('auth_to_1c - OK')

        return client

    except requests.exceptions.HTTPError as err:
        logger.error(f'requests.exceptions.HTTPError: {err}')
        raise AuthTo1cError
    except Exception as err:
        logger.exception(f'Exception: {err}')
        raise AuthTo1cError
