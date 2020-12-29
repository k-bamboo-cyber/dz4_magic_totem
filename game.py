"""Игра на выживание."""
import random
import monsters
import heroes
from heroes import Hero
import things
from things import Things

while True:
    hero_choice = input('Выберите героя. 1 - воин  , 2 - лучник , 3 - маг : ')
    if hero_choice == '1':
        hero = Hero.Warrior()
        break
    elif hero_choice == '2':
        hero = Hero.Archer()
        break
    elif hero_choice == '3':
        hero = Hero.Magician()
        break
    else:
        while hero_choice != '1' and hero_choice != '2':
            print("Введите 1 или 2")
            ans = format(input())
