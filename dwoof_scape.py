import cmd
import textwrap
import sys
import os
import time
import random
import gc
screenwidth = 50


# Player Class #
class Player:
    def __init__(self):
        self.name = ''
        self.hp = str(200)
        self.attack = str(25)
        self.defense = str(25)
        self.weapon = 'fist'
        self.armor = 'shirt'
        self.defeated = False
        self.level = 1


myPlayer = Player()


class Potions:
    def __init__(self):
        self.lesser_heal = 0
        self.lesser_combat = 0
        self.heal = 0
        self.combat = 0
        self.greater_heal = 0
        self.greater_combat = 0


Potions = Potions()


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
        self.name = 'Sadistic Spider'
        self.hp = str(500)
        self.attack = str(25)
        self.defense = str(25)
        self.weapon = 'feisty fang'
        self.armor = 'putrid pelt'
        self.defeated = False


sadisticSpider = SadisticSpider()


class WickedWyvern:
    def __init__(self):
        self.name = 'Wicked Wyvern'
        self.hp = str(1000)
        self.attack = str(75)
        self.defense = str(75)
        self.weapon = 'twisted talon'
        self.armor = 'horrible hide'
        self.defeated = False


wickedWyvern = WickedWyvern()


class WiseOldMan:
    def __init__(self):
        self.name = 'Wise Old Man'
        self.hp = str(1750)
        self.attack = str(150)
        self.defense = str(150)
        self.weapon = 'sturdy staff'
        self.armor = 'clever cloak'
        self.defeated = False


wiseOldMan = WiseOldMan()


class Nightmare:
    def __init__(self):
        self.name = 'Nightmare'
        self.hp = str(3000)
        self.attack = str(250)
        self.defense = str(250)
        self.weapon = 'rubber chicken'
        self.armor = 'party hat'
        self.defeated = False


nightmare = Nightmare()


class GiantRat:
    def __init__(self):
        self.name = 'Giant Rat'
        self.hp = str(100)
        self.attack = str(10)
        self.defense = str(10)
        self.weapon = 'claw'
        self.armor = 'rough fur'
        self.defeated = False


giantRat = GiantRat()


class Skeleton:
    def __init__(self):
        self.name = 'Skeleton'
        self.hp = str(250)
        self.attack = str(25)
        self.defense = str(25)
        self.weapon = 'bone arm'
        self.armor = 'bone ribs'
        self.level = 1
        self.defeated = False


skeleton = Skeleton()


class Troll:
    def __init__(self):
        self.name = 'Troll'
        self.hp = str(500)
        self.attack = str(50)
        self.defense = str(50)
        self.weapon = 'spiky club'
        self.armor = 'thick skin'
        self.defeated = False


troll = Troll()


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


def start_game():
    os.system('clear')
    intro1 = "Tap.. Tap.. Tap..\n"
    intro2 = "Stranger: You okay there pal? \nLooks like a nasty cut on your head... \nWhat's your name?\n"
    for character in intro1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    for character in intro2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(.5)

    myPlayer.name = input("Input Name > ")
    os.system('clear')
    intro3 = ("Ugh... Yeah, I'm Alright. Name's " + myPlayer.name + ".\n")
    intro4 = "Where am I?\n"
    intro5 = "Stranger: Heck if I know, but it's getting dark. Best get somewhere saf-\n"
    intro6 = "*WHACK*\n"
    intro7 = "The stranger collapses suddenly, hitting the ground with a *THUMP*\n"
    intro8 = "Where he stood now towers a Grimy Goblin...\n"

    for character in intro3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.07)
    time.sleep(.5)
    for character in intro5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in intro6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(.5)
    for character in intro7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(.5)
    for character in intro8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.07)
    time.sleep(2)
    os.system('clear')
    goblinchoice = input("It appears you have no choice but to fight the goblin...\nWhat will you do? (fight) \n> ")
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


def fight(monster):
    bosslist = [grimyGoblin, sadisticSpider, wickedWyvern, wiseOldMan, nightmare]
    trainlist = [giantRat, skeleton, troll]
    os.system('clear')
    if monster in bosslist:
        while int(myPlayer.hp) > 0 and int(monster.hp) > 0:
            linecount = len("{:<25}{:>25}".format((str(myPlayer.name) + " " + str(myPlayer.hp) + "HP"),
                                                  (str(monster.hp) + "HP " + str(monster.name))))
            print("=" * linecount)
            print("{:<25}{:>25}".format((str(myPlayer.name) + " " + str(myPlayer.hp) + "HP"),
                                        (str(monster.hp) + "HP " + str(monster.name))))
            print("{:<25}{:>25}".format(myPlayer.weapon, monster.weapon))
            print("{:<25}{:>25}".format(myPlayer.armor, monster.armor))
            print("=" * linecount)
            style = input("Choose attack (Aggressive / Defensive)\n>")
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
        if int(myPlayer.hp) <= 0:
            death_screen()
        myPlayer.level = myPlayer.level + 1
        startinghp = 100
        maxhp = startinghp * int(myPlayer.level) * int(myPlayer.level)
        myPlayer.hp = maxhp
        if monster in [sadisticSpider, wickedWyvern, wiseOldMan, nightmare]:
            loot(monster)

    elif monster in trainlist:
        while int(myPlayer.hp) > 0 and int(monster.hp) > 0:
            linecount = len("{:<25}{:>25}".format((str(myPlayer.name) + " " + str(myPlayer.hp) + "HP"),
                                                  (str(monster.hp) + "HP " + str(monster.name))))
            print("=" * linecount)
            print("{:<25}{:>25}".format((str(myPlayer.name) + " " + str(myPlayer.hp) + "HP"),
                                        (str(monster.hp) + "HP " + str(monster.name))))
            print("{:<25}{:>25}".format(myPlayer.weapon, monster.weapon))
            print("{:<25}{:>25}".format(myPlayer.armor, monster.armor))
            print("=" * linecount)
            style = input("Choose attack (Aggressive / Defensive / Flee)\n>")
            os.system('clear')
            if style.lower() == "aggressive":
                myPlayer.attack = int(myPlayer.attack) + int(1)
                player_attack(monster)
            elif style.lower() == "defensive":
                myPlayer.defense = int(myPlayer.defense) + int(1)
                player_attack(monster)
            elif style.lower() == "flee":
                input("You flee the battle. Press Enter to Continue...")
                main_loop()
            while style.lower() not in ["aggressive", "defensive", "flee"]:
                print("Please choose 'aggressive' or 'defensive'...")
                style = input("> ")
                os.system('clear')
                if style.lower() == "aggressive":
                    myPlayer.attack = int(myPlayer.attack) + int(1)
                    player_attack(monster)
                elif style.lower() == "defensive":
                    myPlayer.defense = int(myPlayer.defense) + int(1)
                    player_attack(monster)
                elif style.lower() == "flee":
                    input("You flee the battle. Press Enter to Continue...")
                    main_loop()
            monster_attack(monster)
        if int(myPlayer.hp) <= 0:
            death_screen()
        trainloot(monster)


def player_attack(monster):
    if myPlayer.weapon == "fist":
        weapon = 5
    elif myPlayer.weapon == "nasty knife":
        weapon = 10
    elif myPlayer.weapon == "feisty fang":
        weapon = 25
    elif myPlayer.weapon == "twisted talon":
        weapon = 50
    elif myPlayer.weapon == "sturdy staff":
        weapon = 100
    elif myPlayer.weapon == "rubber chicken":
        weapon = 250
    bonus = random.randint(0, int(weapon))
    player_damage = int((int(weapon) * int(myPlayer.attack) / int(monster.defense)) + bonus)
    player_damage_print = (myPlayer.name + " did " + str(player_damage) + " damage!\n")
    for character in str(player_damage_print):
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    monster.hp = (int(monster.hp) - int(player_damage))


def monster_attack(monster):
    if myPlayer.weapon == "fist":
        pwep = 1
    elif myPlayer.weapon == "nasty knife":
        pwep = 10
    elif myPlayer.weapon == "feisty fang":
        pwep = 20
    elif myPlayer.weapon == "twisted talon":
        pwep = 40
    elif myPlayer.weapon == "sturdy staff":
        pwep = 75
    elif myPlayer.weapon == "rubber chicken":
        pwep = 125
    if myPlayer.armor == "shirt":
        parmor = 1
    elif myPlayer.armor == "tattered tassets":
        parmor = 10
    elif myPlayer.armor == "putrid pelt":
        parmor = 25
    elif myPlayer.armor == "horrible hide":
        parmor = 50
    elif myPlayer.armor == "clever cloak":
        parmor = 100
    elif myPlayer.armor == "party hat":
        parmor = 250
    if monster.weapon == "nasty knife":
        mwep = 10
    elif monster.weapon == "feisty fang":
        mwep = 20
    elif monster.weapon == "twisted talon":
        mwep = 40
    elif monster.weapon == "sturdy staff":
        mwep = 75
    elif monster.weapon == "rubber chicken":
        mwep = 125
    elif monster.weapon == "party hat":
        mwep = 500
    elif monster.weapon == "claw":
        mwep = 5
    elif monster.weapon == "bone arm":
        mwep = 25
    elif monster.weapon == "spiky club":
        mwep = 50
    wepbonus = random.randint(0, int(mwep))
    armbonus = random.randint(0, int(parmor))
    monster_damage = int(((pwep * int(monster.attack)) /
                          int(myPlayer.defense)) + abs(wepbonus - armbonus))
    #monster_damage = (int(monster.attack) - int(myPlayer.defense) + bonus) * int(bonus)
    if monster_damage < 0:
        monster_damage = 0
    monster_damage_print = (monster.name + " did " + str(monster_damage) + " damage!\n")
    for character in str(monster_damage_print):
        sys.stdout.write(character)
        sys.stdout.flush()
        #time.sleep(0.03)
    new_player_hp = int(myPlayer.hp) - int(monster_damage)
    myPlayer.hp = new_player_hp


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
        time.sleep(0.05)
    time.sleep(1)
    for character in goblin2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    for character in goblin3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    for character in goblin4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
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


def loot(monster):
    os.system('clear')
    print("You've found a " + monster.weapon + " and " + monster.armor)
    print("Type 'equip " + monster.weapon + "' or 'equip " + monster.armor + "' to wield them \n")
    while myPlayer.weapon != monster.weapon or myPlayer.armor != monster.armor:
        equip = input("> ")
        if equip.lower() == "equip " + monster.weapon:
            myPlayer.weapon = monster.weapon
            print(monster.weapon + " equipped!")
        elif equip.lower() == "equip " + monster.armor:
            myPlayer.armor = monster.armor
            print(monster.armor + " equipped!")
        else:
            print("Please input 'equip " + monster.weapon + "' or 'equip " + monster.armor + "' \n> ")
    main_loop()


def trainloot(monster):
    giantRat.hp = 100
    skeleton.hp = 250
    troll.hp = 500
    os.system('clear')
    roll = random.randint(1, 100)
    if monster is giantRat:
        if roll <= 60:
            Potions.lesser_heal = (Potions.lesser_heal + 1)
            print("[+] Gained 1 Lesser Healing Potion")
        elif 60 < roll <= 90:
            Potions.lesser_heal = (Potions.lesser_heal + 1)
            Potions.lesser_combat = (Potions.lesser_combat + 1)
            print("[+] Gained 1 Lesser Healing Potion\n[+] Gained 1 Lesser Combat Potion")
        elif roll > 90:
            Potions.heal = (Potions.heal + 1)
            Potions.combat = (Potions.combat + 1)
            print("[+] Gained 1 Healing Potion\n[+] Gained 1 Combat Potion")
    elif monster is skeleton:
        if roll <= 60:
            Potions.heal = (Potions.heal + 1)
            print("[+] Gained 1 Healing Potion")
        elif 60 < roll <= 90:
            Potions.heal = (Potions.heal + 1)
            Potions.combat = (Potions.combat + 1)
            print("[+] Gained 1 Healing Potion\n[+] Gained 1 Combat Potion")
        elif roll > 90:
            Potions.greater_heal = (Potions.greater_heal + 1)
            Potions.greater_combat = (Potions.greater_combat + 1)
            print("[+] Gained 1 Greater Healing Potion\n[+] Gained 1 Greater Combat Potion")
    elif monster is troll:
        if roll <= 60:
            Potions.greater_heal = (Potions.greater_heal + 1)
            print("[+] Gained 1 Greater Healing Potion")
        elif 60 < roll <= 90:
            Potions.greater_heal = (Potions.greater_heal + 1)
            Potions.greater_combat = (Potions.greater_combat + 1)
            print("[+] Gained 1 Healing Potion\n[+] Gained 1 Combat Potion")
        elif roll > 90:
            Potions.greater_heal = (Potions.greater_heal + 3)
            Potions.greater_combat = (Potions.greater_combat + 3)
            print("[+] Gained 1 Greater Healing Potion\n[+] Gained 1 Greater Combat Potion")
    input("Press Enter to Continue...")
    main_loop()


def stats():
    os.system('clear')
    startinghp = 100
    maxhp = startinghp * int(myPlayer.level) * int(myPlayer.level)
    print(str(myPlayer.name) + " (" + str(myPlayer.hp) + " / " + str(maxhp) + " HP) - Combat Level " +
          str(myPlayer.level) + "\n")
    print(" - Attack Experience " + str(myPlayer.attack) + "\n")
    print(" - Defense Experience " + str(myPlayer.defense) + "\n")
    print(" - Current Weapon " + str(myPlayer.weapon) + "\n")
    print(" - Current Armor " + str(myPlayer.armor) + "\n")
    input("Press Enter to Return...")
    main_loop()


def train():
    selection = random.randint(1, 100)
    if selection <= 60:
        fight(giantRat)
    elif 60 < selection <= 90:
        fight(skeleton)
    else:
        fight(troll)


def use_item():
    os.system('clear')
    startinghp = 100
    maxhp = startinghp * int(myPlayer.level) * int(myPlayer.level)
    if int(myPlayer.hp) >= maxhp:
        myPlayer.hp = maxhp
        print("Max HP for level!")
    print("Type 'use' followed by item name, or 'exit' to exit" + "\n")
    print(str(myPlayer.name) + " (" + str(myPlayer.hp) + " / " + str(maxhp) + " HP) - Combat Level " +
          str(myPlayer.level) + "\n")
    print("(" + str(Potions.lesser_heal) + ") Lesser Heal\n")
    print("(" + str(Potions.heal) + ") Heal\n")
    print("(" + str(Potions.greater_heal) + ") Greater Heal\n")
    print("(" + str(Potions.lesser_combat) + ") Lesser Combat\n")
    print("(" + str(Potions.combat) + ") Combat\n")
    print("(" + str(Potions.greater_combat) + ") Greater Combat\n")
    selection = input("> ")
    if selection.lower() == "use lesser heal" and Potions.lesser_heal > 0:
        Potions.lesser_heal = int(Potions.lesser_heal) - 1
        myPlayer.hp = int(myPlayer.hp) + int(maxhp) / 4
        lesserheal = int(maxhp) / 4
        print("Gained (" + str(lesserheal) + ") Health Points")
    elif selection.lower() == "use heal" and Potions.heal > 0:
        Potions.heal = int(Potions.heal) - 1
        myPlayer.hp = int(myPlayer.hp) + int(maxhp) / 2
        heal = int(maxhp) / 2
        print("Gained (" + str(heal) + ") Health Points")
    elif selection.lower() == "use greater heal" and Potions.greater_heal > 0:
        Potions.greater_heal = int(Potions.greater_heal) - 1
        myPlayer.hp = int(myPlayer.hp) + int(maxhp)
        greaterheal = int(maxhp)
        print("Gained (" + str(greaterheal) + ") Health Points")
    elif selection.lower() == "use lesser combat" and Potions.lesser_combat > 0:
        Potions.lesser_combat = int(Potions.lesser_combat) - 1
        xpbonus = random.randint(1, 5)
        assignment = random.randint(1, 2)
        if assignment == int(1):
            myPlayer.attack = int(myPlayer.attack) + int(xpbonus)
            print("Gained (" + str(xpbonus) + ") Attack Experience")
        elif assignment == int(2):
            myPlayer.defense = int(myPlayer.defense) + int(xpbonus)
            print("Gained (" + str(xpbonus) + ") Defense Experience")
    elif selection.lower() == "use combat" and Potions.combat > 0:
        Potions.combat = int(Potions.combat) - 1
        xpbonus = random.randint(5, 15)
        assignment = random.randint(1, 2)
        if assignment == int(1):
            myPlayer.attack = int(myPlayer.attack) + int(xpbonus)
            print("Gained (" + str(xpbonus) + ") Attack Experience")
        elif assignment == int(2):
            myPlayer.defense = int(myPlayer.defense) + int(xpbonus)
            print("Gained (" + str(xpbonus) + ") Defense Experience")
    elif selection.lower() == "use greater combat" and Potions.greater_combat > 0:
        Potions.greater_combat = int(Potions.greater_combat) - 1
        xpbonus = random.randint(15, 30)
        assignment = random.randint(1, 2)
        if assignment == int(1):
            myPlayer.attack = int(myPlayer.attack) + int(xpbonus)
            print("Gained (" + str(xpbonus) + ") Attack Experience")
        elif assignment == int(2):
            myPlayer.defense = int(myPlayer.defense) + int(xpbonus)
            print("Gained (" + str(xpbonus) + ") Defense Experience")
    elif selection.lower() == "exit":
        main_loop()
    else:
        print("please enter valid selection.\n")
        time.sleep(3)
        use_item()
    if int(myPlayer.hp) >= maxhp:
        myPlayer.hp = maxhp
    time.sleep(1.5)
    use_item()


def next_boss():
    if myPlayer.level == 2:
        fight(sadisticSpider)
    elif myPlayer.level == 3:
        fight(wickedWyvern)
    elif myPlayer.level == 4:
        fight(wiseOldMan)
    elif myPlayer.level == 5:
        fight(nightmare)


def main_loop():
    os.system('clear')
    print('############################')
    print('######## dwoofScape ########')
    print('############################')
    print('        -- Train --         ')
    print('       -- Use Item --       ')
    print('        -- Stats --         ')
    print('  -- Continue Down Path --  ')
    print('      Created By: dwoof     ')
    userchoice = input("> ")
    if userchoice.lower() == "train":
        train()
    elif userchoice.lower() == "use item":
        use_item()
    elif userchoice.lower() == "stats":
        stats()
    elif userchoice.lower() == "continue down path":
        next_boss()
    while userchoice.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        userchoice = input("> ")
        if userchoice.lower() == "train":
            train()
        elif userchoice.lower() == "use item":
            use_item()
        elif userchoice.lower() == "stats":
            stats()
        elif userchoice.lower() == "continue down path":
            next_boss()


def death_screen():
    os.system('clear')
    print("You Lose")
    input("Press Enter to exit...")
    sys.exit()


def win_screen():
    os.system('clear')
    print("You Win!")
    input("Press Enter to Return to Main Menu...")
    title_screen()


# Game Begins #
while int(myPlayer.hp) > 0:
    title_screen()
    goblin_defeated()
    main_loop()

