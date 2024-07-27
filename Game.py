from Hero import Hero
from Monster import Monster

class Game:
    def __init__(self):
        self.hero = None
        self.monsters = []

    def create_hero(self, name):
        self.hero = Hero(name, 100, 10, 5)
        print(f"Hero {name} has been created!")

    def spawn_monster(self, name, health, attack, defense, monster_type, experience_value):
        monster = Monster(name, health, attack, defense, monster_type, experience_value)
        self.monsters.append(monster)
        print(f"A {monster_type} named {name} appears!")

    def play_turn(self):
        if self.hero and self.monsters:
            monster = self.monsters[0]
            self.hero.attack_target(monster)
            if not monster.is_alive():
                print(f"{monster.name} has been defeated!")
                self.hero.gain_experience(monster.experience_value)
                self.monsters.remove(monster)
            else:
                monster.attack_target(self.hero)
                if not self.hero.is_alive():
                    print(f"{self.hero.name} has been defeated! Game over.")
                    return False
        return True

    def start_game(self):
        self.create_hero("Archer")
        self.spawn_monster("Goblin", 50, 8, 3, "Goblin", 20)
        self.spawn_monster("Orc", 80, 12, 5, "Orc", 50)

        print("\n--- Game Start ---")
        while self.play_turn():
            continue
        print("--- Game Over ---")
