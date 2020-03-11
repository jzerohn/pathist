from pathist.common.abilities_enum import CoreAbility

def ac_size_modifier(size):
    if not isinstance(size, str):
        raise ValueError('size must be a string indicating size class')

    switch = {"Colossal": -8,
        "Gargantuan": -4,
        "Large": -1,
        "Medium": 0,
        "Small": 1,
        "Tiny": 2,
        "Diminutive": 4,
        "Fine": 8
    }

    return switch.get(size, None)

def stat_from_core_ability(core_ability):
    if not isinstance(core_ability, CoreAbility):
        raise TypeError('core_ability must be of class CoreAbility')

    switch = {
        CoreAbility.ST: "STR",
        CoreAbility.KO: "CON",
        CoreAbility.GE: "DEX",
        CoreAbility.IN: "INT",
        CoreAbility.WI: "WIS",
        CoreAbility.CH: "CHA"
    }

    return switch.get(core_ability, None)