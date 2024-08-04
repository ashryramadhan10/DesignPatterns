import inspect
from typing import Callable, Type

def override(interface_class: Type) -> Callable:
    def decorator(method: Callable) -> Callable:
        method_name = method.__name__
        for cls in inspect.getmro(interface_class):
            if cls is not object and method_name in cls.__dict__:
                return method
        raise TypeError(f"{method_name} does not override any method in {interface_class.__name__}")
    return decorator