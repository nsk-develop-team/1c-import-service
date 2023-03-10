import os

MAX_SIZE = 2097152  # 2 MB = 2097152 byte

TRY_COUNTER = 10

DATAFILE_NAME = 'datafile.zip'

XML_PATH = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = XML_PATH + '/data/'
DATAFILE_NAME = 'datafile'
DATAFILE_PATH = DATA_PATH + DATAFILE_NAME
DATAFILE_XML_PATH = DATAFILE_PATH + '.xml'
DATAFILE_ZIP_PATH = DATAFILE_PATH + '.zip'
DOC_PATH = XML_PATH + '/templates/docPostuplenieTovarovIUslug_ED1_8.xml'

NAMESPACES = {
        'msg': 'http://www.1c.ru/SSL/Exchange/Message',
        'xs': 'http://www.w3.org/2001/XMLSchema',
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'bd': 'http://v8.1c.ru/edi/edi_stnd/EnterpriseData/1.8'
}
