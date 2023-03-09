import datetime
import os
import sys
import uuid

sys.path.append(os.getcwd())  # для корректного импорта VSCode
from main import put_data_to_web_1c


def main():
    """Test function put_data_to_web_1c in creator.py."""
    data = {
        'id': str(uuid.uuid4()),
        'amount': '1670',
        'account': 'CESAR',
        'currency': 'USD',
        'created_date': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        'local_currency': '118018.9',
        'rate': '70.67',
        'doc_number': '0000-999999',
        'comment': 'blablabla'
    }
    put_data_to_web_1c(None, data)


if __name__ == '__main__':
    main()
