def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<b>{result}</b>'
    return wrapper


def make_italic(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<i>{result}</i>'
    return wrapper


def make_underline(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<u>{result}</u>'
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))

import unittest


class BoldItalicUnderlineTests(unittest.TestCase):
    def test_make_bold(self):
        @make_bold
        def func():
            return "pesho"

        res = func()
        self.assertEqual(res, "<b>pesho</b>")

    def test_make_italic(self):
        @make_italic
        def func(name):
            return f"Hey, {name}"

        res = func("pesho")
        self.assertEqual(res, "<i>Hey, pesho</i>")

    def test_make_underline(self):
        @make_underline
        def func(first_name, last_name):
            return f"{first_name} {last_name}"

        res = func("pesho", "peshov")
        self.assertEqual(res, "<u>pesho peshov</u>")

    def test(self):
        @make_bold
        @make_underline
        @make_italic
        def func():
            return "pesho"

        res = func()
        self.assertEqual(res, "<b><u><i>pesho</i></u></b>")


if __name__ == "__main__":
    unittest.main()
