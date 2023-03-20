FILE_NAME = 'MoveGood.xml'
TEMPLATE_NAME = 'docMoveGood_ED_1_8.xml'
BODY_PATH = 'bd:Body'
ELEMENT_PATH = 'bd:Body/bd:Документ.ПеремещениеТоваров'

DICTIONARY = {
    'CESAR': {
        'stock_id': 'f8c70b63-fded-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN CESAR',
    },
    'JULIET': {
        'stock_id': 'ce0a3bfe-194c-11ed-80e2-b42e9965e88e',
        'stock_name': 'BIN Juliet',
    },
    'MAX': {
        'stock_id': '5f2c9987-c31e-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN MAX',
    },
    'TAN': {
        'stock_id': '4261e8c7-db48-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN TAN',
    },
    'VITANYA': {
        'stock_id': '2963d180-f24d-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN VITANYA ',
    },
    'SERIOUS': {
        'stock_id': 'c3393548-ca1f-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN SERIOUS',
    },
    'TOKOYA': {
        'stock_id': 'a7df94ea-ae47-11eb-80d8-b42e9965e88e',
        'stock_name': 'BIN Tok',
    },
    'VITOL': {
        'stock_id': 'c3393529-ca1f-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN VITOL',
    },
    'RRH': {
        'stock_id': '1d3ad6a1-c628-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN RRH',
    },
    'DEVA_MARIIA': {
        'stock_id': '7fca2481-c0c7-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN DEVA_MARIIA',
    },
    'KUN': {
        'stock_id': '11d420c2-c487-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN KUN',
    },
    'KASATKA': {
        'stock_id': 'd0969272-cbc3-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN KASATKA',
    },
    'TATAN': {
        'stock_id': '0e1427c7-b443-11ed-8c2c-00155d9b3aff',
        'stock_name': 'BIN TATAN',
    },
    'HBG': {
        'take_stock_id': '0dd41c48-e998-11ea-8128-0050569f2e9f',
        'take_stock_name': 'HBG',
    },
    'HBGS': {
        'take_stock_id': 'b7a16df6-eb97-11eb-80dd-b42e9965e88e',
        'take_stock_name': 'HBG S',
    },
}

MAPPING = {
    'id': 'bd:КлючевыеСвойства/bd:Ссылка',
    'amount': 'bd:Товары/bd:Строка/bd:Количество',
    'from_account': 'DICTIONARY',
    'to_account': 'DICTIONARY',
    'created_date': 'bd:КлючевыеСвойства/bd:Дата',
    'doc_number': 'bd:КлючевыеСвойства/bd:Номер',
}

DICTIONARY_MAPPING = {
    'stock_id': ['bd:СкладОтправитель/bd:Ссылка'],
    'take_stock_id': ['bd:СкладПолучатель/bd:Ссылка'],
    'stock_name': ['bd:СкладОтправитель/bd:Наименование'],
    'take_stock_name': ['bd:СкладПолучатель/bd:Наименование']
}