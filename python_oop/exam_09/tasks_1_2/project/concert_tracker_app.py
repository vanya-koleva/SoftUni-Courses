from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
    CONCERTS = {
        "Rock": {
            "Drummer": {"play the drums with drumsticks"},
            "Singer": {"sing high pitch notes"},
            "Guitarist": {"play rock"},
        },
        "Metal": {
            "Drummer": {"play the drums with drumsticks"},
            "Singer": {"sing low pitch notes"},
            "Guitarist": {"play metal"},
        },
        "Jazz": {
            "Drummer": {"play the drums with drum brushes"},
            "Singer": {"sing high pitch notes", "sing low pitch notes"},
            "Guitarist": {"play jazz"},
        },
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")

        self.check_existence(name, self.musicians, f"{name} is already a musician!")

        musician = self.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        self.check_existence(name, self.bands, f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(
        self,
        genre: str,
        audience: int,
        ticket_price: float,
        expenses: float,
        place: str,
    ):
        existing_concert = next((x for x in self.concerts if x.place == place), None)

        if existing_concert is not None:
            raise Exception(
                f"{place} is already registered for {existing_concert.genre} concert!"
            )

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.get_existing_obj(
            musician_name, self.musicians, f"{musician_name} isn't a musician!"
        )
        band = self.get_existing_obj(
            band_name, self.bands, f"{band_name} isn't a band!"
        )

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.get_existing_obj(
            band_name, self.bands, f"{band_name} isn't a band!"
        )
        musician = self.get_existing_obj(
            musician_name,
            band.members,
            f"{musician_name} isn't a member of {band_name}!",
        )

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        concert = [x for x in self.concerts if x.place == concert_place][0]
        band = self.find_obj_by_name(band_name, self.bands)

        for musician_type in ["Drummer", "Singer", "Guitarist"]:
            if not any(
                filter(lambda x: x.__class__.__name__ == musician_type, band.members)
            ):
                raise Exception(
                    f"{band_name} can't start the concert because it doesn't have enough members!"
                )

        for musician in band.members:
            required_skills = self.CONCERTS[concert.genre][musician.__class__.__name__]
            if not required_skills.issubset(set(musician.skills)):
                raise Exception(
                    f"The {band_name} band is not ready to play at the concert!"
                )

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    @staticmethod
    def find_obj_by_name(name: str, collection: list):
        return next((x for x in collection if x.name == name), None)

    def get_existing_obj(self, name, collection, error_message):
        obj = self.find_obj_by_name(name, collection)

        if obj is None:
            raise Exception(error_message)

        return obj

    def check_existence(self, name, collection, error_message):
        obj = self.find_obj_by_name(name, collection)

        if obj is not None:
            raise Exception(error_message)
