import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args, **kwargs):
        print(args)
        if args in cache_value:
            return cache_value[args]

        result = func(*args, **kwargs)
        cache_value[args] = result

        print(cache_value)
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(2)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(2, 4))