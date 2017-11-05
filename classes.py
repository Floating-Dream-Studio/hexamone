
class Player:
    def __init__(self):
        self.hexamone = Hexamone()

    def attack(self, spell, target):
        damage = self.hexamone.spells[spell]
        target.hexamone.hp -= damage


class Pnj:
    def __init__(self):
        self.hexamone = Hexamone()
        

class Hexamone:
    def __init__(self):
        self.name = "pika"
        self.hp = 10
        self.atk = 10
        self.spells = {
            'a' : 12,
            'z' : 5,
            'e' : 4,
            'r' : 3
        }
