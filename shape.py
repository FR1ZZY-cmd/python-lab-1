from typing import Union


class Shape:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def area(self) -> float:
        raise NotImplementedError("Метод поиска площади должен быть переопределен в подклассе")

    def perimeter(self) -> float:
        raise NotImplementedError("Метод поиска периметра должен быть переопределен в подклассе")

    def __str__(self) -> str:
        return f"{self.name} ({self.color})"

    def __repr__(self) -> str:
        return f"Shape(name='{self.name}', color='{self.color}')"


class Rectangle(Shape):
    def __init__(self, name: str, color: str, width: float, height: float):
        super().__init__(name, color)
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def scale(self, factor: float) -> None:
        self.width *= factor
        self.height *= factor

    def __str__(self) -> str:
        return f"{super().__str__()} - Ширина: {self.width}, Высота: {self.height}"

    def __repr__(self) -> str:
        return f"Rectangle(name='{self.name}', color='{self.color}', width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, name: str, color: str, side: float):
        super().__init__(name, color, side, side)
        self.side = side

    def area(self) -> float:
        return self.side * self.side

    def __str__(self):
        return f"{super(Rectangle, self).__str__()} - Сторона: {self.side}"

    def __repr__(self):
        return f"Square(name='{self.name}', color='{self.color}', side={self.side})"



if __name__ == '__main__':
    shape = Shape("Фигура", "Белый")
    print(shape)  # Фигура (Белый)


    rectangle = Rectangle("Прямоугольник", "Красный", 5, 10)
    print(rectangle)  # Прямоугольник (Красный) - Ширина: 5, Высота: 10
    print(f"Площадь прямоугольника: {rectangle.area()}") # Площадь прямоугольника: 50
    print(f"Периметр прямоугольника: {rectangle.perimeter()}") # Периметр прямоугольника: 30
    rectangle.scale(2)
    print(rectangle) # Прямоугольник (Красный) - Ширина: 10.0, Высота: 20.0

    square = Square("Квадрат", "Синий", 7)
    print(square)  # Квадрат (Синий) - Сторона: 7
    print(f"Площадь квадрата: {square.area()}")  # Площадь квадрата: 49
    print(f"Периметр квадрата: {square.perimeter()}") # Периметр квадрата: 28
    square.scale(3)
    print(square) # Квадрат (Синий) - Сторона: 21.0

    print(repr(shape))
    print(repr(rectangle))
    print(repr(square))
