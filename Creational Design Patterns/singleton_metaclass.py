class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *arg, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*arg, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=MetaSingleton):
    def __init__(self):
        print(f'the memory location of object is {self}')

logger1 = Logger()
print(logger1)
logger2 = Logger()
print(logger2)