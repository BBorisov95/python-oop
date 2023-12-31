from typing import List


class Person:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        return self.__new_person(self.name, other.surname)

    @classmethod
    def __new_person(cls, name, surname):
        return cls(name, surname)


class Group:

    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people: List[Person] = people

    def __repr__(self):
        return f'Group {self.name} with members {", ".join([p.__repr__() for p in self.people])}'

    def __iter__(self):
        for index, _person in enumerate(self.people):
            yield f'Person {index}: {_person.__repr__()}'

    def __getitem__(self, index):
        return f'Person {index}: {self.people[index].__repr__()}'

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return self.__new_group(f"{self.name} {other.name}", self.people + other.people)

    @classmethod
    def __new_group(cls, name, people):
        return cls(name, people)


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
