import datetime
import logging
import os
import time
import uuid
from logging.handlers import RotatingFileHandler

from archiver import split_zip_file, xml_to_zip
from auth import auth_to_1c
from dotenv import load_dotenv
from exceptions import (AuthTo1cError, CreateXmlError, SplitZipFileError,
                        XmlToZipError)
from xmlcreator import create_xml

load_dotenv()

logger = logging.getLogger('main')
logger.setLevel(logging.INFO)
handler = RotatingFileHandler('logs.log', maxBytes=50000000, backupCount=5)
logger.addHandler(handler)
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - '
    '%(funcName)s - %(lineno)d - %(message)s'
)
handler.setFormatter(formatter)


def put_data_to_web_1c(service_url, user, password, data):
    """Authorized in a 1C web service, collects a XML from input data,
    archives and sends them to a web service."""
    try:
        auth_client = auth_to_1c(service_url, user, password)
        path_to_web = os.path.abspath('web')
        create_xml(data, path_to_web)
        xml_to_zip(path_to_web)

        path_to_datafile = path_to_web + '/data/datafile.zip'
        file_id = str(uuid.uuid4())
        if os.path.getsize(path_to_datafile) < 2097152:
            with open(path_to_datafile, 'rb') as zip_file:
                file_data = zip_file.read()

            auth_client.service.PutFilePart(file_id, 0, file_data)
            logger.info('PutFilePart - OK')
        else:
            split_zip_file(path_to_datafile)
            part_number = 1
            part_path = f"{path_to_datafile}.{part_number + 0:03d}"

            while os.path.exists(part_path):
                with open(part_path, 'rb') as zip_file:
                    file_data = zip_file.read()

                auth_client.service.PutFilePart(
                    file_id, part_number, file_data
                )
                logger.info('PutFilePart - OK')
                part_number += 1
                os.remove(part_path)
                part_path = f'{path_to_datafile}.{part_number + 0:03d}'

        response = auth_client.service.PutData(file_id)
        time.sleep(5)

        result = auth_client.service.PutDataActionResult(
            response['OperationID']
        )
        logger.info(result)

    except FileNotFoundError as err:
        logger.error(f'FileNotFoundError: {err}')
        return
    except CreateXmlError as err:
        logger.error(f'CreateXmlError: {err}')
        return
    except AuthTo1cError as err:
        logger.error(f'AuthTo1cError: {err}')
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
        logger.exception(f'Unexpected error while working with file: {err}')
        return


def main():
    """Announces input data and calls the XML sending function."""
    data = {
        'amount': '1670',
        'account': 'ILONMASK',
        'created_date': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        'local_currency': '118018.9',
        'rate': '70.67'
    }
    service_url = os.getenv('SERVICE_URL')
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    put_data_to_web_1c(service_url, login, password, data)


if __name__ == '__main__':
    main()
