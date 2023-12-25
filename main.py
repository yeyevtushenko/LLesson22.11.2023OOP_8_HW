class AutoAttributesMeta(type):
    def __new__(cls, name, bases, dct):
        dct['added_attribute'] = 'This attribute is automatically added'
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=AutoAttributesMeta):
    pass

obj = MyClass()
print(obj.added_attribute)
