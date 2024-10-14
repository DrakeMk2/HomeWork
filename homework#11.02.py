from inspect import getmodule
from pprint import pprint


def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': obj.__dict__,
        'methods': dir(obj),
        'module': getmodule(obj)
    }


class MyClass:
    def __init__(self):
        self.name = 'MyClass'
        self.value = 77


obj = MyClass()

number_info = introspection_info(obj)
pprint(number_info)
