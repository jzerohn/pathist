class ArmorClass:

    def __init__ (self, armor_bonus = 0, shield_bonus = 0, dexterity_modifier = 0, enhancement_bonus = 0, deflection_bonus = 0, natural_armor = 0, dodge_bonus = 0, size_bonus = 0, other = 0):
        if armor_bonus < 0 or shield_bonus < 0 or dexterity_modifier < 0 or enhancement_bonus < 0 or deflection_bonus < 0 or natural_armor < 0 or dodge_bonus < 0 or size_bonus < 0 or other < 0:
            raise ValueError('bonus must be at least zero')

        self._ac = None
        self._flat_footed = None
        self._touch = None
        
        self.update_armor(armor_bonus, shield_bonus, dexterity_modifier, enhancement_bonus, deflection_bonus, natural_armor, dodge_bonus, size_bonus, other)

    @property
    def ac(self):
        return self._ac

    @property
    def flat_footed(self):
        return self._flat_footed

    @property
    def touch(self):
        return self._touch

    def update_armor(self, armor_bonus = 0, shield_bonus = 0, dexterity_modifier = 0, enhancement_bonus = 0, deflection_bonus = 0, natural_armor = 0, dodge_bonus = 0, size_bonus = 0, other = 0):
        self._ac = 10 + armor_bonus + shield_bonus + dexterity_modifier + enhancement_bonus + deflection_bonus + natural_armor + dodge_bonus + size_bonus + other
        self._flat_footed = 10 + armor_bonus + shield_bonus + enhancement_bonus + deflection_bonus + natural_armor + dodge_bonus + size_bonus + other
        self._touch = 10 + dexterity_modifier + enhancement_bonus + deflection_bonus + dodge_bonus + size_bonus + other