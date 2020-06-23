class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, other, other2 = None):
        other.loss(self.attack)

    def loss(self, attack):
        self.health -= attack


class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)


class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3)
        self.defense = 2

    def loss(self, attack):
        self.health -= max(0, attack - self.defense)

class Vampire(Warrior):
        def __init__(self):
            super().__init__(health=40, attack=4)
            self.vampirism = 50
        
        def hit(self, other, other2 = None):
            other.loss(self.attack)
            if hasattr(other, 'defense'):
                self.health += (self.attack-other.defense) / 100 * self.vampirism
            else:
                self.health += self.attack / 100 * self.vampirism

class Lancer(Warrior):
    def __init__(self):
        super().__init__(health=50, attack=6)
        self.attack_1 = 100
        self.attack_2 = 50

    def hit(self, other1, other2):
        if other2 == None:
            other1.loss(self.attack / 100 * self.attack_1)
        else:
            other1.loss(self.attack / 100 * self.attack_1)
            other2.loss(self.attack / 100 * self.attack_2)

class Healer(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=0)
        self.healing = 2
    
    def heal(self, teammate):
        if self.healing + teammate.health > globals()[type(teammate).__name__]().health:
            teammate.health = globals()[type(teammate).__name__]().health
        else:
            teammate.health += self.healing
    

def sub_fight(unit_0, unit_1, unit_2, unit_3):
    while 1:
        unit_1.hit(unit_2, unit_3)
        if hasattr(unit_0, 'heal'):
            unit_0.heal(unit_1)
        if unit_2.health <= 0:
            return True
        unit_2.hit(unit_1, unit_0)
        if hasattr(unit_3, 'heal'):
            unit_3.heal(unit_2)
        if unit_1.health <= 0:
            return False

def fight(unit_1, unit_2):
    return sub_fight(None, unit_1, unit_2, None)

class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_class, count):
        for _ in range(count):
            self.units.append(unit_class())

    @property
    def first_alive_unit(self):
        for unit in self.units:
            if unit.is_alive:
                return unit
    @property
    def second_alive_unit(self):
        units_save = []
        units_save += self.units
        units_save.pop(units_save.index(self.first_alive_unit))
        for uni in units_save:
            if uni.is_alive:
                return uni

    @property
    def is_alive(self):
        return self.first_alive_unit is not None
    

    @property
    def alive_units(self):
        return [u for u in self.units if u.is_alive]

    def __len__(self):
        return len(self.units)


class Battle:
    @staticmethod
    def fight(army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            sub_fight(army_1.second_alive_unit, army_1.first_alive_unit, army_2.first_alive_unit, army_2.second_alive_unit)
        return army_1.is_alive
    @classmethod
    def straight_fight(cls, army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            for unit_1, unit_2 in zip(army_1.alive_units, army_2.alive_units):
                fight(unit_1, unit_2)
        return army_1.is_alive

        



if __name__ == '__main__':
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Lancer, 7)
    army_1.add_units(Vampire, 3)
    army_1.add_units(Warrior, 4)
    army_1.add_units(Defender, 2)
    army_2.add_units(Warrior, 4)
    army_2.add_units(Defender, 4)
    army_2.add_units(Vampire, 6)
    army_2.add_units(Lancer, 4)
    battle = Battle()
    print(battle.straight_fight(army_1, army_2))
        
