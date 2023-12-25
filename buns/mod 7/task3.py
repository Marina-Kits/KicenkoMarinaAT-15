import time

def validate_args(function):
    def wrapper_function(*arguments, **kwargs):
        if len(arguments)>1:
            return "Too many arguments"
        if len(arguments)<1:
            return "Not enough arguments"
        argument=arguments[0]
        if not isinstance(argument, int):
            return "Wrong types"
        if argument<0:
            return "Negative argument"
        return function(*arguments, **kwargs)
    return wrapper_function

def memoize(function):
    function_cache={}
    def wrapper_function(*arguments):
        if arguments not in function_cache:
            function_cache[arguments]=function(*arguments)
        return function_cache[arguments]
    return wrapper_function

def timer(function):
    def wrapper_function(*arguments, **kwargs):
        start=time.time()
        res=function(*arguments, **kwargs)
        end = time.time()
        print(f"{function.__name__} выполнялась в течение {end-start} секунд")
        return res
    return wrapper_function

@validate_args
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

@timer
def function_test(function,n):
    return function(n)

print("Без memoize:")
print(function_test(fibonacci,34))
fibonacci=memoize(fibonacci)
print("\nС memoize:")
print(function_test(fibonacci,34))