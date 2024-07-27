from Character import Character

class Monster(Character):
    def __init__(self, name, health, attack, defense, monster_type, experience_value):
        super().__init__(name, health, attack, defense)
        self.monster_type = monster_type
        self.experience_value = experience_value

    def display_monster_type(self):
        print(f"{self.name} is a {self.monster_type}.")
