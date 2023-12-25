def memoize(function):
    function_cache={}
    def wrapper_function(*arguments):
        if arguments not in function_cache:
            function_cache[arguments]=function(*arguments)
        return function_cache[arguments]
    return wrapper_function

@memoize
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(8))