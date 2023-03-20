import datetime
import uuid


def create_order_data():
    return [
        {
            'id': str(uuid.uuid4()),
            'amount': '1670',
            'account': 'VITANYA',
            'currency': 'USD',
            'created_date': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            'local_currency': '118018.9',
            'rate': '70.67',
            'doc_number': '1000-000001',
            'comment': 'blablabla'
        },
        {
            'id': str(uuid.uuid4()),
            'amount': '3000',
            'account': 'TATAN',
            'currency': 'USD',
            'created_date': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            'local_currency': '999999.9',
            'rate': '70.67',
            'doc_number': '1000-000002',
            'comment': 'blablabla'
        }
    ]


def create_withdraw_data():
    return [
        {
            'id': str(uuid.uuid4()),
            'amount': '3000',
            'from_account': 'VITANYA',
            'to_account': 'HBG',
            'created_date': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            'doc_number': '1000-000003',
        },
        {
            'id': str(uuid.uuid4()),
            'amount': '10000',
            'from_account': 'TATAN',
            'to_account': 'HBGS',
            'created_date': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            'doc_number': '1000-000002',
        }
    ]