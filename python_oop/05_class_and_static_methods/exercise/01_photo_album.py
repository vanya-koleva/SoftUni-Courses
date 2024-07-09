from math import ceil
from typing import List


class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE: int = 4
    DASHES_COUNT: int = 11
    DASHES: str = "-"

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.MAX_PHOTOS_PER_PAGE))

    def add_photo(self, label: str) -> str:
        for page in range(self.pages):
            if len(self.photos[page]) < self.MAX_PHOTOS_PER_PAGE:
                slot = len(self.photos[page]) + 1
                self.photos[page].append(label)

                return f"{label} photo added successfully on page {page + 1} slot {slot}"

        return "No more free slots"

    def display(self) -> str:
        result = [self.DASHES * self.DASHES_COUNT]
        for page in self.photos:
            result.append(("[] " * len(page)).strip())
            result.append(self.DASHES * self.DASHES_COUNT)

        return "\n".join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
