import requests
import random


banned_cards_endpoint = "https://db.ygoprodeck.com/api/v7/cardinfo.php?banlist=tcg&sort=name"

endpoint = "https://db.ygoprodeck.com/api/v7/cardinfo.php?sort=name"

endp = "https://db.ygoprodeck.com/api/v7/cardinfo.php?sort=name&id="

response = requests.get(f"{endpoint}")
result = response.json()

response2 = requests.get(f"{endp}")
result2 = response.json()



all_monster_cards = []
all_spell_cards = []
all_trap_cards = []
def random_main_deck():
    for b in result["data"]:
        if b["type"] != "Pendulum Effect Monster" and\
                b["type"] != "Pendulum Flip Effect Monster" and\
                b["type"] != "Pendulum Normal Monster" and\
                b["type"] != "Pendulum Tuner Effect Monster" and\
                b["type"] != "Link Monster" and\
                b["type"] != "Synchro Monster" and\
                b["type"] != "Synchro Pendulum Effect Monster" and\
                b["type"] != "Synchro Tuner Monster" and\
                b["type"] != "XYZ Monster" and\
                b["type"] != "XYZ Pendulum Effect Monster" and\
                b["type"] != "Fusion Monster" and\
                b["type"] != "Spell Card" and\
                b["type"] != "Trap Card" and\
                b["type"] != "Token" and\
                b["type"] != "Skill Card":
                all_monster_cards.append(b["id"])
    return all_monster_cards

def random_traps():
    for b in result["data"]:
        if b["type"] == "Trap Card":
                all_trap_cards.append(b["id"])
    return all_trap_cards

def random_spells():
    for b in result["data"]:
        if b["type"] == "Spell Card":
                all_spell_cards.append(b["id"])
    return all_spell_cards


with open("C:/Yu-Gi-Oh! The Dawn of a New Era/YGOPRO/deck/random.ydk", "w") as f:
    f.write("#created by ...\n")
    f.write("#main\n")
    for d in range(0, 20):
        f.write(str(random.choice(random_main_deck())))
        f.write("\n")

    for d in range(0, 10):
        f.write(str(random.choice(random_spells())))
        f.write("\n")

    for d in range(0, 10):
        f.write(str(random.choice(random_traps())))
        f.write("\n")

    f.write("#extra\n")
    f.write("!side")




