import cmd
import textwrap
import sys
import os
import time
import random


# Player Class #


class Player:
    def __init__(self):
        self.name = ''
        self.hp = str(150)
        self.attack = str(10)
        self.defense = str(10)
        self.weapon = 'fist'
        self.armor = 'shirt'
        self.defeated = False


myPlayer = Player()


# Foe Classes#


class GrimyGoblin:
    def __init__(self):
        self.name = 'Grimy Goblin'
        self.hp = str(100)
        self.attack = str(10)
        self.defense = str(10)
        self.defeated = False


grimyGoblin = GrimyGoblin()


class SadisticSpider:
    def __init__(self):
        self.name = 'Grimy Goblin'
        self.hp = 250
        self.attack = 25
        self.defeated = False


sadisticSpider = SadisticSpider()


class WickedWyvern:
    def __init__(self):
        self.name = 'Grimy Goblin'
        self.hp = 500
        self.attack = 50
        self.defeated = False


wickedWyvern = WickedWyvern()


class WiseOldMan:
    def __init__(self):
        self.name = 'Grimy Goblin'
        self.hp = 1000
        self.attack = 100
        self.defeated = False


wiseOldMan = WiseOldMan()


class Nightmare:
    def __init__(self):
        self.name = 'Grimy Goblin'
        self.hp = 2500
        self.attack = 250
        self.defeated = False


nightmare = Nightmare()
# Gameplay #


def title_screen():
    os.system('clear')
    print('############################')
    print('## Welcome to dwoofScape! ##')
    print('############################')
    print('         -- Play --         ')
    print('         -- Help --         ')
    print('         -- Quit --         ')
    print(' Created By: Derek Woughter ')
    userchoice = input("> ")
    if userchoice.lower() == "play":
        start_game()
    elif userchoice.lower() == "help":
        help_menu()
    elif userchoice.lower() == "quit":
        sys.exit()
    while userchoice.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        userchoice = input("> ")
        if userchoice.lower() == "play":
            start_game()
        elif userchoice.lower() == "help":
            help_menu()
        elif userchoice.lower() == "quit":
            sys.exit()


def help_menu():
    os.system('clear')
    print('############################')
    print('##    dwoofScape Help     ##')
    print('############################')
    print('--   Type your commands   --')
    print('--     Fight the foes     --')
    print('--   Earn advanced gear   --')
    print('--  Good luck, have fun!  --')
    input("\nPress Enter to Return to Main Menu...")
    title_screen()


def player_attack(monster):
    monster_hp = int(monster.hp)
    bonus = random.randint(0, 10)
    player_damage = (myPlayer.attack + str(bonus))
    print(myPlayer.name + " did " + player_damage + " damage!")
    new_monster_hp = int(monster.hp) - int(player_damage)
    monster.hp = new_monster_hp


def monster_attack(monster):
    bonus = random.randint(0, 10)
    monster_damage = (monster.attack + str(bonus))
    print(monster.name + " did " + monster_damage + " damage!")
    new_player_hp = int(myPlayer.hp) - int(monster_damage)
    myPlayer.hp = new_player_hp


def goblin_defeated():
    print("made it this far")
    input("nice")


def fight(monster):
    my_current_hp = myPlayer.hp
    monster_current_hp = monster.hp
    while int(my_current_hp) > 0 and monster_current_hp > str(0):
        print(myPlayer.name + " (" + my_current_hp + " HP) VS " + monster.name + " (" + monster_current_hp + " HP)")
        style = input("Choose attack style (Aggressive / Defensive)\n>")
        if style.lower() == "aggressive":
            myPlayer.attack = myPlayer.attack + str(1)
            player_attack(monster)
        elif style.lower() == "defensive":
            myPlayer.defense = myPlayer.defense + str(1)
            player_attack(monster)
        while style.lower() not in ["aggressive", "defensive"]:
            print("Please choose 'aggressive' or 'defensive'...")
            style = input("> ")
            if style.lower() == "aggressive":
                myPlayer.attack = myPlayer.attack + str(1)
                player_attack(monster)
            elif style.lower() == "defensive":
                myPlayer.defense = myPlayer.defense + str(1)
                player_attack(monster)
        monster_attack(monster)


def start_game():
    os.system('clear')
    intro1 = "Tap.. Tap.. Tap..\n"
    intro2 = "Stranger: You okay there pal? \nLooks like a nasty cut on your head... \nWhat's your name?\n"
    for character in intro1:
        sys.stdout.write(character)
        sys.stdout.flush()
        #time.sleep(0.08)
    for character in intro2:
        sys.stdout.write(character)
        sys.stdout.flush()
        #time.sleep(0.05)
    #time.sleep(.5)

    player_name = input("Input Name > ")
    myPlayer.name = player_name

    intro3 = ("Ugh... Yeah, I'm Alright. Name's " + myPlayer.name + ".\n")
    intro4 = "Where am I?\n"
    intro5 = "Stranger: Heck if I know, but it's getting dark. Best get somewhere saf-\n"
    intro6 = "*WHACK*\n"
    intro7 = "The stranger collapses suddenly, hitting the ground with a *THUMP*\n"
    intro8 = "Where he stood now towers a Grimy Goblin...\n"

    for character in intro3:
        sys.stdout.write(character)
        sys.stdout.flush()
        #time.sleep(0.05)
    for character in intro4:
        sys.stdout.write(character)
        sys.stdout.flush()
        #time.sleep(0.07)
    #time.sleep(.5)
    for character in intro5:
        sys.stdout.write(character)
        sys.stdout.flush()
        #time.sleep(0.05)
    for character in intro6:
        sys.stdout.write(character)
        sys.stdout.flush()
        #time.sleep(0.02)
    #time.sleep(.5)
    for character in intro7:
        sys.stdout.write(character)
        sys.stdout.flush()
       # time.sleep(0.05)
    #time.sleep(.5)
    for character in intro8:
        sys.stdout.write(character)
        sys.stdout.flush()
        #time.sleep(0.07)
    #time.sleep(.5)
    goblinchoice = input("It appears you have no choice but to fight the goblin...\n What will you do?\n> ")
    if goblinchoice.lower() in ["fight", "fight goblin", "fight the goblin", "fight grimy goblin",
                                "fight the grimy goblin"]:
        fight(grimyGoblin)
    while goblinchoice.lower() not in ["fight", "fight goblin", "fight the goblin", "fight grimy goblin",
                                       "fight the grimy goblin"]:
        print("Please enter 'fight' to continue.")
        goblinchoice = input("> ")
        if goblinchoice.lower() == "fight":
            fight(grimyGoblin)


def death_screen():
    os.system('clear')
    print("You Lose")
    input("Press Enter to Return to Main Menu...")
    title_screen()


def win_screen():
    os.system('clear')
    print("You Win!")
    input("Press Enter to Return to Main Menu...")
    title_screen()


defeated_bosses = {'grimy_goblin': False, 'sadistic_spider': False, 'wicked_wyvern': False,
                   'wise_old_man': False, 'nightmare': False}

weapons = {'nasty_knife': False, 'feisty_fang': False, 'twisted_talon': False,
           'sturdy_staff': False, 'rubber_chicken': False}

armor = {'tattered_tassets': False, 'putrid_pelt': False, 'horrible_hide': False,
         'clever_cloak': False, 'party_hat': False}


title_screen()


goblin_defeated()


