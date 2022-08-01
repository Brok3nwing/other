import requests
import random


endpoint = "https://db.ygoprodeck.com/api/v7/cardinfo.php?sort=name"
response = requests.get(f"{endpoint}")
result = response.json()


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

for count in range(0, 10):
    with open(f"C:/Yu-Gi-Oh! The Dawn of a New Era/YGOPRO/deck/random{count}.ydk", "w") as f:
        total_price = []
        f.write("#created by ...\n")
        f.write("#main\n")
        for d in range(0, 20):
            random_card = random.choice(random_main_deck())
            random_main_deck().remove(random_card)
            id_endpoint = "https://db.ygoprodeck.com/api/v7/cardinfo.php?id="+str(random_card)

            id_response = requests.get(f"{id_endpoint}")
            id_result = id_response.json()
            b = id_result["data"]
            price = float((b[0]["card_prices"][0]["tcgplayer_price"]))
            total_price.append(price)


            f.write(str(random_card))
            f.write("\n")

        for d in range(0, 10):
            random_card = random.choice(random_spells())
            random_spells().remove(random_card)
            id_endpoint = "https://db.ygoprodeck.com/api/v7/cardinfo.php?id="+str(random_card)

            id_response = requests.get(f"{id_endpoint}")
            id_result = id_response.json()
            b = id_result["data"]
            price = float((b[0]["card_prices"][0]["tcgplayer_price"]))
            total_price.append(price)
            f.write(str(random_card))
            f.write("\n")

        for d in range(0, 10):
            random_card = random.choice(random_traps())
            random_traps().remove(random_card)
            id_endpoint = "https://db.ygoprodeck.com/api/v7/cardinfo.php?id="+str(random_card)

            id_response = requests.get(f"{id_endpoint}")
            id_result = id_response.json()
            b = id_result["data"]
            price = float((b[0]["card_prices"][0]["tcgplayer_price"]))
            total_price.append(price)
            f.write(str(random_card))
            f.write("\n")

        f.write("#extra\n")
        f.write("!side")
        print(f"Random Deck Number {count} created with value {sum(total_price)}$")




