import math


class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def xy(self):
        return (self.__x, self.__y)


class Figure:

    def __init__(self, tr):
        self.__area = None
        self.a, self.b, self.c = self.data_input()
        self.tr = tr
        self.area = self._update_area()

    def _update_area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def data_input(self):
        flag = False
        a, b, c = 0, 0, 0
        while not flag:
            a = float(
                input(f"Введи стороны {self.tr} треугольника\n а = "))
            b = float(input(" b = "))
            c = float(input(" c = "))
            flag = self.input_validation(a, b, c)
        return a, b, c

    @property
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def input_validation(a: float, b: float, c: float) -> bool:
        if a + b < c or b + c < a or a + c < b:
            return False
        return True

    def __le__(self, second):
        return self.area <= second.area

    def __ge__(self, second):
        return self.area >= second.area

    def __lt__(self, second):
        return self.area < second.area

    def __eq__(self, second):
        return self.area == second.area

    def __ne__(self, second):
        return self.area != second.area

    def __gt__(self, second):
        return self.area > second.area


class Triangle(Figure):

    def __init__(self, points):
        super().__init__(self, points)

    def _update_area(self):
        print("Area update")
        return super()._update_area()


# class Fourangle(Figure):

#     def _update_area(self):
#         print("Fourangle::update_area")
#         return super()._update_area()


print(
    "Triangle with max area",
    max(Triangle(i) for i in range(N)).tr
)
