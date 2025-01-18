def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    obj_module = getattr(obj, "__module__", "<unknown>")

    extra_info = {}
    if isinstance(obj, (int, float, complex, str, list, dict, set, tuple)):
        extra_info['length'] = len(obj) if hasattr(obj, '__len__') else "N/A"
        extra_info['is_empty'] = len(obj) == 0 if hasattr(obj, '__len__') else "N/A"

    return {
        "type": obj_type,
        "attributes": attributes,
        "methods": methods,
        "module": obj_module,
        "extra_info": extra_info,
    }


# Пример использования функции с числами
number_info = introspection_info(42)
print(number_info)


# Пример использования функции с пользовательским классом
class MyClass:
    def __init__(self, value):
        self.value = value

    def greet(self):
        return f"Hello, {self.value}!"


my_obj = MyClass("world")
class_info = introspection_info(my_obj)
print(class_info)
