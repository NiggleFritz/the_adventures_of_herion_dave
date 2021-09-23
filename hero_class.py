class Hero:
    def __init__(self, hero_health, hero_damage, hero_luck, hero_ranged, hero_defence, hero_magic, hero_name):
        self.health = hero_health
        self.attack = hero_damage
        self.luck = hero_luck
        self.ranged = hero_ranged
        self.defence = hero_defence
        self.magic = hero_magic
        self.name = hero_name

    # we're gonna get setters and getters
    # These are getters, where we can check the health or attack of the character
    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_luck(self):
        return self.luck

    def get_ranged(self):
        return self.ranged

    def get_defence(self):
        return self.defence

    def get_magic(self):
        return self.magic

    def get_name(self):
        return self.name

    # setters is what we can use to change a variable
    # for example if we want to set a new attack value
    def set_health(self, new_health):
        self.health = new_health

    def set_attack(self, new_attack):
        self.attack = new_attack

    def set_luck(self, new_luck):
        self.luck = new_luck

    def set_ranged(self, new_ranged):
        self.ranged = new_ranged

    def set_defence(self, new_defence):
        self.defence = new_defence

    def set_magic(self, new_magic):
        self.magic = new_magic
