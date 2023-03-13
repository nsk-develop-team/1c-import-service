import datetime
import os
import uuid

from src.web.services import put_data_to_web_1c
from src.web.auth import auth_to_1c


def test_put_data_to_web_1c():
    """Test function put_data_to_web_1c in creator.py."""
    data = [{
        'id': str(uuid.uuid4()),
        'amount': '1300',
        'account': 'CESAR',
        'currency': 'USD',
        'created_date': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        'local_currency': '99993.9',
        'rate': '70.67',
        'doc_number': '0000-999999',
        'comment': 'blablabla'
        },
        {
            'id': str(uuid.uuid4()),
            'amount': '1000',
            'account': 'VITOL',
            'currency': 'USD',
            'created_date': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            'local_currency': '100000.9',
            'rate': '70.67',
            'doc_number': '0000-999998',
            'comment': 'blablabla'
        }
    ]

    service_url = os.getenv('SERVICE_URL')
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    client = auth_to_1c(service_url, login, password)

    put_data_to_web_1c(client, data)


if __name__ == '__main__':
    test_put_data_to_web_1c()
