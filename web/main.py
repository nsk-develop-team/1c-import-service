import datetime
import logging
import os
import time
import uuid
from logging import StreamHandler

from archiver import split_zip_file, xml_to_zip
from auth import auth_to_1c
from dotenv import load_dotenv
from exceptions import (AuthTo1cError, CreateXmlError, SplitZipFileError,
                        XmlToZipError)
from xmlcreator import create_xml

load_dotenv()

logger = logging.getLogger('main')
logger.setLevel(logging.INFO)
handler = StreamHandler()
logger.addHandler(handler)
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - '
    '%(funcName)s - %(lineno)d - %(message)s'
)
handler.setFormatter(formatter)


def test_connection(client):
    if client is None:
        service_url = os.getenv('SERVICE_URL')
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')
        client = auth_to_1c(service_url, login, password)

    while not client.service.TestConnection():
        logger.error('TestConnection returns FALSE. Try to reconnect...')
        time.sleep(5)
        client = auth_to_1c(service_url, login, password)

    return client


def put_data_to_web_1c(client, data):
    """Authorized in a 1C web service, collects a XML from input data,
    archives and sends them to a web service.
    """
    try:
        path_to_web = os.path.dirname(__file__)
        create_xml(data, path_to_web)
        xml_to_zip(path_to_web)

        path_to_datafile = path_to_web + '/data/datafile.zip'
        file_id = str(uuid.uuid4())
        if os.path.getsize(path_to_datafile) < 2097152:
            client = test_connection(client=client)
            with open(path_to_datafile, 'rb') as zip_file:
                file_data = zip_file.read()

            client.service.PutFilePart(file_id, 0, file_data)
            os.remove(path_to_datafile)
            logger.info('PutFilePart - OK')
        else:
            split_zip_file(path_to_datafile)
            part_number = 1
            part_path = f"{path_to_datafile}.{part_number + 0:03d}"

            client = test_connection(client=client)
            while os.path.exists(part_path):
                with open(part_path, 'rb') as zip_file:
                    file_data = zip_file.read()

                client.service.PutFilePart(
                    file_id, part_number, file_data
                )
                os.remove(part_path)
                logger.info('PutFilePart - OK')
                part_number += 1
                part_path = f'{path_to_datafile}.{part_number + 0:03d}'

        response = client.service.PutData(file_id)

        while True:
            result = client.service.PutDataActionResult(
                response['OperationID'])
            if result['return'] != 'Active':
                break
            time.sleep(5)

        logger.info(result)

    except FileNotFoundError as err:
        logger.error(f'FileNotFoundError: {err}')
        return
    except AuthTo1cError as err:
        logger.error(f'AuthTo1cError: {err}')
        return
    except CreateXmlError as err:
        logger.error(f'CreateXmlError: {err}')
        return
    except XmlToZipError as err:
        logger.error(f'XmlToZipError: {err}')
        return
    except SplitZipFileError as err:
        logger.error(f'SplitZipFileError: {err}')
        return
    except KeyError as err:
        logger.error(f'Incorrect response from the PutData method: {err}')
        return
    except Exception as err:
        logger.exception(f'Unexpected error: {err}')
        return


def main():
    """Announces input data, checks
    authorization and calls put_data_to_web_1c.
    """
    data = {
        'amount': '1670',
        'account': 'ILONMASK',
        'created_date': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        'local_currency': '118018.9',
        'rate': '70.67'
    }

    try:
        client = test_connection(client=None)
        put_data_to_web_1c(client, data)
    except AuthTo1cError as err:
        logger.error(f'AuthTo1cError: {err}')
        return
    except Exception as err:
        logger.exception(f'Unexpected error: {err}')
        return


if __name__ == '__main__':
    main()
