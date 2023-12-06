from project.booths.booth import Booth


class PrivateBooth (Booth):
    TYPE = 'PrivateBooth '

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * 3.5

