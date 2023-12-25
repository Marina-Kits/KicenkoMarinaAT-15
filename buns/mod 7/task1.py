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

@validate_args
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(3))
print(fibonacci())
print(fibonacci(3,5))
print(fibonacci(-3))
print(fibonacci("3"))
