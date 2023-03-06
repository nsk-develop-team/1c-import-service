body_path = 'bd:Body/v8:DocumentObject.ПоступлениеТоваровУслуг/'

ACCOUNTS_MAP = {
    'ILONMASK': {
        body_path + 'v8:Склад': '5f2c9987-c31e-11ec-80df-b42e9965e88e',
        body_path + 'v8:Контрагент': (
            '5f2c9988-c31e-11ec-80df-b42e9965e88e'
        ),
        body_path + 'v8:Организация': (
            '6c17169d-8810-11eb-80cc-b42e9965e88e'
        )
    },
    'CAESAR': {
        body_path + 'v8:Склад': '5f2c9987-c31e-11ec-80df-b42e9965e88e',
        body_path + 'v8:Контрагент': (
            '5f2c9988-c31e-11ec-80df-b42e9965e88e'
        ),
        body_path + 'v8:Организация': (
            '6c17169d-8810-11eb-80cc-b42e9965e88e'
        )
    },
}

NAMES_MAP = {
        'amount': body_path + 'v8:Товары/v8:Количество',
        'account': ACCOUNTS_MAP,
        'created_date': body_path + 'v8:Date',
        'local_currency': body_path + 'v8:Товары/v8:Сумма',
        'rate': body_path + 'v8:Товары/v8:Цена'
    }

NAMESPACES = {
        'msg': 'http://www.1c.ru/SSL/Exchange/Message',
        'v8': 'http://v8.1c.ru/8.1/data/enterprise/current-config',
        'xs': 'http://www.w3.org/2001/XMLSchema',
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'bd': 'http://v8.1c.ru/edi/edi_stnd/EnterpriseData/1.8'
}
