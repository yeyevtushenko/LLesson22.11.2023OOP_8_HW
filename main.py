class InitArgsMeta(type):
    def __init__(cls, name, bases, dct):
        original_init = cls.__init__ if '__init__' in dct else lambda self: None

        def new_init(self, *args, **kwargs):
            print(f"Checking and processing arguments in {cls.__name__}'s __init__")
            original_init(self, *args, **kwargs)
        cls.__init__ = new_init
        super().__init__(name, bases, dct)


class MyClass(metaclass=InitArgsMeta):
    def __init__(self, arg1, arg2):
        print(f"MyClass __init__ called with arguments: {arg1}, {arg2}")


obj = MyClass(10, 20)