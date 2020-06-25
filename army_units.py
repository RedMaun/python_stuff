class Army:
    def __init__(self, armySolder = None, armyType = None, typeSwordsman = None, typeLancer = None, typeArcher = None):
        self.armySolder = armySolder
        self.armyType = armyType
        self.typeSwordsman = typeSwordsman
        self.typeLancer = typeLancer
        self.typeArcher = typeArcher

    def train_swordsman(self, nameSolder = None):
        objectArmy = Swordsman()
        objectArmy.nameSolder = nameSolder
        objectArmy.armySolder = self.armySolder 
        objectArmy.armyType = self.typeSwordsman 
        return objectArmy

    def train_lancer(self, nameSolder = None):
        objectArmy = Lancer()
        objectArmy.nameSolder = nameSolder
        objectArmy.armySolder = self.armySolder
        objectArmy.armyType = self.typeLancer
        return objectArmy

    def train_archer(self, nameSolder = None):
        objectArmy = Archer()
        objectArmy.nameSolder = nameSolder
        objectArmy.armySolder = self.armySolder
        objectArmy.armyType = self.typeArcher
        return objectArmy

class Swordsman:
    def __init__(self, typeSolder = 'swordsman', nameSolder = None, armySolder = None, armyType = None):
        self.typeSolder = typeSolder
        self.nameSolder = nameSolder
        self.armySolder = armySolder
        self.armyType = armyType
    def introduce(self):
        return self.armyType + ' ' + self.nameSolder + ', ' + self.armySolder + ' ' + self.typeSolder

class Lancer:
    def __init__(self, typeSolder = 'lancer', nameSolder = None, armySolder = None, armyType = None):
        self.typeSolder = typeSolder
        self.nameSolder = nameSolder
        self.armySolder = armySolder
        self.armyType = armyType
    def introduce(self):
        return self.armyType + ' ' + self.nameSolder + ', ' + self.armySolder + ' ' + self.typeSolder
        
class Archer:
    def __init__(self, typeSolder = 'archer', nameSolder = None, armySolder = None, armyType = None):
        self.typeSolder = typeSolder
        self.nameSolder = nameSolder
        self.armySolder = armySolder
        self.armyType = armyType
    def introduce(self):
        return self.armyType + ' ' + self.nameSolder + ', ' + self.armySolder + ' ' + self.typeSolder

class AsianArmy(Army):
    def __init__(self, armySolder = 'Asian', typeSwordsman = 'Samurai', typeLancer = 'Ronin', typeArcher = 'Shinobi'):
        self.armySolder = armySolder
        self.typeSwordsman = typeSwordsman
        self.typeLancer = typeLancer
        self.typeArcher = typeArcher

class EuropeanArmy(Army):
    def __init__(self, armySolder = 'European', typeSwordsman = 'Knight', typeLancer = 'Raubritter', typeArcher = 'Ranger'):
        self.armySolder = armySolder
        self.typeSwordsman = typeSwordsman
        self.typeLancer = typeLancer
        self.typeArcher = typeArcher


my_army = EuropeanArmy()
enemy_army = AsianArmy()

soldier_1 = my_army.train_swordsman("Jaks")
soldier_2 = my_army.train_lancer("Harold")
soldier_3 = my_army.train_archer("Robin")

soldier_4 = enemy_army.train_swordsman("Kishimoto")
soldier_5 = enemy_army.train_lancer("Ayabusa")
soldier_6 = enemy_army.train_archer("Kirigae")



soldier_1.introduce() == "Knight Jaks, European swordsman"
soldier_2.introduce() == "Raubritter Harold, European lancer"
soldier_3.introduce() == "Ranger Robin, European archer"
    
soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
soldier_6.introduce() == "Shinobi Kirigae, Asian archer"


