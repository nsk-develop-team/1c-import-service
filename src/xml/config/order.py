FILE_NAME = 'GoodAndService.xml'
TEMPLATE_NAME = 'docGoodsAndServices_ED_1_8.xml'
BODY_PATH = 'bd:Body'
ELEMENT_PATH = 'bd:Body/bd:Документ.ПоступлениеТоваровУслуг'

DICTIONARY = {
    'CESAR': {
        'acc_id': 'f8c70b62-fded-11ec-80df-b42e9965e88e',
        'name': 'CESAR',
        'fullname': 'CESAR',
        'stock_id': 'f8c70b63-fded-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN CESAR',
        'contract': 'f8c70b64-fded-11ec-80df-b42e9965e88e'
    },
    'JULIET': {
        'acc_id': 'bb93f9ee-22c6-11ed-80e2-b42e9965e88e',
        'name': 'JULIET',
        'fullname': 'JULIET',
        'stock_id': 'ce0a3bfe-194c-11ed-80e2-b42e9965e88e',
        'stock_name': 'BIN Juliet',
        'contract': 'bb93f9ef-22c6-11ed-80e2-b42e9965e88e'
    },
    'MAX': {
        'acc_id': '5f2c9988-c31e-11ec-80df-b42e9965e88e',
        'name': 'MAX',
        'fullname': 'MAX',
        'stock_id': '5f2c9987-c31e-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN MAX',
        'contract': '5f2c9989-c31e-11ec-80df-b42e9965e88e'
    },
    'TAN': {
        'acc_id': '25b52b68-dc03-11ec-80df-b42e9965e88e',
        'name': 'TAN',
        'fullname': 'TAN',
        'stock_id': '4261e8c7-db48-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN TAN',
        'contract': '25b52b69-dc03-11ec-80df-b42e9965e88e'
    },
    'VITANYA': {
        'acc_id': '74f2315e-f795-11ec-80df-b42e9965e88e',
        'name': 'VITANYA',
        'fullname': 'VITANYA',
        'stock_id': '2963d180-f24d-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN VITANYA ',
        'contract': '74f2315f-f795-11ec-80df-b42e9965e88e'
    },
    'SERIOUS': {
        'acc_id': 'c3393546-ca1f-11ec-80df-b42e9965e88e',
        'name': 'SERIOUS',
        'fullname': 'SERIOUS',
        'stock_id': 'c3393548-ca1f-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN SERIOUS',
        'contract': 'c3393547-ca1f-11ec-80df-b42e9965e88e'
    },
    'tokoya': {
        'acc_id': '4fe50fe2-c094-11ec-80df-b42e9965e88e',
        'name': 'tokoya',
        'fullname': 'tokoya',
        'stock_id': 'a7df94ea-ae47-11eb-80d8-b42e9965e88e',
        'stock_name': 'BIN Tok',
        'contract': '2ccb2498-bc35-11ed-8c2c-00155d9b3aff'
    },
    'VITOL': {
        'acc_id': 'c3393527-ca1f-11ec-80df-b42e9965e88e',
        'name': 'VITOL',
        'fullname': 'VITOL',
        'stock_id': 'c3393529-ca1f-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN VITOL',
        'contract': 'c3393528-ca1f-11ec-80df-b42e9965e88e'
    },
    'RRH': {
        'acc_id': '1d3ad6ae-c628-11ec-80df-b42e9965e88e',
        'name': 'RRH',
        'fullname': 'RRH',
        'stock_id': '1d3ad6a1-c628-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN RRH',
        'contract': '1d3ad6af-c628-11ec-80df-b42e9965e88e'
    },
    'DEVA_MARIIA': {
        'acc_id': '7fca248e-c0c7-11ec-80df-b42e9965e88e',
        'name': 'DEVA_MARIIA',
        'fullname': 'DEVA_MARIIA',
        'stock_id': '7fca2481-c0c7-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN DEVA_MARIIA',
        'contract': '7fca248f-c0c7-11ec-80df-b42e9965e88e'
    },
    'KUN': {
        'acc_id': '11d420c3-c487-11ec-80df-b42e9965e88e',
        'name': 'KUN',
        'fullname': 'KUN',
        'stock_id': '11d420c2-c487-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN KUN',
        'contract': '11d420c4-c487-11ec-80df-b42e9965e88e'
    },
    'KASATKA': {
        'acc_id': 'd0969271-cbc3-11ec-80df-b42e9965e88e',
        'name': 'KASATKA',
        'fullname': 'KASATKA',
        'stock_id': 'd0969272-cbc3-11ec-80df-b42e9965e88e',
        'stock_name': 'BIN KASATKA',
        'contract': 'd0969273-cbc3-11ec-80df-b42e9965e88e'
    },
    'TATAN': {
        'acc_id': '0e1427c5-b443-11ed-8c2c-00155d9b3aff',
        'name': 'TATAN',
        'fullname': 'TATAN',
        'stock_id': '0e1427c7-b443-11ed-8c2c-00155d9b3aff',
        'stock_name': 'BIN TATAN',
        'contract': '0e1427c6-b443-11ed-8c2c-00155d9b3aff'
    },
}

DICTIONARY_MAPPING = {
    'acc_id': [
        'bd:КлючевыеСвойства/bd:Контрагент/bd:Ссылка',
        'bd:ДанныеВзаиморасчетов/bd:Договор/bd:Контрагент/bd:Ссылка'
    ],
    'name': [
        'bd:КлючевыеСвойства/bd:Контрагент/bd:Наименование',
        'bd:ДанныеВзаиморасчетов/bd:Договор/bd:Контрагент/bd:Наименование'
    ],
    'fullname': [
        'bd:КлючевыеСвойства/bd:Контрагент/bd:НаименованиеПолное',
        'bd:ДанныеВзаиморасчетов/bd:Договор/bd:Контрагент/bd:НаименованиеПолное'
    ],
    'stock_id': ['bd:Склад/bd:Ссылка'],
    'stock_name': ['bd:Склад/bd:Наименование'],
    'contract': ['bd:ДанныеВзаиморасчетов/bd:Договор/bd:Ссылка']
}

MAPPING = {
    'id': 'bd:КлючевыеСвойства/bd:Ссылка',
    'amount': 'bd:Товары/bd:Строка/bd:Количество',
    'account': 'DICTIONARY',
    'currency': False,
    'created_date': 'bd:КлючевыеСвойства/bd:Дата',
    'local_currency': ('bd:Товары/bd:Строка/bd:Сумма', 'bd:Сумма'),
    'rate': 'bd:Товары/bd:Строка/bd:Цена',
    'doc_number': 'bd:КлючевыеСвойства/bd:Номер',
    'comment': 'bd:Комментарий'
}