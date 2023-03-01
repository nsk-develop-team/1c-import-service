import base64
import os
import time
import zipfile

from web_service.auth import auth_to_1c
from web_service.xml_handler import create_xml, split_zip_file, xml_to_zip


def put_data_to_web_1c(service_url, user, password, data):
    """Отправка XML файла в сервис 1С."""
    path_to_data = os.path.abspath("web_service/data/")
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
