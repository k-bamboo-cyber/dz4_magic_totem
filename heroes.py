"""Описание героев."""
from abc import ABC, abstractmethod
import random
import things
from things import Things


class Hero(ABC):
    """Абстрактный класс героя."""

    he_life_count = 30
    arrows = 2
    vi = 0
    start_thing = {'меч': 10}

    def weapon_getting(self, weapon) -> tuple:
        """Получение меча."""
        s_force = random.randint(5, 20)
        print("Вы получили оружие с силой атаки", s_force,
              "\nВзять его? Нажмите 1 или 2."
              "\n1-взять его себе выбросив старый,2-пройти мимо оружия")
        ans = input()
        if ans == '1' or ans == '2':

            return s_force, ans
        else:
            while ans != '1' and ans != '2':
                print("Введите 1 или 2")
                ans = format(input())
            return s_force, ans

    def apple_getting(self, h_life_count: int) -> tuple:
        """Получение яблока."""
        bonus = random.randint(5, 20)
        h_life_count += bonus
        return h_life_count, bonus


class Warrior(Hero):
    """Класс воина."""


class Archer(Hero):
    """Класс лучников."""


class Magician(Hero):
    """Класс магов."""
