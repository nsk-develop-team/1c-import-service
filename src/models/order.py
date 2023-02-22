class Order:
    def __init__(self, obj):
        self.amount = '0.0'
        self.account = ''
        self.currency = ''
        self.created_date = ''
        self.local_currency = ''
        self.rate = '0.0'

        self.insert_obj(obj)

    def props(self):
        return [i for i in self.__dict__.keys() if i[:1] != '_']

    def insert_obj(self, obj):
        try:
            for key in self.props():
                # to extend the properties
                self.__setattr__(key, obj[key])
        except KeyError as e:
            raise ValueError(str(e) + ' key doesn\'t found')

    def get(self):
        # TODO: realize get method
        pass
