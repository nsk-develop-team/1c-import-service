import datetime
import os
import sys
import uuid

sys.path.append(os.getcwd())  # для корректного импорта VSCode
from src.xml.xmlConverter.creator import create_xml


def test_create_xml():
    """Test function create_xml in creator.py."""
    data = [
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
             'amount': '1670',
             'account': 'TATAN',
             'currency': 'USD',
             'created_date': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
             'local_currency': '118018.9',
             'rate': '70.67',
             'doc_number': '1000-000001',
             'comment': 'blablabla'
        }
    ]
    create_xml(data)


if __name__ == '__main__':
    test_create_xml()
