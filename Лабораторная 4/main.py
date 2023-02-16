if __name__ == "__main__":
    #Сравниваем наушники двух производителей
    class Headphones:
        def __init__(self, brand: str, manufacturer: str):
            self.brand = brand
            self.manufacturer = manufacturer

        def construction(self):
            print("Накладные наушники")

        def control(self):
            print("Способ управления: Сенсорный")

        def __str__(self):
            return f"Наушники: {self.brand}. Производитель {self.manufacturer}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.brand!r}, manufacturer={self.manufacturer!r})"

    class Airpods(Headphones):
        def construction(self):
            print("Внутриканальные наушники")

    class Jbl(Headphones):
        def control(self):
            print("Способ управления: кнопочный")

    pass

ap = Airpods("Apple", "Китай")
print(ap.__str__())
print(ap.__repr__())
print(ap.construction())
print(ap.control())

jbl = Jbl("JBL", "Китай")
print(jbl.__str__())
print(jbl.__repr__())
print(jbl.construction())
print(jbl.control())
