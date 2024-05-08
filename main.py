from functools import wraps
import asyncio


class Cache:
    def __init__(self):
        self.data = {}

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            name = func.__name__
            if name in self.data:
                return self.data[func.__name__]
            else:
                result = func(*args, **kwargs)
                self.data[func.__name__] = result
                return result
        return wrapper

    def invalidate(self, func):
        if func.__name__ in self.data:
            del self.data[func.__name__]


cache = Cache()


@cache
def slow_function(arg):
    return arg


class MyClass:
    @cache
    def method(self, arg):
        return arg


@cache
async def async_func(arg):
    await asyncio.sleep(1)
    return arg