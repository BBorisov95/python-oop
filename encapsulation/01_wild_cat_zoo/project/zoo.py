from typing import List
from project.animal import Animal
from project.cheetah import Cheetah
from project.lion import Lion
from project.tiger import Tiger
from project.worker import Worker

class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if len(self.animals) == self.__animal_capacity:
            return f'Not enough space for animal'
        if price > self.__budget:
            return f'Not enough budget'
        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) == self.__workers_capacity:
            return 'Not enough space for worker'
        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name: str) -> str:
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self) -> str:
        total_salaries_cost = sum([worker.salary for worker in self.workers])
        if self.__budget >= total_salaries_cost:
            self.__budget -= total_salaries_cost
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self) -> str:
        total_cost_for_animals = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= total_cost_for_animals:
            self.__budget -= total_cost_for_animals
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self):
        return self.__get_statuses(self.animals, ['Lion', 'Tiger', 'Cheetah'])

    def workers_status(self):
        return self.__get_statuses(self.workers, ['Keeper', 'Caretaker', 'Vet'])

    def __get_statuses(self, category: List, list_of_instances) -> str:
        result_dict = {arg: [] for arg in list_of_instances}
        for el in category:
            result_dict[el.__class__.__name__].append(repr(el))
        result = [f'You have {len(category)} {str(category[0].__class__.__base__.__name__).lower()}s']
        for k,v in result_dict.items():
            result.append(f'----- {len(v)} {k}s:')
            result.extend(v)
        return '\n'.join(result)
