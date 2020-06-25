class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
    
    def equip_weapon(self, weapon):
        self.health += weapon.health
        self.attack += weapon.attack

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

    def equip_weapon(self, weapon):
        self.health += weapon.health
        self.attack += weapon.attack
        self.defense += weapon.defense

    def loss(self, attack):
        self.health -= max(0, attack - self.defense)

class Vampire(Warrior):
        def __init__(self):
            super().__init__(health=40, attack=4)
            self.vampirism = 50
        
        def equip_weapon(self, weapon):
            self.health += weapon.health
            self.attack += weapon.attack
            self.vampirism += weapon.vampirism

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

    def equip_weapon(self, weapon):
        self.health += weapon.health
        self.attack += weapon.attack

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
    
        def equip_weapon(self, weapon):
            self.health += weapon.health
            self.attack += weapon.attack
            self.healing += weapon.heal_power

    def heal(self, teammate):
        if self.healing + teammate.health > globals()[type(teammate).__name__]().health:
            teammate.health = globals()[type(teammate).__name__]().health
        else:
            teammate.health += self.healing
    
class Warlord(Warrior):
    def __init__(self):
        super().__init__(health=100, attack=4)
        self.defense = 2

    def equip_weapon(self, weapon):
        self.health += weapon.health
        self.attack += weapon.attack
        self.defense += weapon.defense

    def loss(self, attack):
        self.health -= max(0, attack - self.defense)

def sub_fight(unit_0, unit_1, unit_2, unit_3):
    while 1:
        unit_1.hit(unit_2, unit_3)
        print(unit_2.health)
        if hasattr(unit_0, 'heal'):
            unit_0.heal(unit_1)
        if unit_2.health <= 0:
            return True
        unit_2.hit(unit_1, unit_0)
        print(unit_1.health)
        if hasattr(unit_3, 'heal'):
            unit_3.heal(unit_2)
        if unit_1.health <= 0:
            return False

def fight(unit_1, unit_2):
    return sub_fight(None, unit_1, unit_2, None)

class Army:
    def __init__(self):
        self.units = []
        self.army_list = []

    def add_units(self, unit_class, count):
        did_warlord_in_list = 0
        if unit_class == Warlord:
            if len(self.units) == 0:
                self.units.append(Warlord())
            else:
                for i in range(0, len(self.units)):
                    if type(self.units[i]).__name__ == 'Warlord':
                        did_warlord_in_list = 1
                if did_warlord_in_list == 0:
                    self.units.append(Warlord())
        else:
            for _ in range(count):
                self.units.append(unit_class())

    def check(self, army, type_warrior):
        for i in range(0, len(army)):
            if type(army[i]).__name__ == type_warrior:
                return True, i
        return False, i

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

    def move_units(self, army = None):
        if army is None:
            army = self.units
        chec, _ = Army().check(army, 'Warlord')
        if chec == False:
            return 0

        _, lord_ind = Army().check(army, 'Warlord')
        army.insert(len(army), army[lord_ind])
        army.pop(lord_ind)
        
        lancer_tf, lancer_ind = Army().check(army, 'Lancer')
        if lancer_tf == True:
            lancer_list = []
            for i in range(0, len(army)):
                lancer_list.append(type(army[i]).__name__)

            count = lancer_list.count('Lancer')
            c = 0
            for i in range(0, count):
                g = lancer_list.index('Lancer')
                lancer_list[g] = 'None'
                army[c], army[g] = army[g], army[c]
                c += 1
                
        if lancer_tf == False:
            for i in range(0, len(army)):
                if type(army[i]).__name__ != 'Warlord' and type(army[i]).__name__ != 'Healer':
                    warrior_ind = i 
                    break
            army[0], army[warrior_ind] = army[warrior_ind], army[0]

        healer_tf, _ = Army().check(army, 'Healer')
        if healer_tf == True:
            healer_list = []
            for i in range(0, len(army)):
                healer_list.append(type(army[i]).__name__)

            count = healer_list.count('Healer')
            c = 1
            for i in range(0, count):
                g = healer_list.index('Healer')
                healer_list[g] = 'None'
                army[c], army[g] = army[g], army[c]
                c += 1

class Battle:
    @staticmethod
    def fight(army_1, army_2):
        chec1, _ = Army().check(army_1.units, 'Warlord')
        if chec1 == True:
            army_1.move_units()
        chec2, _ = Army().check(army_2.units, 'Warlord')
        if chec2 == True:
            army_2.move_units()

        while army_1.is_alive and army_2.is_alive:
            first = army_1.first_alive_unit
            second = army_2.first_alive_unit
            first_0 = army_1.second_alive_unit
            second_0 = army_2.second_alive_unit 
            win = sub_fight(first_0, first, second, second_0)
            if first_0 == None:
                if first.is_alive == False:
                    chec1, _ = Army().check(army_1.units, 'Warlord')
                    if chec1 == True:
                        army_1.move_units()
            else:
                if first.is_alive == False or first_0.is_alive == False:
                    chec1, _ = Army().check(army_1.units, 'Warlord')
                    if chec1 == True:
                        army_1.move_units()

            if second_0 == None:
                if second.is_alive == False:
                    chec2, _ = Army().check(army_2.units, 'Warlord')
                    if chec2 == True:
                        army_2.move_units()
            else:
                if second.is_alive == False or second_0.is_alive == False:
                    chec2, _ = Army().check(army_2.units, 'Warlord')
                    if chec2 == True:
                        army_2.move_units()

        return army_1.is_alive
    @classmethod
    def straight_fight(cls, army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            for unit_1, unit_2 in zip(army_1.alive_units, army_2.alive_units):
                fight(unit_1, unit_2)
        return army_1.is_alive

class Weapon:
    def __init__(self, health=0, attack=0, defense=0, vampirism=0, heal_power=0):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power


class Sword(Weapon):
    def __init__(self):
        super().__init__(health=5, attack=2)

class Shield(Weapon):
    def __init__(self):
        super().__init__(health=20, attack=-1, defense=2)

class GreatAxe(Weapon):
    def __init__(self):
        super().__init__(health=-15, attack=5, defense=-2, vampirism=10)

class Katana(Weapon):
    def __init__(self):
        super().__init__(health=-20, attack=6, defense=-5, vampirism=50)

class MagicWand(Weapon):
    def __init__(self):
        super().__init__(health=30, attack=3, heal_power=3)


if __name__ == '__main__':
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Warrior, 2)
    army_1.add_units(Lancer, 2)
    army_1.add_units(Defender, 1)
    army_1.add_units(Warlord, 3)
    army_2.add_units(Warlord, 2)
    army_2.add_units(Vampire, 1)
    army_2.add_units(Healer, 5)
    army_2.add_units(Knight, 2)
    army_1.move_units()
    army_2.move_units()
    battle = Battle()
    print(battle.fight(army_1, army_2))