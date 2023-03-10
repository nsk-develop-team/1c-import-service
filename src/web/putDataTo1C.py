import logging
import os
import time
import uuid
from logging import StreamHandler

from dotenv import load_dotenv

from src.exceptions import (AuthTo1СError, CreateXmlError, SplitZipFileError,
                            XmlToZipError)
from src.web.auth import auth_to_1c
from src.xml.xmlConverter.archiver import split_zip_file, xml_to_zip
from src.xml.xmlConverter.constants import (DATA_PATH, DATAFILE_ZIP_PATH,
                                            MAX_SIZE, TRY_COUNTER)
from src.xml.xmlConverter.creator import create_xml

load_dotenv()


logger = logging.getLogger('web')
logger.setLevel(int(os.getenv('LOGGING_LEVEL')))
handler = StreamHandler()
logger.addHandler(handler)
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - '
    '%(funcName)s - %(lineno)d - %(message)s'
)
handler.setFormatter(formatter)


def test_connection(client):
    """Checks for an authorized client and
    checks the connection with the 1C service.
    """
    if client is None:
        service_url = os.getenv('SERVICE_URL')
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')
        logger.info('Client==None. Try to connect...')
        client = auth_to_1c(service_url, login, password)

    if not client.service.TestConnection():
        logger.error('TestConnection returns FALSE.')

        raise AuthTo1СError

    return client


def put_data_to_web_1c(client, data):
    """Authorized in a 1C web service, collects a XML from input data,
    archives and sends them to a web service.
    """
    try:
        for part_data in data:
            if not create_xml(part_data):
                raise CreateXmlError

            if not xml_to_zip():
                raise XmlToZipError

            file_id = str(uuid.uuid4())
            if os.path.getsize(DATAFILE_ZIP_PATH) < MAX_SIZE:
                client = test_connection(client=client)
                with open(DATAFILE_ZIP_PATH, 'rb') as zf:
                    file_data = zf.read()

                client.service.PutFilePart(file_id, 0, file_data)
                logger.info('PutFilePart - OK')
            else:
                if not split_zip_file(MAX_SIZE):
                    raise SplitZipFileError

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

            if result['return'] == 'Completed':
                for f in os.listdir(DATA_PATH):
                    os.remove(os.path.join(DATA_PATH, f))
            logger.info(result)

        return True

    except FileNotFoundError as err:
        logger.error(f'FileNotFoundError: {err}')
        return False
    except AuthTo1СError as err:
        logger.error(f'AuthTo1cError: {err}')
        return False
    except CreateXmlError as err:
        logger.error(f'CreateXmlError: {err}')
        return False
    except XmlToZipError as err:
        logger.error(f'XmlToZipError: {err}')
        return False
    except SplitZipFileError as err:
        logger.error(f'SplitZipFileError: {err}')
        return False
    except KeyError as err:
        logger.error(f'Incorrect response from the PutData method: {err}')
        return False
    except Exception as err:
        logger.exception(f'Unexpected error: {err}')
        return False
