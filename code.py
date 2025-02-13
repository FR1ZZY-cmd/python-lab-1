from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, int) and not isinstance(capacity_volume, float):
            raise TypeError("Вместимость стакана должна быть числом.")
        if capacity_volume <= 0:
            raise ValueError("Вместимость стакана должна быть положительной.")

        if not isinstance(occupied_volume, int) and not isinstance(occupied_volume, float):
            raise TypeError("Заполненость стакана должна быть числом.")
        if occupied_volume <= 0:
            raise ValueError("Заполненость стакана должна быть положительной.")
        if occupied_volume <= capacity_volume:
            raise ValueError("Заполненость стакана должна быть меньше либо равна вместимости стакана.")

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    first = Glass(10, 20)
    second = Glass(10.3, 15.2)

    third = Glass('10','20')

