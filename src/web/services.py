import logging
import os
import time
import uuid

from .auth import auth_to_1c
from src.exceptions import (AuthTo1СError, CreateXmlError, SplitZipFileError,
                            XmlToZipError, SendFileError)
from src.xml.xmlConverter.archiver import split_zip_file, xml_to_zip
from src.xml.xmlConverter.constants import (DATA_PATH, DATAFILE_ZIP_PATH,
                                            MAX_SIZE, TRY_COUNTER)
from src.xml.xmlConverter.creator import create_xml

logger = logging.getLogger('web')


def auth():
    """Authorization to 1C web service use environment"""
    try:
        service_url = os.getenv('1C_WEB_URL')
        login = os.getenv('1C_USER_NAME')
        password = os.getenv('1C_WEB_PASSWD')
        client = auth_to_1c(service_url, login, password)
        return client
    except Exception as err:
        raise AuthTo1СError(f'Exception: {err}')


def test_connection(client):
    """Checks connection with the 1C service.
    """
    if not client.service.TestConnection():
        raise AuthTo1СError('TestConnection returns FALSE.')


def send_file(client):
    """Send file to 1C web service
    """
    try:
        file_id = str(uuid.uuid4())
        if os.path.getsize(DATAFILE_ZIP_PATH) < MAX_SIZE:
            with open(DATAFILE_ZIP_PATH, 'rb') as zf:
                file_data = zf.read()

            client.service.PutFilePart(file_id, 0, file_data)
            logger.info('PutFilePart - OK')
        else:
            split_zip_file(MAX_SIZE)

            part_number = 1
            part_path = f"{DATAFILE_ZIP_PATH}.{part_number + 0:03d}"
            client = test_connection(client=client)
            while os.path.exists(part_path):
                with open(part_path, 'rb') as zf:
                    file_data = zf.read()
                client.service.PutFilePart(
                    file_id, part_number, file_data
                )
                logger.info('PutFilePart - OK')
                part_number += 1
                part_path = f'{DATAFILE_ZIP_PATH}.{part_number + 0:03d}'
        return file_id

    except Exception as err:
        raise SendFileError(f'Exception: {err}')


def put_data_to_web_1c(client, data):
    """Authorized in a 1C web service, collects a XML from input data,
    archives and sends them to a web service.
    """
    try:
        create_xml(data)
        xml_to_zip()
        file_id = send_file(client)

        response = client.service.PutData(file_id)

        counter = TRY_COUNTER
        while counter:
            counter -= 1
            logger.info('Try to PutDataActionResult...')
            result = client.service.PutDataActionResult(
                response['OperationID']
            )
            if result['return'] != 'Active':
                break
            time.sleep(5)

        logger.info(result)
        if result['return'] == 'Completed':
            for f in os.listdir(DATA_PATH):
                os.remove(os.path.join(DATA_PATH, f))
            return True
        else:
            return False

    except FileNotFoundError as err:
        raise Exception(f'FileNotFoundError: {err}')
    except (AuthTo1СError, CreateXmlError, XmlToZipError, SplitZipFileError, SendFileError) as err:
        raise Exception(f'{err.__class__.__name__}: {err}')
    except KeyError as err:
        raise Exception(f'Incorrect response from the PutData method: {err}')
    except Exception as err:
        raise Exception(f'Unexpected error: {err}')
