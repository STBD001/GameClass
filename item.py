class Item:
    def __init__(self, name, item_type, effect):
        self.name = name
        self.item_type = item_type
        self.effect = effect

    def use(self, target):
        print(f"{target.name} uses {self.name}. Effect: {self.effect}")
