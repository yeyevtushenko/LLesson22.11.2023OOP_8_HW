class MetaClass(type):
    def __new__(cls, name, bases, dct):
        # Додаємо логіку до методу "some_method"
        if 'some_method' in dct:
            original_method = dct['some_method']
            def modified_method(self, *args, **kwargs):
                # Додаткова логіка
                print(f"Додаткова логіка перед викликом {name}.some_method")
                # Виклик оригінального методу
                result = original_method(self, *args, **kwargs)
                # Додаткова логіка після виклику
                print(f"Додаткова логіка після виклику {name}.some_method")
                return result
            dct['some_method'] = modified_method

        return super().__new__(cls, name, bases, dct)

# Використання метакласу для створення класу
class MyBaseClass(metaclass=MetaClass):
    def some_method(self):
        print("Оригінальний метод MyBaseClass.some_method")

# Створення екземпляру класу і виклик методу
obj = MyBaseClass()
obj.some_method()
