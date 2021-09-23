import random
import math


# We're constructing a enemy class
class Enemy:
    def __init__(self, enemy_health, enemy_damage, enemy_special, enemy_chance, enemy_name):
        # attributes for the enemy class
        self.health = enemy_health
        self.attack = enemy_damage
        self.special = enemy_special
        self.chance = enemy_chance
        self.name = enemy_name

    # getters for the enemy class
    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_special(self):
        return self.special

    def get_chance(self):
        return self.chance

    def get_name(self):
        return self.name

    # setters for the enemy class
    def set_health(self, new_health):
        self.health = new_health

    def set_damage(self, new_damage):
        self.attack = new_damage

    def set_special(self, new_special):
        self.special = new_special

    def set_chance(self, new_chance):
        self.chance = new_chance

    def set_name(self, new_name):
        self.name = new_name

    # we're going to make an inherit method
    # the parent class will be the enemy method and the boss will be the child class


class Boss(Enemy):
    def __init__(self, enemy_health, enemy_damage, enemy_special, enemy_chance, enemy_name, enemy_super_move):
        # in order to actually inherit the Enemy class we need to use the super method
        super().__init__(enemy_health, enemy_damage, enemy_special, enemy_chance, enemy_name)
        self.superMove = enemy_super_move

    # getter for SuperMove
    def get_super(self):
        return self.superMove

    # setter for SuperMove
    def set_super(self, new_super_move):
        self.superMove = new_super_move

# If I want to create a last boss or something I can just create an inheritance of Boss with the super method


# creating a function to create enemies
def enemy_gen(level_boss):
    """
    :param level_boss:
    :return: This function will return an enemy or a boss depending if
    the variable 'level boss' is True or False
    """
    # temp = []
    with open('adjective.txt', 'r') as file:
        lines = file.readlines()
        # as we want to choose a random adjective, our adjective is going to be between
        # the first adjective (0) and the length of the file -1 because of how Python operates the numbers
        # we're putting the [:-1] to eliminate from the text the '/n' that appears in each letter
        adjective = lines[random.randint(0, len(lines)-1)][:-1]
    with open('animal.txt', 'r') as file2:
        lines2 = file2.readlines()
        animal = lines2[random.randint(0, len(lines)-1)][:-1]

    if level_boss is False:
        health = random.randint(50, 100)
        attack = random.randint(5, 10)
        special = random.randint(10, 20)
        chance = random.randint(1, 10)

        # In here we're saying: call the class Enemy and give those attributes
        return Enemy(health, attack, special, chance, adjective + " " + animal)

    else:
        health = random.randint(200, 250)
        attack = random.randint(20, 40)
        special = random.randint(50, 60)
        chance = random.randint(1, 8)
        super_move = random.randint(100, 200)

        # Return the Boss object and give it those attributes
        return Boss(health, attack, special, chance, adjective + " " + animal, super_move)


def enemy_attack(hit_chance, attack_value, name, defence):
    """
    :param hit_chance:
    :param attack_value:
    :param name:
    :param defence:
    :return: This function will return the attack inflicted if an enemy hits you
    """
    print(f"{name} is preparing for an attack ")
    hit = random.randint(0, 10)
    if hit_chance >= hit:
        print("It has hit you!")
        loss = attack_value - defence
        print(f"You stagger and you loose {loss} points of health")
        return math.ceil(loss)
    else:
        print(f"You're lucky: the enemy missed you")
        return 0


def first_enemies(name):
    enemy_health = random.randint(5, 15)
    ene_attack = random.randint(3, 15)
    enemy_special = random.randint(5, 25)
    enemy_chance = random.randint(3, 10)
    enemy = Enemy(enemy_health=enemy_health, enemy_damage=ene_attack, enemy_special=enemy_special,
                  enemy_chance=enemy_chance, enemy_name=name)
    return enemy
