# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union

class Bouquet:
    def __init__(self, flowers_quantity:int, flowers_sort:str):
        """

        :param flowers_quantity: количество цветов в букете
        :param flowers_sort: сорт цветов
        >>> bouquet1 = Bouquet(25, 'roses')
        """
        if not isinstance(flowers_quantity, int):
            raise TypeError("Количество цветов должно быть типа str")
        if flowers_quantity <= 0:
            raise ValueError("Количество цветов должно быть больше нуля")
        self.flowers_quantity = flowers_quantity
        self.flowers_sort = None
        self.init_flowers_sort(flowers_sort)

    def init_flowers_sort(self, flowers_sort:str):
        if not isinstance(flowers_sort, str):
            raise TypeError('Сорт цветов должен быть типа str')
        self.flowers_sort = flowers_sort

    def amount_of_flowers(self) -> bool:
        """
        Посчитать количество цветов в букете
        :return: количество цветов
        """
        ...

    def add_flowers(self):
        """
        Предположим, что мы хотим, чтобы в букете было только четное количество цветов.
        Тогда накладываем соответствующее условие:
        if bouquet1.flowers_quantity % 2 == 0:
            bouquet1.flowers_quantity += 11
        else:
            bouquet1.flowers_quantity += 10

        :return: итоговое количество цветов
        """
        ...

class Blouses:
    def __init__(self, blouse_color:str, design:str, price: Union[int, float]):
        if not isinstance(blouse_color, str):
            raise TypeError('Цвет блузки должен быть типа str')

        if not isinstance(design, str):
            raise TypeError('Дизайн должен быть типа str')

        if not isinstance(price, Union[int, float]):
            raise TypeError("Цена должна быть типа int или float")
        if price <= 0:
            raise ValueError('Цена блузки должна быть положительной')

    def change_price(self):
        """
        Функция меняет цену блузки
        :param self: price
        :return: новая цена блузки
        """
        ...

    def printing_design(self):
        """
        :param self: design
        :return: название принта блузки
        """
        ...

class Student:
    def __init__(self, student_name: str, student_grades: list[int], student_class: str):
        """
          :param student_name: имя ученика
          :param student_grades: список с оценками ученика
          :param student_class: класс, в котором обучается студент
          >>> student1 = Student("Александр", [3, 4, 5], "11Б")
          """
        if not isinstance(student_name, str):
            raise TypeError('Имя ученика должно быть типа str')
        if not isinstance(student_class, str):
            raise TypeError

        if not isinstance(student_grades, list):
            raise TypeError('Оценки должны быть типа list, содержащим int')
        if not all([type(item) is int for item in student_grades]):
            raise ValueError('Оценки должны быть типа int')
        if not all([1 <= item <= 5 for item in student_grades]):
            raise ValueError('Оценки должны быть от 1 до 5 баллов')

        self.student_name = student_name
        self.student_grades = student_grades
        self.student_class = student_class


    def add_grades(self):
        """
        Функция добавляет оценки в список
        :return: список с оценками
        :raise ValueError: Если оценка не является int типом или если оценка не в промежутке [1;5]
        >>> student1 = Student("Александр", [3, 4, 5], "11Б")
        >>> student1 = Student("Александр", [3, 4, 5, 5], "11Б")

        """
        ...

    def change_class(self):
        """
                Функция меняет класс ученика
                :return: новый класс
                :raise TypeError: Если название класса не типа int
                >>> student1 = Student("Александр", [3, 4, 5], "11Б")
                >>> student1 = Student("Александр", [3, 4, 5], "11A")

                """
        ...

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
