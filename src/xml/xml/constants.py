body_path = 'bd:Body/bd:Документ.ПоступлениеТоваровУслуг/'

ACCOUNTS_PATHS = {
    'acc_id': [
        body_path + ('bd:КлючевыеСвойства/bd:Контрагент/'
                     'bd:Ссылка'),
        body_path + ('bd:ДанныеВзаиморасчетов/bd:Договор/bd:Контрагент/'
                     'bd:Ссылка'),
        ],
    'name': [
        body_path + ('bd:КлючевыеСвойства/bd:Контрагент/'
                     'bd:Наименование'),
        body_path + ('bd:ДанныеВзаиморасчетов/bd:Договор/bd:Контрагент/'
                     'bd:Наименование')
        ],
    'fullname': [
        body_path + ('bd:КлючевыеСвойства/bd:Контрагент/'
                     'bd:НаименованиеПолное'),
        body_path + ('bd:ДанныеВзаиморасчетов/bd:Договор/bd:Контрагент/'
                     'bd:НаименованиеПолное')
    ],
    'stock_id': [
        body_path + 'bd:Склад/bd:Ссылка'
    ],
    'stock_name': [
        body_path + 'bd:Склад/bd:Наименование',
        ],
    'contract': [
        body_path + ('bd:ДанныеВзаиморасчетов/bd:Договор/'
                     'bd:Ссылка')
    ]
}

# значение False - поле не будет заполняться в шаблоне
NAMES_MAP = {
        'id': body_path + 'bd:КлючевыеСвойства/bd:Ссылка',
        'amount': body_path + 'bd:Товары/bd:Строка/bd:Количество',
        'account': ACCOUNTS_PATHS,
        'currency': False,
        'created_date': body_path + 'bd:КлючевыеСвойства/bd:Дата',
        'local_currency': body_path + 'bd:Товары/bd:Строка/bd:Сумма',
        'rate': body_path + 'bd:Товары/bd:Строка/bd:Цена',
        'doc_number': body_path + 'bd:КлючевыеСвойства/bd:Номер',
        'comment': body_path + 'bd:Комментарий'
    }

NAMESPACES = {
        'msg': 'http://www.1c.ru/SSL/Exchange/Message',
        'xs': 'http://www.w3.org/2001/XMLSchema',
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'bd': 'http://v8.1c.ru/edi/edi_stnd/EnterpriseData/1.8'
}
