import logging
import os
import uuid
import time

import requests.exceptions
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport

from ..exceptions import AuthTo1СError, SendFileError
from ..constants import MAX_SIZE, TRY_COUNTER

logger = logging.getLogger('web')


class Client1С:
    def __init__(self, service_url, user, password):
        self.client = self.auth_to_1c(service_url, user, password)

    @staticmethod
    def auth_to_1c(service_url, user, password):
        """Authorization in the 1C services
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

    def test_connection(self):
        """Checks connection with the 1C services.
        """
        if not self.client.service.TestConnection():
            raise AuthTo1СError('TestConnection returns FALSE.')

    def send_file(self, zip_file):
        """Send file to 1C web services
        """
        try:
            self.test_connection()

            file_id = str(uuid.uuid4())
            if os.path.getsize(zip_file) < MAX_SIZE:
                with open(zip_file, 'rb') as zf:
                    file_data = zf.read()

                self.client.service.PutFilePart(file_id, 0, file_data)
                logger.info('PutFilePart - OK')
            # TODO: set split attribute as method parameters
            #  \ and check filesize in the other way
            # else:
            #     split_zip_file(MAX_SIZE)
            #
            #     part_number = 1
            #     part_path = f"{DATAFILE_ZIP_PATH}.{part_number + 0:03d}"
            #     client = test_connection(client=client)
            #     while os.path.exists(part_path):
            #         with open(part_path, 'rb') as zf:
            #             file_data = zf.read()
            #         client.service.PutFilePart(
            #             file_id, part_number, file_data
            #         )
            #         logger.info('PutFilePart - OK')
            #         part_number += 1
            #         part_path = f'{DATAFILE_ZIP_PATH}.{part_number + 0:03d}'
            return file_id

        except Exception as err:
            raise SendFileError(f'Exception: {err}')

    def put_file_to_web_service(self, file_zip):
        """Authorized in a 1C web services, collects a XML from input data,
        archives and sends them to a web services.
        """
        try:
            file_id = self.send_file(file_zip)

            response = self.client.service.PutData(file_id)

            counter = TRY_COUNTER
            while counter:
                counter -= 1
                logger.info('Try to PutDataActionResult...')
                result = self.client.service.PutDataActionResult(
                    response['OperationID']
                )
                if result['return'] != 'Active':
                    break
                time.sleep(5)

            logger.info(result)
            # if result['return'] == 'Completed':
            #     for f in os.listdir(DATA_PATH):
            #         os.remove(os.path.join(DATA_PATH, f))
            #     return True
            # else:
            #     return False

        except FileNotFoundError as err:
            raise Exception(f'FileNotFoundError: {err}')
        except (AuthTo1СError, SendFileError) as err:
            raise Exception(f'{err.__class__.__name__}: {err}')
        except KeyError as err:
            raise Exception(f'Incorrect response from the PutData method: {err}')
        except Exception as err:
            raise Exception(f'Unexpected error: {err}')