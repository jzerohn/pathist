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