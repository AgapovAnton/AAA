import json


class ColorizeMixin():
    def __repr__(self, color_code: int):
        return f'\033[1;{color_code};40m'


class JsonToObject():
    def get_attr(self, key: str):
        """ getter для динамически создаваемых аттрибутов """
        def func(obj=self):
            return obj.__dict__['_' + key]
        return func

    def set_attr(self, key: str):
        """ setter для динамически создаваемых аттрибутов """
        def func(obj=self, value=None):
            obj.__dict__['_' + key] = value
        return func

    def __init__(self, json_: dict):
        """ конструктор класса создает аттрибуты из элементов json,
        если элемент является словарем, то вызываем JsonToObject к
        найденому словарю
        """
        for key, item in json_.items():
            setattr(self.__class__, key,
                    property(self.get_attr(key),
                             self.set_attr(key)))
            if type(item) == dict:
                self.__setattr__('_' + key, JsonToObject(item))
            else:
                self.__setattr__('_' + key, item)

            if key == 'price' and item < 0:
                print('ValueError(must be >= 0)')


class Advert(ColorizeMixin, JsonToObject):
    repr_color_code = 33        # yellow
    repr_color_code_black = 30  # black

    def __init__(self, json_: dict):
        super().__init__(json_)

    @property
    def price(self):
        if hasattr(self, '_price'):
            return self._price
        else:
            self._price = 0
            return self._price

    @price.setter
    def price(self, value: int):
        self._price = value or 0

    def __repr__(self):
        res = super().__repr__(self.repr_color_code) + \
              f'{self.title} | {self.price} p' + \
              super().__repr__(self.repr_color_code_black)
        return res


lesson_str1 = '{"title":"python"}'

lesson1 = json.loads(lesson_str1)
lesson_ad1 = Advert(lesson1)
print(lesson_ad1.price)
# 0

lesson_str2 = """{"title":"python",
                 "price":5,
                 "location":{"address":"Москва, Лесная",
                             "metro_stations":["Белорусская"]}}"""

lesson2 = json.loads(lesson_str2)
lesson_ad2 = Advert(lesson2)
print(lesson_ad2.location.address)
# Москва, Лесная

lesson_str3 = """{"title":"python",
                 "price":-5,
                 "location":{"address":"Москва, Лесная",
                             "metro_stations":["Белорусская"]}}"""

lesson3 = json.loads(lesson_str3)
lesson_ad3 = Advert(lesson3)
# ValueError(must be >= 0)

iphone_str = '{"title":"iPhone X", "price":100}'

iphone = json.loads(iphone_str)
iphone_ad = Advert(iphone)
print(iphone_ad)
# iPhone X | 100 p

corgi_str = """{"title":"Вельш-корги",
                "price":1000,
                "class":"dogs",
                "location":{"address":"сельское полесение Ельдигинское"}}"""
corgi_json = json.loads(corgi_str)
corgi = Advert(corgi_json)

print(corgi)
corgi._class
