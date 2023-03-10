import datetime
import logging

import pytz
from lxml import etree

from .config import NAMES_MAP
from .constants import DATAFILE_XML_PATH, DOC_PATH, NAMESPACES

logger = logging.getLogger('web')

moscow_tz = pytz.timezone('Europe/Moscow')
moscow_time = datetime.datetime.now(moscow_tz)
formatted_time = moscow_time.strftime("%Y-%m-%dT%H:%M:%S")


def create_xml(data):
    """Creates an XML file filled with the data."""
    try:
        doc = etree.parse(DOC_PATH)
        doc.find(
            'msg:Header/msg:CreationDate', namespaces=NAMESPACES
        ).text = formatted_time

        for data_key, data_value in data.items():
            template_path = NAMES_MAP[data_key]

            if isinstance(template_path, tuple):
                account_paths, account_data = template_path
                for var_name, value in account_data[data_value].items():
                    for path in account_paths[var_name]:
                        doc.find(path, namespaces=NAMESPACES).text = value
                continue

            if template_path:
                doc.find(
                    template_path, namespaces=NAMESPACES
                ).text = data_value

        with open(DATAFILE_XML_PATH, 'wb') as f:
            f.write(b'')
            doc.write(f, encoding='UTF-8')
        logger.info('create_xml - OK')

        return True

    except KeyError as err:
        logger.error(f'KeyError: {err}')
        return False
    except FileNotFoundError as err:
        logger.error(f'FileNotFoundError: {err}')
        return False
    except Exception as err:
        logger.exception(f'Exception: {err}')
        return False
