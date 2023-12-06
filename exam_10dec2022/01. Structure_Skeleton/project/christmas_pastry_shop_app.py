from typing import List
from project.booths.booth import Booth
from project.delicacies.delicacy import Delicacy
from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:

    VALID_DELICACIES = {'Stolen': Stolen,
                        'Gingerbread': Gingerbread}

    VALID_BOOTHS = {'Open Booth': OpenBooth,
                    'Private Booth': PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if any([d for d in self.delicacies if d.name == name]):
            raise Exception(f'{name} already exists!')
        if type_delicacy not in self.VALID_DELICACIES:
            raise Exception(f'{type_delicacy} is not on our delicacy menu!')
        delicacy = self.VALID_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f'Added delicacy {name} - {type_delicacy} to the pastry shop.'

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if any([b for b in self.booths if b.booth_number == booth_number]):
            raise Exception(f'Booth number {booth_number} already exists!')
        if type_booth not in self.VALID_BOOTHS:
            raise Exception(f'{type_booth} is not a valid booth!')
        booth = self.VALID_BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f'Added booth number {booth_number} in the pastry shop.'

    def reserve_booth(self, number_of_people: int):
        try:
            booth = [b for b in self.booths if not b.is_reserved
                          and b.capacity >= number_of_people][0]
        except IndexError:
            raise Exception(f'No available booth for {number_of_people} people!')
        #booth.is_reserved = True
        booth.reserve(number_of_people)
        return f'Booth {booth.booth_number} has been reserved for {number_of_people} people.'

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = next((b for b in self.booths if b.booth_number == booth_number), None)
        if booth is None:
            raise Exception(f'Could not find booth {booth_number}!')
        delicacy = next((d for d in self.delicacies if d.name == delicacy_name), None)
        if delicacy is None:
            raise Exception(f'No {delicacy_name} in the pastry shop!')
        booth.delicacy_orders.append(delicacy)
        return f'Booth {booth_number} ordered {delicacy_name}.'

    def leave_booth(self, booth_number: int):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        cost_for_ordered_delicacies = sum([d.price for d in booth.delicacy_orders])
        bill = booth.price_for_reservation + cost_for_ordered_delicacies
        self.income += bill
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0
        return f'Booth {booth_number}:\nBill: {bill:.2f}lv.'

    def get_income(self):
        return f'Income: {self.income:.2f}lv.'





