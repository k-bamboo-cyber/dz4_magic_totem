"""Описание чудовищ."""
from abc import ABC, abstractmethod
import random


class Monster(ABC):
    """Абстрактный класс чудовищ."""

    mo_force = random.randint(5, 20)
    mo_life_count = random.randint(5, 30)
    mon_type = ''

    @abstractmethod
    def go(self, mo_force):
        """Метод атаки."""
        pass


class Goblin(Monster):
    """Класс гоблинов."""

    mo_force = Monster.mo_force
    mo_life_count = Monster.mo_life_count
    mon_type = 'Гоблин'

    def go(self, mo_force: int):
        """Ближняя атака гоблина."""
        print('Гоблин атакует в ближнем бою')
        return 'ближний бой', mo_force


class Skeleton(Monster):
    """Класс скелетонов."""

    mo_force = Monster.mo_force
    mo_life_count = Monster.mo_life_count
    mon_type = 'Скелетон'

    def go(self, mo_force: int):
        """Атака скелетона из лука."""
        print('Скелетон атакует из лука')
        return 'луковая атака', mo_force


class Ogre(Monster):
    """Класс огров."""

    mo_force = Monster.mo_force
    mo_life_count = Monster.mo_life_count
    mon_type = 'Огр'

    def go(self, mo_force: int):
        """Атака мага."""
        print('Маг атакует')
        return 'магия', mo_force


class MonsterFactory(ABC):
    """Абстрактная фабрика игрового противника."""

    @abstractmethod
    def create_monster(self):
        """Создание чудовища."""
        pass


class GoblinFactory(MonsterFactory):
    """Фабрика гоблинов."""

    def create_monster(self):
        """Создание чудовища."""
        return Goblin()


class SkeletonFactory(MonsterFactory):
    """Фабрика скелетонов."""

    def create_monster(self):
        """Создание чудовища."""
        return Skeleton()


class OgreFactory(MonsterFactory):
    """Фабрика огров."""

    def create_monster(self):
        """Создание чудовища."""
        return Ogre()


def mon_spawner():
    """Маппинг для чудовищ."""
    spawner_to_factory_mapping = {
        "гоблин": GoblinFactory,
        "скелетон": SkeletonFactory,
        "огр": OgreFactory}
    monster_type_list = ["гоблин", "скелетон", "огр"]
    SPAWNER_TYPE = random.choice(monster_type_list)
    spawner = spawner_to_factory_mapping[SPAWNER_TYPE]()
    monster = spawner.create_monster()
    print('Вы встретили чудовище {0}, с  {1} жизнями и силой удара {2}'
          .format(monster.mon_type,
                  monster.mo_life_count, monster.mo_force))
    return monster
