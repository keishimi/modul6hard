class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled: bool = True):
        self.__color = color
        self.__sides = list(sides) if len(sides) == self.sides_count else [1] * self.sides_count
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        rgb = [r, g, b]
        rgb.sort()
        if rgb[0] < 0 or rgb[-1]>225:
            return False
        else:
            return True
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        set = []
        for i in new_sides:
            if i>0:
                set.append(i)
        if len(set) > 0 and len(new_sides) == len(self.__sides):
            return True
        else:
            return False


    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return self.__len__*(2/3.14)

    def get_square(self):
        return 3.14159 * self.__radius**2

class Triangle(Figure):
    sides_count = 3

    def __height(self):
        s = self.__len__ / 2
        h = (2**(s(s-self.__sides[0])(s-self.__sides[1])(s-self.__sides[2])))/2*s
        return h

    def get_square(self):
        s = self.__len__/2
        S = sqrt((s(s - self.__sides[0])(s-self.__sides[1])(s-self.__sides[2])))
        return S
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__sides = self.sides_count * [i for i in sides]
        else:
            self.__sides = [1 * self.sides_count]

    def get_sides(self):
        return [*self.__sides]
    def get_volume(self):
        return self.__sides[0] * 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

