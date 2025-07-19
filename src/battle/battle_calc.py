import random

def damage(atk_power, attacker, defender):
    crit_flag = False
    # print(f"atk_power:{atk_power}")
    # print(f"attacker power:{attacker.power}")
    # print(f"defender def:{defender.defense}")
    rdm = random.randint(1, 20)
    # print(f"rdm:{rdm}")
    # print(f"crit number needed:{20 - (attacker.luck // 10)}")
    crit = 1.5 if rdm >= (20 - attacker.luck // 10) else 1
    # print(f"crit:{crit}")
    flag = ""
    if crit > 1:
        crit_flag = "crit"
    rps = get_type_bonus(attacker, defender)
    # print(f"rps:{rps}")

    modifier = get_type_bonus(attacker, defender) * crit
    print(f"modifier:{modifier}")
    # dmg = int((atk_power + (attacker.power - defender.defense)) * crit * rps)
    dmg = int((((2 * attacker.level / 5 + 2) * attacker.power * ((atk_power * 5) / defender.defense)) / 50 + 2) * modifier)
    dodge_chance = (defender.speed - attacker.speed) * 0.01  # 1% per point difference
    rdm = random.random()
    if rdm < dodge_chance:
        dmg = 0
        flag = "dodge"
        print("dodge")
    # print(f"dmg dealt:{dmg}")
    hit_chance = get_hit_chance(attacker, defender)

    rdm = random.random()
    if rdm > hit_chance:
        dmg = 0
        # print("miss")
        flag = "miss"
        print(f"{attacker.name}'s attack missed!")
    variation = random.uniform(0.85, 1.00)  # Pokémon usually uses 0.85–1.00
    adjusted_power = int(dmg * variation)
    return [adjusted_power, crit_flag]

def get_hit_chance(attacker, defender):
    base_chance = 0.5  # 90% base chance to hit
    # speed_diff = defender.speed - attacker.speed
    dodge_modifier = attacker.technique * 0.007  # each point of speed changes hit chance by 0.5%
    final_chance = base_chance + dodge_modifier
    result = max(0.1, min(final_chance, 0.99))
    print(f"hit chance:{result}")
    return result  # clamp between 10% and 99%



def get_type_bonus(attacker, defender):
    wins_against = {
        "Brawler": "Grappler",
        "Grappler": "High Flyer",
        "High Flyer": "Brawler"
    }

    if attacker.type_class == defender.type_class:
        return 1.0
    elif wins_against.get(attacker.type_class) == defender.type_class:
        return 1.1
    else:
        return 0.9
