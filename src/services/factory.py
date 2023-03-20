import pkgutil
import importlib
import datetime
import logging
import copy

import pytz
from lxml import etree

from src.exceptions import CreateXmlError
from src.constants import NAMESPACES, TEMPLATES_PATH, XML_DATA_PATH
from src.xml.model.entity import Entity
import src.xml.config as configuration

logger = logging.getLogger('web')


class XMLFactory:
    def __init__(self):
        self.entities = []
        self.load_configs()

    def load_configs(self):
        """Load configuration files
        """
        module_names = [name for _, name, _ in pkgutil.iter_modules(configuration.__path__)]
        for module_name in module_names:
            self.entities.append(Entity(importlib.import_module(configuration.__name__ + '.' + module_name)))

    def validation_config(self, data):
        """Search valid mapping schema
        for incoming data"""
        filtered_entities = list(filter(lambda entity: entity.is_valid(data), self.entities))
        if len(filtered_entities) == 0:
            raise Exception(f'Not found valid mapping for income data {data}')
        elif len(filtered_entities) > 1:
            raise Exception(f'Several valid mapping for income data {data}')
        else:
            return filtered_entities[0]

    def create_xml_file(self, data):
        """Create XML file from
        entity pattern with data"""
        try:
            entity = self.validation_config(data[0])
            xml_document = self.create_xml(entity, data)
            xml_document_path = XML_DATA_PATH + entity.file_name

            with open(xml_document_path, 'w+b') as f:
                f.write(b'')
                xml_document.write(f, encoding='UTF-8')
            logger.info('create_xml - OK')
            return xml_document_path

        except KeyError as err:
            raise CreateXmlError(f'KeyError: {err}')
        except FileNotFoundError as err:
            raise CreateXmlError(f'FileNotFoundError: {err}')
        except Exception as err:
            raise CreateXmlError(f'Exception: {err}')

    def create_xml(self, entity, data):
        """Fill in XML document with data."""
        moscow_tz = pytz.timezone('Europe/Moscow')
        moscow_time = datetime.datetime.now(moscow_tz)
        formatted_time = moscow_time.strftime("%Y-%m-%dT%H:%M:%S")

        doc = etree.parse(TEMPLATES_PATH + entity.template_name)
        root_node = doc.getroot()
        root_node.find(
            'msg:Header/msg:CreationDate', namespaces=NAMESPACES
        ).text = formatted_time

        body = root_node.find(entity.body_path, namespaces=NAMESPACES)
        template_element = root_node.find(entity.element_path, namespaces=NAMESPACES)
        body.remove(template_element)

        for item in data:
            element = self.modify_element(entity, copy.deepcopy(template_element), item)
            body.append(element)
        return doc

    @staticmethod
    def modify_element(entity, element, data):
        """Update good fields from order data"""
        for data_key, data_value in data.items():
            template_path = entity.mapping[data_key]

            if template_path == 'DICTIONARY':
                for var_name, value in entity.dictionary[data_value].items():
                    for path in entity.dictionary_mapping[var_name]:
                        element.find(path, namespaces=NAMESPACES).text = value
                continue

            if template_path:
                if isinstance(template_path, tuple):
                    for path in template_path:
                        element.find(path, namespaces=NAMESPACES).text = data_value
                else:
                    element.find(template_path, namespaces=NAMESPACES).text = data_value
        return element

