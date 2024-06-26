# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит
# интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#    - Тип объекта.
#    - Атрибуты объекта.
#    - Методы объекта.
#    - Модуль, к которому объект принадлежит.
#    - Другие интересные свойства объекта, учитывая его тип (по желанию).

# Пример работы:
# number_info = introspection_info(42)
# print(number_info)
# import inspect
# print(type(5))
# print(type([]))
# print(type({}))
#
from pprint import pprint

obj = 42
print(dir(obj))
print(type(obj))
obj_string = 'Hello'
obj_list = [obj, obj_string]
print(list(obj_list))
def introspection_info(self, obj):
    self.obj = 13

introspection_info.obj = 'abc'
print(callable(introspection_info))
print(dir(introspection_info))
print(hasattr(introspection_info, 'obj'))

