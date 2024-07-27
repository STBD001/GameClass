from Character import Character

class Hero(Character):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
        self.experience = 0
        self.inventory = []

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gains {amount} experience points. Total experience: {self.experience}.")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picks up {item}.")

    def display_inventory(self):
        print(f"{self.name}'s Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
