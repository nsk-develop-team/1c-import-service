template_path = 'V8Exch:Data/v8:DocumentObject.ПоступлениеТоваровУслуг/'

ACCOUNTS_MAP = {
    'ILONMASK': {
        template_path + 'v8:Склад': '5f2c9987-c31e-11ec-80df-b42e9965e88e',
        template_path + 'v8:Контрагент': (
            '5f2c9988-c31e-11ec-80df-b42e9965e88e'
        ),
        template_path + 'v8:Организация': (
            '6c17169d-8810-11eb-80cc-b42e9965e88e'
        )
    },
    'CAESAR': {
        'v8:Склад': '5f2c9987-c31e-11ec-80df-b42e9965e88e',
        'v8:Контрагент': '5f2c9988-c31e-11ec-80df-b42e9965e88e',
        'v8:Организация': '6c17169d-8810-11eb-80cc-b42e9965e88e'
    }
}

NAMES_MAP = {
        'amount': template_path + 'v8:Товары/v8:Количество',
        'account': ACCOUNTS_MAP,
        'created_date': template_path + 'v8:Date',
        'local_currency': template_path + 'v8:Товары/v8:Сумма',
        'rate': template_path + 'v8:Товары/v8:Цена'
    }

NAMESPACES = {
        'V8Exch': 'http://www.1c.ru/V8/1CV8DtUD/',
        'v8': 'http://v8.1c.ru/8.1/data/enterprise/current-config'
}
