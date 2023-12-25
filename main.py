class DynamicNameMeta(type):
    def __new__(cls, name, bases, dct):
        dynamic_name = dct.get('dynamic_name', 'DefaultName')
        name = f'Dynamic_{dynamic_name}_Class'
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=DynamicNameMeta):
    dynamic_name = 'Special'


obj = MyClass()
print(obj.__class__.__name__)
