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
        self.attack = str(10000)
        self.defense = str(10000)
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
        self.weapon = 'nasty knife'
        self.armor = 'tattered tassets'
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
    print('      Created By: dwoof     ')
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
    bonus = random.randint(-10, 20)
    player_damage = abs(int(myPlayer.attack) + int(bonus) - int(monster.defense))
    print(myPlayer.name + " did " + str(player_damage) + " damage!")
    new_monster_hp = int(monster.hp) - int(player_damage)
    monster.hp = new_monster_hp


def monster_attack(monster):
    bonus = random.randint(-10, 20)
    monster_damage = abs(int(monster.attack) + int(bonus) - int(myPlayer.defense))
    print(monster.name + " did " + str(monster_damage) + " damage!")
    new_player_hp = int(myPlayer.hp) - int(monster_damage)
    myPlayer.hp = new_player_hp


def loot(monster):
    print("You've found a " + monster.weapon + " and " + monster.armor)
    print("Type 'equip " + monster.weapon + "' and 'equip " + monster.armor + "' to wield them \n")
    while myPlayer.weapon != monster.weapon or myPlayer.armor != monster.armor:
        equip = input("> ")
        if equip.lower() == "equip " + monster.weapon:
            myPlayer.weapon = monster.weapon
            print(monster.weapon + " equipped!")
        elif equip.lower() == "equip " + monster.armor:
            myPlayer.armor = monster.armor
            print(monster.armor + " equipped!")


def goblin_defeated():
    grimyGoblin.defeated = True
    os.system('clear')
    goblin1 = "You give the grimy goblin one last kick for good measure.\n"
    goblin2 = "It appears the goblin has some loot that may be of use to you.\n"
    goblin3 = "Looting enemies will give you items to help on your journey.. \nAlways check after defeating one!\n"
    goblin4 = "Type 'loot grimy goblin' to claim it before moving on.\n"
    for character in goblin1:
        sys.stdout.write(character)
        sys.stdout.flush()
        #time.sleep(0.05)
    #time.sleep(1)
    for character in goblin2:
        sys.stdout.write(character)
        sys.stdout.flush()
        #time.sleep(0.05)
    #time.sleep(1)
    for character in goblin3:
        sys.stdout.write(character)
        sys.stdout.flush()
        #time.sleep(0.05)
    #time.sleep(1)
    for character in goblin4:
        sys.stdout.write(character)
        sys.stdout.flush()
        #time.sleep(0.05)
    lootgoblin = input("> ")
    if lootgoblin.lower() in ["loot", "loot goblin", "loot the goblin", "loot grimy goblin",
                              "loot the grimy goblin"]:
        loot(grimyGoblin)
    while lootgoblin.lower() not in ["loot", "loot goblin", "loot the goblin", "loot grimy goblin",
                                     "loot the grimy goblin"]:
        print("Please enter 'loot grimy goblin' to continue.")
        lootgoblin = input("> ")
        if lootgoblin.lower() in ["loot", "loot goblin", "loot the goblin", "loot grimy goblin",
                                  "loot the grimy goblin"]:
            loot(grimyGoblin)


def fight(monster):
    os.system('clear')
    while int(myPlayer.hp) > 0 and int(monster.hp) > 0:
        print(myPlayer.name + " (" + str(myPlayer.hp) + " HP) VS " + monster.name + " (" + str(monster.hp) + " HP)")
        style = input("Choose attack style (Aggressive / Defensive)\n>")
        os.system('clear')
        if style.lower() == "aggressive":
            myPlayer.attack = int(myPlayer.attack) + int(1)
            player_attack(monster)
        elif style.lower() == "defensive":
            myPlayer.defense = int(myPlayer.defense) + int(1)
            player_attack(monster)
        while style.lower() not in ["aggressive", "defensive"]:
            print("Please choose 'aggressive' or 'defensive'...")
            style = input("> ")
            os.system('clear')
            if style.lower() == "aggressive":
                myPlayer.attack = int(myPlayer.attack) + int(1)
                player_attack(monster)
            elif style.lower() == "defensive":
                myPlayer.defense = int(myPlayer.defense) + int(1)
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
        if goblinchoice.lower() in ["fight", "fight goblin", "fight the goblin", "fight grimy goblin",
                                    "fight the grimy goblin"]:
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


weapons = {'nasty_knife': False, 'feisty_fang': False, 'twisted_talon': False,
           'sturdy_staff': False, 'rubber_chicken': False}

armor = {'tattered_tassets': False, 'putrid_pelt': False, 'horrible_hide': False,
         'clever_cloak': False, 'party_hat': False}


title_screen()


goblin_defeated()

input("you made it this far")

