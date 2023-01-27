class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages


    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        super().__str__()
        self._duration = duration

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, new_dn: int) -> None:
        if not isinstance(new_dn, int):
            raise TypeError("длительность должна быть типа int")
        if new_dn <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self._duration = new_dn

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность: {self.duration} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

if __name__ == "__main__":
   pbook = PaperBook("Преступление и наказание", "Ф.М. Достоевский", 480)
   print(pbook.__str__())
   print(pbook.__repr__())
   audbook = AudioBook("Преступление и наказание", "Ф.М. Достоевский", 8)
   print(audbook.__str__())
   print(audbook.__repr__())
