import datetime
import logging
import os

from lxml import etree

from ...exceptions import CreateXmlError
from ..config.config import ACCOUNTS_CONFIG
from .constants import ACCOUNTS_PATHS, NAMES_MAP, NAMESPACES

logger = logging.getLogger('main')


def create_xml(data):
    """Creates an XML file filled with the data."""
    try:
        parent_dir_path = os.path.dirname(os.path.dirname(__file__))
        doc = etree.parse(parent_dir_path + '/templates/template.xml')
        doc.find(
            'msg:Header/msg:CreationDate', namespaces=NAMESPACES
        ).text = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        for data_key, data_value in data.items():
            template_path = NAMES_MAP[data_key]

            if template_path == ACCOUNTS_PATHS:
                account_data = ACCOUNTS_CONFIG[data_value]
                for var_name, value in account_data.items():
                    for path in ACCOUNTS_PATHS[var_name]:
                        doc.find(path, namespaces=NAMESPACES).text = value
                continue

            if template_path:
                doc.find(
                    template_path, namespaces=NAMESPACES
                ).text = data_value

        with open(parent_dir_path + "/data/datafile.xml", 'wb') as f:
            f.write(b'')
            doc.write(f, encoding='UTF-8')
        logger.info('create_xml - OK')

    except KeyError as err:
        logger.error(f'KeyError: {err}')
        raise CreateXmlError
    except FileNotFoundError as err:
        logger.error(f'FileNotFoundError: {err}')
        raise CreateXmlError
    except Exception as err:
        logger.exception(f'Exception: {err}')
        raise CreateXmlError

# acc_id, name, fullname, stock_id, stock_name, contract = (
#                     ACCOUNT_MAP[data_value].values()
#                 )

# def old_create_xml(data):
#     """Creates an XML file filled with the data."""
#     try:
#         parent_dir_path = os.path.dirname(os.path.dirname(__file__))
#         doc = etree.parse(parent_dir_path + '/templates/template.xml')
#         doc.find(
#             'msg:Header/msg:CreationDate', namespaces=NAMESPACES
#         ).text = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

#         for data_name, data_value in data.items():
#             template_path = NAMES_MAP[data_name]
#             if isinstance(template_path, dict):
#                 acc_id, fullname, sklad_name = ACCOUNT_MAP[data_value].values
#                 for path, value in template_path[data_value].items():
#                     doc.find(path, namespaces=NAMESPACES).text = value
#                 continue

#             if template_path:
#                 doc.find(
#                     template_path, namespaces=NAMESPACES
#                 ).text = data_value

#         with open(parent_dir_path + "/data/datafile.xml", 'wb') as f:
#             f.write(b'')
#             doc.write(f, encoding='UTF-8')
#         logger.info('create_xml - OK')

#     except KeyError as err:
#         logger.error(f'KeyError: {err}')
#         raise CreateXmlError
#     except FileNotFoundError as err:
#         logger.error(f'FileNotFoundError: {err}')
#         raise CreateXmlError
#     except Exception as err:
#         logger.exception(f'Exception: {err}')
#         raise CreateXmlError
