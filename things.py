"""Описание предметов."""
from abc import ABC, abstractmethod
import random


class Things(ABC):
    """Абстрактный класс предметов."""

    @abstractmethod
    def get_thing(self, th_force: int):
        """Метод, наличие которого обязательно у всех."""
        return self


class Sword(Things):
    """Класс мечей."""

    th_force = random.randint(5, 30)

    def get_thing(self, th_force: int):
        """Получение предмета."""
        return th_force


class Bow(Things):
    """Класс луков."""

    th_force = random.randint(5, 30)

    def get_thing(self, th_force: int):
        """Получение предмета."""
        return th_force


class Arrow(Things):
    """Класс стрел."""

    th_force = random.randint(5, 30)

    def get_thing(self, th_force: int):
        """Получение предмета."""
        return th_force


class Book(Things):
    """Класс книг."""

    th_force = random.randint(5, 30)

    def get_thing(self, th_force: int):
        """Получение предмета."""
        return th_force


class Apple(Things):
    """Класс яблок."""

    th_force = random.randint(5, 30)

    def get_thing(self, th_force: int):
        """Получение предмета."""
        return th_force


class Totem(Things):
    """Класс тотемов."""

    th_force = 0

    def get_thing(self, th_force: int):
        """Получение предмета."""
        return th_force


class ThingsFactory(ABC):
    """Абстрактный класс фабрики предметов."""

    @abstractmethod
    def gen_thing(self):
        """Получение предмета."""
        pass


class SwordFactory(ThingsFactory):
    """Абстрактный класс фабрики мечей."""

    def gen_thing(self):
        """Получение предмета."""
        return Sword()


class BowFactory(ThingsFactory):
    """Абстрактный класс фабрики луков."""

    def gen_thing(self):
        """Получение предмета."""
        return Bow()


class ArrowFactory(ThingsFactory):
    """Абстрактный класс фабрики стрел."""

    def gen_thing(self):
        """Получение предмета."""
        return Arrow()


class BookFactory(ThingsFactory):
    """Абстрактный класс фабрики книг."""

    def gen_thing(self):
        """Получение предмета."""
        return Book()


class AppleFactory(ThingsFactory):
    """Абстрактный класс фабрики яблок."""

    def gen_thing(self):
        """Получение предмета."""
        return Apple()


class TotemFactory(ThingsFactory):
    """Абстрактный класс фабрики яблок."""

    def gen_thing(self):
        """Получение предмета."""
        return Totem()


def th_spawner():
    """Маппинг  для предметов."""
    spawner_to_factory_mapping = {
        "меч": SwordFactory,
        "лук": BowFactory,
        "стрела": ArrowFactory,
        "книга": BookFactory,
        "яблоко": AppleFactory,
        "тотем": TotemFactory
    }
    things_type_list = ["меч", "лук", "стрела", "книга", "яблоко", "тотем"]
    SPAWNER_TYPE = random.choice(things_type_list)
    spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()
    thing = spawner.gen_thing()
    return thing
