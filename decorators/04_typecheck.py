def type_check(type_to_check):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, type_to_check):
                    return 'Bad Type'
            result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator

@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))

@type_check(str)
def first_letter(word):
    return word[0]

@type_check(float)
def float_num(float_num):
    return float_num

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
print(float_num(3.5))