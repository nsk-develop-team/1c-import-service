import os
import sys

sys.path.append(os.getcwd())  # для корректного импорта VSCode
from src.xml.xmlConverter.archiver import split_zip_file
from tests.testXmlToZip import test_xml_to_zip


def test_split_zip_file(size):
    """Test functions split_zip_file in archiver.py."""
    test_xml_to_zip()
    split_zip_file(size)


if __name__ == '__main__':
    TEST_SIZE = 4096
    test_split_zip_file(TEST_SIZE)
