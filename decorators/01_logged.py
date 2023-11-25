from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'you called {func.__name__}{args}\nit returned {result}'
    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

# test zero second
import unittest

class LoggedTests(unittest.TestCase):
    def test_zero_second(self):
        @logged
        def sum_func(a, b):
            return a + b
        result = sum_func(1, 4)
        self.assertEqual(result, 'you called sum_func(1, 4)\nit returned 5')

if __name__ == '__main__':
    unittest.main()