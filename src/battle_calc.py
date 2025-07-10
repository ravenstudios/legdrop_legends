import random

def damage(atk_power, attacker, defender):
    crit_flag = False
    print(f"atk_power:{atk_power}")
    print(f"attacker power:{attacker.power}")
    print(f"defender def:{defender.defense}")
    rdm = random.randint(1, 20)
    print(f"rdm:{rdm}")
    print(f"crit number needed:{20 - (attacker.luck // 10)}")
    crit = 1.5 if rdm >= (20 - attacker.luck // 10) else 1
    print(f"crit:{crit}")
    if crit > 1:
        crit_flag = True
    rps = get_type_bonus(attacker, defender)


    dmg = int((atk_power + (attacker.power - defender.defense)) * crit * rps)
    print(f"dmg dealt:{dmg}")
    return [dmg, crit_flag]



def get_type_bonus(attacker, defender):
    wins_against = {
        "brawler": "grappler",
        "grappler": "high-flyer",
        "high-flyer": "brawler"
    }

    if attacker.type_class == defender.type_class:
        return 1.0  # Neutral
    elif wins_against.get(attacker.type_class) == defender.type_class:
        return 1.5  # Super effective
    else:
        return 0.5  # Not very effective
