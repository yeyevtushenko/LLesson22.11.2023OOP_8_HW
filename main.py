class MetaClass(type):
    def __new__(cls, name, bases, dct):
        if 'some_method' in dct:
            original_method = dct['some_method']
            def modified_method(self, *args, **kwargs):
                print(f"Додаткова логіка перед викликом {name}.some_method")
                result = original_method(self, *args, **kwargs)
                print(f"Додаткова логіка після виклику {name}.some_method")
                return result
            dct['some_method'] = modified_method

        return super().__new__(cls, name, bases, dct)


class MyBaseClass(metaclass=MetaClass):
    def some_method(self):
        print("Оригінальний метод MyBaseClass.some_method")


obj = MyBaseClass()
obj.some_method()
