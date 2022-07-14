from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.create_photos()

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for idx, page in enumerate(self.photos):
            if len(page) < self.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {idx + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        delimiter = '-' * 11
        result = delimiter
        for page in self.photos:
            page_info = ' '.join(['[]' for photo in page])
            result += '\n' + page_info + "\n" + delimiter
        return result.strip()

    def create_photos(self):
        result = []
        for _ in range(self.pages):
            result.append([] * self.PHOTOS_PER_PAGE)
        return result
    
    
album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
