import math

class Figure:

    def __init__(self , color , sides , filled= bool):
        self.__sides = sides
        self.__color = color
        self.filled = filled
        self.sides_count = 0

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def set_color(self , *new_color):
        if self.__is_valid_color(new_color):
            self.__color = new_color

    def set_sides(self , *sides):
        if len(sides) == self.sides_count:
            self.__sides = sides

    def __is_valid_color(self , color):
        for c  in color:
            if c not in range(255):
                return False
            continue
        else: return True


    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):

    def __init__(self , color, sides):
        super().__init__(color , sides)
        self.sides_count = 1
        self.sides = [sides if isinstance(sides , int) else [1]]
        self.__radius = self.get_sides()/2*math.pi

    def get_square(self):
        return math.pi * self.__radius**2


class Triangle(Figure):
    def __init__(self , color , *sides):
        super().__init__(color , sides)
        self.sides_count = 3
        self.__sides = [sides if len(sides) == self.sides_count else [1,1,1]]
        self.__color = color

    def get_square(self):
        p = sum(super().get_sides())/2
        return math.sqrt(p * (p - super().get_sides()[0])
                         *(p - super().get_sides()[1])
                         *(p - super().get_sides()[2]))



class Cube(Figure):
    def __init__(self , color , side):
        self.side = side
        super().__init__(color , sides=[side ,side,side,side,side,side,side,side,side,side,side,side])
        self.sides_count = 12



    def get_volume(self):
        return self.side**3

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

tri = Triangle((156,156,78) , 3,4,5)
print(tri.get_square())
print(tri.get_color())
tri.set_color(12,12,12)
tri.set_sides(40,50,30)
print(tri.get_color())
print(tri.get_sides())
print(tri.get_square())