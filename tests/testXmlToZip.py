import os
import sys

sys.path.append(os.getcwd())  # для корректного импорта VSCode
from src.xml.xmlConverter.archiver import xml_to_zip
from tests.testCreateXml import test_create_xml


def test_xml_to_zip():
    """Test functions xml_to_zip in archiver.py."""
    test_create_xml()
    xml_to_zip()


if __name__ == '__main__':
    test_xml_to_zip()
