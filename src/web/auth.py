import logging

import requests.exceptions
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport

from ..exceptions import AuthTo1СError

logger = logging.getLogger('web')


def auth_to_1c(service_url, user, password):
    """Authorization in the 1C service
    according to the transferred parameters.
    """
    try:
        session = Session()
        session.auth = HTTPBasicAuth(user, password)
        transport = Transport(session=session)
        client = Client(service_url, transport=transport)
        logger.info('auth_to_1c - OK')

        return client

    except requests.exceptions.HTTPError as err:
        raise AuthTo1СError(f'requests.exceptions.HTTPError: {err}')
    except Exception as err:
        raise AuthTo1СError(f'Exception: {err}')
