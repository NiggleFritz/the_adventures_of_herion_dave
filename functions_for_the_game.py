# importing modules
import math
import random
import time
# from pprint import pprint
# from art1 import logo, logo2, enemy_list
from hero_class import Hero
from enemy_class import Enemy, Boss, enemy_gen, enemy_attack, first_enemies
import os
import sys

# import sleep to show output for some time period
from time import sleep


# ***Clear the screen function***
def clear_screen():
    """
    This function will clear the screen
    """
    sleep(2)
    os.system('cls')


# function for making the illusion of typing on every print
def typing(message):
    print("")
    for word in message:
        time.sleep(random.choice([0.3, 0.11, 0.08, 0.07,   0.07, 0.07, 0.06, 0.06, 0.05, 0.01]))
        sys.stdout.write(word)
        sys.stdout.flush()
    time.sleep(.1)
    return ""


# we're gonna ask the user a series of questions and the answers to those questions are gonna build our class
def create_class():
    global heroAttack, heroRanged, heroMagic, heroDefence, heroLuck
    typing('Type "1" for first option, and "2" for the second option')
    a = int(input(typing("Are you more strategic(1) or more of a warrior(2)?: ")))
    while a != 1 and a != 2:
        typing(f"{a} is not either '1' or '2'... invalid option\n")
        m1 = typing("Are you more strategic(1) or more of a warrior(2)?: \n")
        a = int(input(m1))

    if a == 1:
        # Strategic path
        heroAttack = 5
        heroDefence = 7
    elif a == 2:
        # Warrior path
        heroAttack = 10
        heroDefence = 15

    # Determining the hero's luck!
    time.sleep(.5)
    typing("Let's see how much luck you have")
    input(typing("Press enter to roll a dice..."))
    time.sleep(.5)
    typing('Rolling dice...')
    heroLuck = random.randint(3, 10)
    typing(f"Your hero has {heroLuck} points out of 10")

    typing("Interesting...")
    # Determining the hero's magic!
    c = int(input(typing("Are you more of a bow and arrow(1) or a magic user?(2): ")))
    while c != 1 and c != 2:
        typing(f"{c} is not either '1' or '2'... invalid option")
        c = int(input(typing("Are you more of a bow and arrow(1) or a magic user(2)?: ")))

    if c == 1:
        # Archer Path
        typing("I thought you'd choose magic... Arrows are for asshole")
        time.sleep(2)
        typing("But anyways, who am I to judge")
        heroRanged = 15
        heroMagic = 10
    elif c == 2:
        typing("I thought you'd choose arrows... You only chose Magic because you don't want to fight...")
        time.sleep(2)
        typing("But anyways, who am I to judge")
        heroRanged = 10
        heroMagic = 15

    time.sleep(1)
    # Determining the hero's Name!
    hero_name = "Heroin Dave"
    typing(f"You have created your character, {hero_name}...")
    time.sleep(5)
    clear_screen()

    return heroAttack, heroLuck, heroRanged, heroDefence, heroMagic, hero_name


# printing the logo
# print(logo)
# time.sleep(15)
clear_screen()


# print(logo2)
# We're going to use class_data as a list, so 0 = heroAttack, 1 = hero_luck and so on...
class_data = create_class()
gen_character = Hero(hero_health=30, hero_damage=class_data[0], hero_luck=class_data[1], hero_ranged=class_data[2],
                     hero_defence=class_data[3], hero_magic=class_data[4], hero_name=class_data[5])


# Some functions that will help us run our game smoother
def hit_chance(luck):
    hit = random.randint(0, 4)
    if luck < hit:
        typing("LOL, you missed")
        return False
    else:
        typing("You hit the enemy!")
        return True


def is_dead(health):
    if health < 1:
        return True
    else:
        return False


def loot(luck, generate_character):
    loot_chance = random.randint(0, 4)
    if luck < loot_chance:
        typing("No loot found );")
    else:
        # I have 5 diff tables to look at, this tables are the txt files!
        table_number = random.randint(0, 4)
        loot_table_list = ["items", 'ranged', 'defence', 'magic', 'attack']
        # through this new variable is going to randomly look up in any of the files
        item_type = loot_table_list[table_number]
        # opening the file
        with open(item_type + '.txt', 'r') as file:
            lines = file.readlines()

        typing("The enemy dropped a....")
        item = random.randint(0, len(lines)-1)
        item_line = lines[item]
        split_item_line = item_line.split(',')
        item_name = split_item_line[0]
        value = int(split_item_line[1])
        typing(item_name)

        if item_type == 'attack':
            # We programmed a lot of getters and setters so we can actually get them and edit them in here
            generate_character.set_damage(generate_character.get_attack() + value)
            typing(f"Your new attack is {generate_character.get_attack()}")

        elif item_type == "ranged":
            generate_character.set_ranged(generate_character.get_ranged() + value)
            typing("Your new Ranged Attack is...")
            typing(generate_character.get_ranged())

        elif item_type == "defence":
            # Hero.setDefence(Hero.getDefence()+value)
            generate_character.set_defence(generate_character.get_defence() + value)
            typing("Your new Defence is...")
            typing(generate_character.get_defence())

        elif item_type == "magic":
            generate_character.set_magic(generate_character.get_magic() + value)
            typing("Your new Magic attack is...")
            typing(generate_character.get_magic())

        else:
            if split_item_line[2] == 'luck':
                generate_character.set_luck(generate_character.get_luck() + value)
                typing(f'Your new Luck is {generate_character.get_luck()}')

            elif split_item_line[2] == "health":
                generate_character.set_health(generate_character.get_health() + value)
                typing(f"Your new Health is {generate_character.get_health()}")


def game_over(enemy_dead):
    """
    :param enemy_dead:
    :return: this function will let us know when the game is over
    """
    if enemy_dead is True:
        typing("You've defeated your enemy")

    else:
        typing(f"You are out of health {class_data[5]}!")
        time.sleep(8)
        typing("It's a shame... Game Over")
        exit()


def battle(floor, enemygen, generate_character):
    """
    :param floor:
    :param enemygen:
    :param generate_character:
    :return: it will return the battle between the hero and the enemy
    """

    encounter = True
    while encounter:
        # if the chapter is 1
        if floor == 1:
            typing(f"Choose your weapon {class_data[5]}!")
            typing("Bare Hands(1) \nSomething near you to throw(2)")
            choice = int(input(typing("What do you choose?: ")))
            while choice != 1 and choice != 2:
                typing(f"WTF... try to type correctly..")
                typing("Bare Hands(1) \nSomething near you to throw(2)")
            if choice == 1:
                damage = generate_character.get_attack()
            if choice == 2:
                damage = generate_character.get_attack()
            typing("You are preparing for the attack")
            hit = hit_chance(generate_character.get_luck())
            if hit is True:
                enemygen.set_health(enemygen.get_health() - damage)
                typing("You've hit the enemy!")
                typing(f"The enemy health is {enemygen.get_health()}")
            else:
                typing("Your attack missed!")

            enemy_is_dead = is_dead(enemygen.get_health())

            if enemy_is_dead is False:
                # in this case as the enemy_attack is a negative value, we need to put the '+' sign because otherwise
                # it will give more life to our character when an enemy hits it.
                generate_character.set_health(generate_character.get_health() + enemy_attack(enemygen.get_chance(),
                                                                                             enemygen.get_attack(),
                                                                                             enemygen.get_name(),
                                                                                             generate_character.
                                                                                             get_defence()))

                # Checking if the enemy is dead
                character_is_dead = is_dead(generate_character.get_health())

                if character_is_dead is True:
                    return False
                else:
                    typing(f"You character remaining health is {generate_character.get_health()}")

            # this else is when the enemy dies
            else:
                return True

        else:
            # when there are other chapters
            typing(f"Choose your weapon {class_data[5]}!")
            typing("Sword Attack(1) \nRanged Attack(2) \nMagic Attack(3)")
            choice = int(input())
            while choice != 1 and choice != 2 and choice != 3:
                typing(f"WTF! A {enemygen.get_name()} is trying to kill us and you're "
                       f"typing the wrong keys you donkey!")
                time.sleep(3)
                typing("Sword Attack(1) \nRanged Attack(2) \nMagic Attack(3) \n Choose your weapon: ")
                choice = int(input())
            if choice == 1:
                damage = generate_character.get_attack()
            elif choice == 2:
                damage = generate_character.get_ranged()
            else:
                damage = generate_character.get_magic()

            typing("You are preparing for the attack")
            hit = hit_chance(generate_character.get_luck())

            if hit is True:
                enemygen.set_health(enemygen.get_health() - damage)
                typing("You've the enemy!")
                typing(f"The enemy health is {enemygen.get_health()}")
            else:
                typing("Your attack missed!")

            enemy_is_dead = is_dead(enemygen.get_health())

            if enemy_is_dead is False:
                # in this case as the enemy_attack is a negative value, we need to put the '+' sign because otherwise
                # it will give more life to our character when an enemy hits it.
                generate_character.set_health(generate_character.get_health() + enemy_attack(enemygen.get_chance(),
                                                                                             enemygen.get_attack(),
                                                                                             enemygen.get_name(),
                                                                                             generate_character.
                                                                                             get_defence()))

                # Checking if the enemy is dead

                character_is_dead = is_dead(generate_character.get_health())

                if character_is_dead is True:
                    return False

                else:
                    typing(f"You character remaining health is {generate_character.get_health()}")

            # this else is when the enemy dies
            else:
                typing("You have defeated the enemy")
                typing("Did it drop any loot?")
                loot(generate_character.get_luck(), generate_character)

                return True


def level_generator(chapter, generate_character, level):
    # the function has 'level' as parameter, meaning that we put 1 as a parameter
    # math.ceil(level*5) its going to return the number of enemies * 5, so we're going to have 5 enemies lv 1
    max_number_of_enemies = math.ceil(level*5)
    for enemy in range(0, max_number_of_enemies):
        # chance of generating a boss while we're creating an enemy
        boss_chance = random.randint(1, 10)
        if boss_chance > 7:
            level_boss = True
        else:
            level_boss = False
        character_dead = battle(floor=chapter, enemygen=enemy_gen(level_boss), generate_character=generate_character)
        game_over(character_dead)
