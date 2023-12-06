from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    VALID_MUSICIANS = {"Guitarist": Guitarist,
                       'Drummer': Drummer,
                       'Singer': Singer}

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError('Invalid musician type!')
        if any([m for m in self.musicians if m.name == name]):
            raise Exception(f'{name} is already a musician!')
        musician = self.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(musician)
        return f'{name} is now a {musician_type}.'

    def create_band(self, name: str):
        if any([b for b in self.bands if b.name == name]):
            raise Exception(f'{name} band is already created!')
        band = Band(name)
        self.bands.append(band)
        return f'{name} was created.'

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        try:
            concert = [c for c in self.concerts if c.place == place][0]
            raise Exception(f'{place} is already registered for {concert.genre} concert!')
        except IndexError:
            concert_to_add = Concert(genre, audience, ticket_price, expenses, place)
            self.concerts.append(concert_to_add)
            return f'{genre} concert in {place} was added.'

    def add_musician_to_band(self, musician_name: str, band_name: str):
        try:
            searched_musician = [m for m in self.musicians if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(searched_musician)
        band.increment_musician_type(searched_musician)
        return f'{musician_name} was added to {band_name}.'

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        try:
            band = [b for b in self.bands if b.name == band_name][0]
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        try:
            searched_member = [m for m in band.members if m.name == musician_name][0]
        except IndexError:
            raise Exception(f'{musician_name} isn\'t a member of {band_name}!')
        band.members.remove(searched_member)
        return f'{musician_name} was removed from {band_name}.'

    def start_concert(self, concert_place: str, band_name: str):

        band = [b for b in self.bands if b.name == band_name][0]

        if band.GUITARISTS == 0 or band.DRUMMERS == 0 or band.SINGERS == 0:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = [c for c in self.concerts if c.place == concert_place][0]
        for m in band.members:
            if any([skill not in m.skills for skill in concert._get_type()[m.__class__.__name__]]):
                raise Exception(f'The {band_name} band is not ready to play at the concert!')

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f'{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}.'

