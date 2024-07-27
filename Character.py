class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage and has {self.health} health remaining.")

    def attack_target(self, target):
        damage = self.attack - target.defense
        if damage > 0:
            target.take_damage(damage)
        else:
            print(f"{self.name}'s attack is too weak to harm {target.name}.")

    def is_alive(self):
        return self.health > 0

    def display_status(self):
        print(f"{self.name} - Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}")
