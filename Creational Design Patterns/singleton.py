class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
        # Super() will refer to the base class

    def __init__(self):
        print(f'memory location of object is {self}')


s1 = Singleton()
s2 = Singleton()
