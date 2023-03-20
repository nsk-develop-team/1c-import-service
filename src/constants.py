import os

MAX_SIZE = 2097152  # 2 MB = 2097152 byte

TRY_COUNTER = 10

ENTRY_POINT = os.path.dirname(os.path.dirname(__file__))
TEMPLATES_PATH = ENTRY_POINT + '/src/xml/templates/'
XML_DATA_PATH = ENTRY_POINT + '/src/xml/data/'


NAMESPACES = {
        'msg': 'http://www.1c.ru/SSL/Exchange/Message',
        'xs': 'http://www.w3.org/2001/XMLSchema',
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'bd': 'http://v8.1c.ru/edi/edi_stnd/EnterpriseData/1.8'
}
