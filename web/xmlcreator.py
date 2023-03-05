import datetime
import logging
import os

from constants import NAMES_MAP, NAMESPACES
from exceptions import CreateXmlError
from lxml import etree

logger = logging.getLogger('main')


def create_xml(data, path_to_web):
    """Creates an XML file filled with the data."""
    try:
        doc = etree.parse(path_to_web + '/templates/template.xml')

        for data_key, data_value in data.items():
            template_path = NAMES_MAP[data_key]
            if isinstance(template_path, dict):
                for path, value in template_path[data_value].items():
                    doc.find(path, namespaces=NAMESPACES).text = value
                continue

            doc.find(
                NAMES_MAP[data_key], namespaces=NAMESPACES
            ).text = data_value
        with open(path_to_web + "/data/datafile.xml", 'wb') as f:
            f.write(b'')
            doc.write(f, encoding='UTF-8')
        logger.info('create_xml - OK')

    except FileNotFoundError as err:
        logger.error(f'FileNotFoundError: {err}')
        raise CreateXmlError
    except Exception as err:
        logger.exception(f'Exception: {err}')
        raise CreateXmlError


def main():
    """FOR TESTS."""
    data = {
        'amount': '1670',
        'account': 'ILONMASK',
        'created_date': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        'local_currency': '118018.9',
        'rate': '70.67'
    }
    path_to_web = os.path.abspath('web')
    create_xml(data, path_to_web)


if __name__ == '__main__':
    main()