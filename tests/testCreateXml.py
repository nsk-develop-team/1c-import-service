import sys

from src.services.factory import XMLFactory
from src.services.archive import *
from tests.data import *

sys.path.append(os.getcwd())  # для корректного импорта VSCode


def test_create_xml():
    """Test function create_xml in creator.py."""
    order_data = create_order_data()
    withdraw_data = create_withdraw_data()

    factory = XMLFactory()
    file_order_path = factory.create_xml_file(order_data)
    xml_to_zip(file_order_path)
    file_withdraw_path = factory.create_xml_file(withdraw_data)


if __name__ == '__main__':
    test_create_xml()
