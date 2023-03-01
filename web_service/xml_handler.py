import os
import xmlschema
import xml.etree.ElementTree as Et
import zipfile


def create_xml(data, path_to_data):
    """Создаёт XML файл из переданных файлов"""
    # Путь к XSD схеме
    # xsd_path = path_to_data + 'xsd_scheme.xsd'

    # # Загружаем и компилируем XSD схему
    # schema = xmlschema.XMLSchema(xsd_path)

    # create the root element
    root = Et.Element('data')

    # create child elements with input data
    amount = Et.SubElement(root, 'amount')
    amount.text = data['amount']

    account = Et.SubElement(root, 'account')
    account.text = data['account']

    currency = Et.SubElement(root, 'currency')
    currency.text = data['currency']

    created_date = Et.SubElement(root, 'created_date')
    created_date.text = data['created_date']

    local_currency = Et.SubElement(root, 'local_currency')
    local_currency.text = data['local_currency']

    rate = Et.SubElement(root, 'rate')
    rate.text = data['rate']

    # create and write the XML file
    xml_string = Et.tostring(root)
    try:
        with open(path_to_data + "/datafile.xml", 'wb') as f:
            f.write(xml_string)
    except FileNotFoundError as err:
        print(f"File path error: {err}")


def xml_to_zip(path_to_data):
    """Архивирует XML в ZIP-файл."""
    xml_file_name = path_to_data + "/datafile.xml"
    zip_file_name = path_to_data + "/datafile.zip"
    # Create ZIP, Writes an xml file to it, Delete xml
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_STORED) as zip_file:
        zip_file.write(xml_file_name)
    os.remove(xml_file_name)


def split_zip_file(path_to_data):
    """Split a ZIP file into chunks of a given size."""
    filepath = path_to_data + "/datafile.zip"
    chunk_size=2097152  # 2MB = 2097152byte
    zipname, ext = os.path.splitext(filepath)
    with zipfile.ZipFile(filepath, 'r') as zip_file:
        num_chunks = (zip_file.getinfo(file).file_size for file in zip_file.namelist())
        for num, file in enumerate(zip_file.namelist()):
            num_chunk = 0
            with open(f"{zipname}_{num + 1:03d}{ext}", 'wb') as chunk:
                with zip_file.open(file, 'r') as source:
                    while True:
                        chunk_data = source.read(chunk_size)
                        if not chunk_data:
                            break
                        chunk.write(chunk_data)
                        num_chunk += len(chunk_data)
            num_chunks -= num_chunk
            if num_chunks <= 0:
                break