from functions_for_the_game import battle, game_over, typing, gen_character
from enemy_class import *
import time


def floor1_1():
    typing("You open the door and are greeted with a foul smell. There is a brazer smoldering with a dim light. It "
           "provides just enough illumination that you can make out movement in the back corner. You squint as your "
           "eyes adjust to the dimness. Just then a humanoid shape rises from the ground, and steps into the light.")
    typing("Before you stood the dirtiest, smelliest hippie that you have ever laid eyes on, and living in back alleys "
           "had given you an over exposure to that particular element of society. 'Will you sign this petition to like "
           "save the whales man? They are like super smart' said the smelly hippie")
    typing("Dave having very little experience dealing with other humans politely said 'Dude I am pretty sure I can "
           "smell your balls from here, I am not getting close enough to sign anything'")
    typing("The hippie snarled sounding almost feral? 'How fucking long has he been in here!' Dave thought alarmed. Two"
           " more figures rose from the corners and dave prepared to defend himself against these rabid hippies who "
           "apparently bath in their own ball sweat")
    hippie1 = first_enemies("Hippie")
    who_died_battle1 = battle(floor=1, enemygen=hippie1, generate_character=gen_character)
    game_over(who_died_battle1)
    if who_died_battle1 is True:
        time.sleep(5)
        typing("'Take that you dirty hippies!' Dave stops hammering the Hippies face, and grimaces at the "
               "blood on his hands. After awkwardly flinging his hands at the wall a couple times he wipes them on the"
               " cleanest piece of hippie clothing he could find.")
        move_on = input("Hit enter to continue into the next room")
        if move_on is True:
            return


# def floor1_2():


# def floor1_3():


# def floor1_4():


# def floor1_5():


# def floor1_6():


# def floor1_7():


# def floor1_8():


# def floor1_9():


# def floor1_10():


# def floor1_11():


# def floor1_12():


# def floor1_13():


# def floor1_14():


# def floor1_15():


# def floor1_16():


# def floor1_17():


# def floor1_18():


# def floor1_19():


# def floor1_20():
