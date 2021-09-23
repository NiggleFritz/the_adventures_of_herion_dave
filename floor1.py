# import math
# import random
# import random
# import time
# from pprint import pprint
# from art1 import logo, logo2, enemy_list
# from hero_class import Hero
# from enemy_class import Enemy, Boss, enemygen, enemy_attack, first_enemies
# import os
from floor1_encounters import *
from functions_for_the_game import level_generator, gen_character, create_class, typing, clear_screen, battle, \
    game_over, is_dead


def floor_1():
    typing("FLOOR ONE")
    time.sleep(3)
    clear_screen()
    # encounter = random.randint(0, 20)
    floor1_1()
