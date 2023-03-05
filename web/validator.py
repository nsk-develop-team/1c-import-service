"""
Для тестов !.
"""
import os

from lxml import etree


def xmlvalidator(path_to_web):
    # Путь к XML-файлу и XSD-схеме
    xml_file = path_to_web + '/data/datafile.xml'
    xsd_file = path_to_web + '/templates/XSDschemeEntepriseData1_8.xsd'

    # Загрузка XSD-схемы
    with open(xsd_file, 'r') as f:
        xsd_content = f.read()
    xsd_schema = etree.XMLSchema(etree.fromstring(xsd_content))

    # Проверка XML на соответствие XSD-схеме
    with open(xml_file, 'r') as f:
        xml_content = f.read()
    xml_data = etree.fromstring(xml_content)
    is_valid = xsd_schema.validate(xml_data)

    # Вывод результата проверки
    if is_valid:
        print('XML соответствует XSD-схеме')
    else:
        print('XML не соответствует XSD-схеме')
        print(xsd_schema.error_log)


def test_validator():
    """FOR TESTS."""
    path_to_web = os.path.dirname(__file__)
    xmlvalidator(path_to_web)


if __name__ == '__main__':
    test_validator()
