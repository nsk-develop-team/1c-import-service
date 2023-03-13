import datetime
import logging
import copy

import pytz
from lxml import etree

from ...exceptions import CreateXmlError
from .config import NAMES_MAP, BODY_PATH, GOOD_PATH
from .constants import DATAFILE_XML_PATH, DOC_PATH, NAMESPACES

logger = logging.getLogger('web')


def modify_good(good, order):
    """Update good fields from order data"""
    for order_key, order_value in order.items():
        template_path = NAMES_MAP[order_key]

        if order_key == 'account':
            account_paths, account_data = template_path
            for var_name, value in account_data[order_value].items():
                for path in account_paths[var_name]:
                    good.find(path, namespaces=NAMESPACES).text = value
            continue

        if template_path:
            if isinstance(template_path, tuple):
                for path in template_path:
                    good.find(path, namespaces=NAMESPACES).text = order_value
            else:
                good.find(template_path, namespaces=NAMESPACES).text = order_value

    return good


def create_xml(data):
    """Creates an XML file filled with the data."""
    try:
        moscow_tz = pytz.timezone('Europe/Moscow')
        moscow_time = datetime.datetime.now(moscow_tz)
        formatted_time = moscow_time.strftime("%Y-%m-%dT%H:%M:%S")

        doc = etree.parse(DOC_PATH)
        root_node = doc.getroot()
        root_node.find(
            'msg:Header/msg:CreationDate', namespaces=NAMESPACES
        ).text = formatted_time

        body = root_node.find(BODY_PATH, namespaces=NAMESPACES)
        template_good = root_node.find(GOOD_PATH, namespaces=NAMESPACES)
        body.remove(template_good)

        for order in data:
            good = modify_good(
                copy.deepcopy(template_good), order)
            body.append(good)

        with open(DATAFILE_XML_PATH, 'wb') as f:
            f.write(b'')
            doc.write(f, encoding='UTF-8')
        logger.info('create_xml - OK')

    except KeyError as err:
        raise CreateXmlError(f'KeyError: {err}')
    except FileNotFoundError as err:
        raise CreateXmlError(f'FileNotFoundError: {err}')
    except Exception as err:
        raise CreateXmlError(f'Exception: {err}')
