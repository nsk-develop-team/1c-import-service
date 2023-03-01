import base64
import os
import time
import xmlschema
import xml.etree.ElementTree as Et
import zipfile

import requests.exceptions
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport


def auth_to_1c(service_url, user, password):
    """Авторизация в сервисе 1С по переданным параметрам."""
    session = Session()
    session.auth = HTTPBasicAuth(user, password)
    transport = Transport(session=session)
    try:
        client = Client(service_url, transport=transport)
    except requests.exceptions.HTTPError as err:
        print(f"Ошибка авторизации: {err}")

        return False

    except Exception as err:
        print(f"Непредвиденная ошибка при авторизации: {err}")

        return False

    if client.service.TestConnection():
        print("AUTH_OK")
        return client

    return False


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


def put_data_to_web_1c(service_url, user, password, data):
    """Отправка XML файла в сервис 1С."""
    path_to_data = os.path.abspath("src/data/")
    auth_client = auth_to_1c(service_url, user, password)
    if not auth_client:
        print("АВТОРИЗАЦИЯ НЕ УДАЛАСЬ.")
        return
    create_xml(data, path_to_data)
    xml_to_zip(path_to_data)

    with open(path_to_data + '/datafile.zip', 'rb') as zip_file:
        with zipfile.ZipFile(zip_file) as zip_object:
            filenames = zip_object.namelist()
            with zip_object.open(filenames[0], 'r') as file:
                file_content = file.read()

    base64_data = base64.b64encode(file_content)
    if os.path.getsize(path_to_data + "/datafile.zip") < 2 * 1024 * 1024:
        auth_client.service.PutFilePart("test", 0, base64_data)
        auth_client.service.PutData("test")
        time.sleep(10)
        print(auth_client.service.PutDataActionResult("testOperationID"))


def main():
    """Объявляет входные данные и вызывает функцию отправки XML."""
    data = {
        'amount': '1670',
        'account': 'ILONMASK',
        'currency': 'USD',
        'created_date': '',
        'local_currency': '118018.9',
        'rate': '70.67'
    }
    service_url = ('http://67.211.215.240/InfoBase/ws/'
                   'EnterpriseDataUpload_1_0_1_1?wsdl')
    user = 'test'
    password = '12345'
    put_data_to_web_1c(service_url, user, password, data)


if __name__ == "__main__":
    main()
