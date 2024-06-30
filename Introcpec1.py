import inspect
from pprint import pprint


def introspection_info(obj):
    obj_type = type(obj)
    attributes = dir(obj)
    methods = [method for method in attributes if callable(getattr(obj, method))]
    module = obj
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module}
    return info


number_info = introspection_info(42)
print(number_info)
string_info = introspection_info('Hello')
print(string_info)
list_info = introspection_info([5, 10, 5.0, 'Hello'])
print(list_info)
