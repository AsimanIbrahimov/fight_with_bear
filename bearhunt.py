"""
----------------- Bear Hunting --------------------
1. Bear (500 HP) & Me (100 HP)
2. Sword (50HP). RedBull (+25-40HP)
3. Bear attacks randomly (7-15 HP).
5. If we hit:
Head (1.8x)
Hands (0.8x)
Body (x)
Heart (1.5x)
6. "You win!" title if you win else "Game Over! x_x"

Requirements. PEP-8, if __name__, helpers.py (utils)
Extras! Error Handling
----------------------------------------------------
"""

import random
from time import sleep
from os import system


NORMAL = {
    "Red": "\033[0;31;40m",
    "Green": "\033[0;32;40m",
    "Yellow": "\033[0;33;40m",
    "White": "\033[0;37;40m"
    }

DARK = {
    "Red": "\033[1;31;40m",
    "Green": "\033[1;32;40m",
    "White": "\033[1;37;40m",
}

    
print(f"{"-"*10}Bear Hunting game{"-"*10}")


BODY_PART_COEF= {
    "Head": 1.8,
    "Hand": 0.8,
    "Body": 1,
    "Heart": 1.5
}

body_part = list(BODY_PART_COEF.keys())
damages = [value for value in BODY_PART_COEF.values()]


def bear_body_damage_coef(coef):
	head_damage = coef[0]
	hand_damage = coef[1]
	body_damage = coef[2]
	heart_damage = coef[3]
	bear_coefs = head_damage, hand_damage, body_damage, heart_damage
    
	return bear_coefs


coefs = bear_body_damage_coef(damages)


def bear_attack():
    return random.randint(7, 25)

def player_attack():
    return random.choice(body_part)


def player_is_alive():
    return player_hp > 0


def bear_is_alive():
    return bear_hp > 0


def is_playable():
    return player_is_alive() and bear_is_alive()


def loading(time: int, message: str):
    dots = [x for x in range(5)]
    count = 0

    while count < (time*10):
        for d in dots:
            print(DARK["White"] + (message + "."*d) + NORMAL['White'])
            count += 1
            sleep(0.01)
            system("cls")


def congrats():
    time = 3
    while time > 0:
        for _ in range(4):
            print(DARK['Green'] + "You Won!" + NORMAL['White'])
            sleep(0.5)
            system("cls")
            time -= 1


def dead_message():
    time = 3
    while time > 0:
        for _ in range(4):
            print(F"\n{DARK['Red']}Game Over! x_x{NORMAL['White']}")
            sleep(0.5)
            system("cls")
            time -= 1


def main():
    global bear_hp, player_hp

    bear_hp = 500
    player_hp = 100


    while is_playable():
        print()
        print(f"{NORMAL['Red']}Bear hp: {NORMAL['White']}{bear_hp}")
        print(f"{NORMAL['Green']}Player hp: {NORMAL['White']}{player_hp}")
        print()

        action = input(f"{NORMAL['Yellow']}Press ENTER to attack or\nWrite 'redbull' to recover HP>> {NORMAL['White']} ").lower()
        

        if player_hp > 100:
            player_hp = 100
            print("Your health is full")


        if action == "":
            loading(2, "Attacking")
            location = player_attack()
            damage_multiply = random.choice(coefs)
            sword_damage = 50 * damage_multiply
            bear_hp -= sword_damage
            print(f"{NORMAL['Green']}You attacked bear's {location} for {DARK['Red']}{sword_damage} damage!{NORMAL['White']}")
        

            if bear_hp <= 0:
                congrats()
                break

            bear_damage = bear_attack()
            player_hp -= bear_damage
            print(f"{NORMAL['Red']}Bear dealed {DARK['Red']}{bear_damage} damage to you!{NORMAL['White']}")


            if player_hp <= 0:
                dead_message()
                break
            
            

        elif action == "redbull":
            loading(1, "Drinking redbull")
            player_hp += 50
            print("You drank redbull +50 hp")

        else:
            system("cls")
            print("Invalid action.Try again!")

    
    


if __name__ == "__main__":
    main()
