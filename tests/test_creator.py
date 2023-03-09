import datetime
import os
import sys

sys.path.append(os.getcwd())  # для корректного импорта VSCode
from src.xml.xml.creator import create_xml


def test_create_xml():
    """Test function create_xml in creator.py."""
    data = {
        'id': 'dd288a19-b0f5-11ed-8c28-00155d9b3aff',
        'amount': '1670',
        'account': 'VITANYA',
        'currency': 'USD',
        'created_date': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        'local_currency': '118018.9',
        'rate': '70.67',
        'doc_number': '1000-000001',
        'comment': 'blablabla'
    }
    create_xml(data)


if __name__ == '__main__':
    test_create_xml()
