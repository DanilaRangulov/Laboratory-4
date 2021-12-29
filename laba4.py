# This is class space of Dota 2
# Drow Ranger and Monkey King - heroes with attributes who define a damage,health
class AttributeAgility:
    strength = 50
    agility = 70
    intelligence = 50


class AttributeIntelligence:
    strength = 50
    agility = 30
    intelligence = 70


class AttributeStrength:
    strength = 70
    agility = 30
    intelligence = 45
# Heroes who have main attribute: Strength


class HeroStrength(AttributeStrength):

    def __init__(self, type_attack, item1, item2, item3, item4, item5, item6):
        item_strength = (item1.item_strength + item2.item_strength + item3.item_strength +
                         item4.item_strength + item5.item_strength + item6.item_strength)
        item_net_damage = (item1.item_net_damage + item2.item_net_damage + item3.item_net_damage
                           + item4.item_net_damage + item5.item_net_damage + item6.item_net_damage)
        self.health = self.strength * 10 + item_strength * 10
        if type_attack == "Range":
            self.damage = self.strength * 0.85 + item_strength * 0.85 + item_net_damage
        else:
            self.damage = self.strength * 1.25 + item_strength * 0.85 + item_net_damage

# Damage get mechanics
    def get_damage(self, damage):
        self.health -= damage

# Item buying mechanics
    def buy_item(self, buying_item):
        if self.money > buying_item.coast:
            self.damage += buying_item.item_strength + buying_item.item_net_damage
            self.health += buying_item.item_strength
# Heroes who have main attribute: Intelligence


class HeroIntelligence(AttributeIntelligence):

    def __init__(self, type_attack, item1, item2, item3, item4, item5, item6):
        item_strength = (item1.item_strength + item2.item_strength + item3.item_strength +
                         item4.item_strength + item5.item_strength + item6.item_strength)
        item_damage_attributes = (item1.item_intelligence + item2.item_intelligence + item3.item_intelligence
                                  + item4.item_intelligence + item5.item_intelligence + item6.item_intelligence)
        item_net_damage = (item1.item_net_damage + item2.item_net_damage + item3.item_net_damage
                           + item4.item_net_damage + item5.item_net_damage + item6.item_net_damage)
        self.health = self.strength * 10 + item_strength * 10
        if type_attack == "Range":
            self.damage = self.intelligence * 0.85 + item_damage_attributes * 0.85 + item_net_damage
        else:
            self.damage = self.intelligence * 1.25 + item_damage_attributes * 0.85 + item_net_damage

    def get_damage(self, damage):
        self.health -= damage

    def buy_item(self, buying_item):
        if self.money > buying_item.coast:
            self.damage += buying_item.item_intelligence + buying_item.item_net_damage
            self.health += buying_item.item_strength
# Heroes who have main attribute: Agility


class HeroAgility(AttributeAgility):

    def __init__(self, type_attack, item1, item2, item3, item4, item5, item6, money):
        self.money = money
        item_strength = (item1.item_strength + item2.item_strength + item3.item_strength +
                         item4.item_strength + item5.item_strength + item6.item_strength)
        item_damage_attributes = (item1.item_agility + item2.item_agility + item3.item_agility +
                                  item4.item_agility + item5.item_agility + item6.item_agility)
        item_net_damage = (item1.item_net_damage + item2.item_net_damage + item3.item_net_damage
                           + item4.item_net_damage + item5.item_net_damage + item6.item_net_damage)
        self.health = self.strength * 10 + item_strength * 10
        if type_attack == "Range":
            self.damage = self.agility * 0.85 + item_damage_attributes * 0.85 + item_net_damage
        else:
            self.damage = self.agility * 1.25 + item_damage_attributes * 1.25 + item_net_damage

    def get_damage(self, damage):
        self.health -= damage

    def buy_item(self, buying_item):
        if self.money > buying_item.coast:
            self.damage += buying_item.item_agility + buying_item.item_net_damage
            self.health += buying_item.item_strength

# Class of items who have attributes


class Item:

    def __init__(self, name, item_strength, item_agility, item_intelligence, item_net_damage, coast):
        self.name = name
        self.item_strength = item_strength
        self.item_agility = item_agility
        self.item_intelligence = item_intelligence
        self.item_net_damage = item_net_damage
        self.coast = coast

    def ability(self, hero):
        hero.health -= self.item_net_damage * 1.5


class NeutralItem(Item):

    def ability(self, hero):
        hero.health += self.item_net_damage * 2


# Empty item slot
null = Item("Null", 0, 0, 0, 0, 0)
# Adding items
item_horn = NeutralItem("Horn", 0, 0, 0, 10, 130)
item_blade = Item("QuelienBlade", 0, 0, 0, 10, 130)
item_circlet = Item("Circlet", 2, 2, 2, 0, 155)
item_slippers_of_agility = Item("Slippers of Agility", 3, 0, 0, 0, 140)
item_iron_branch = Item("Iron Branch", 1, 1, 1, 0, 50)
item_mantle_of_intelligence = Item("Mantle of Intelligence", 0, 0, 3, 0, 140)
# Create a heroes
DrowRanger = HeroAgility("Range", item_blade, null, null, null, null, null, 600)
Monkey_King = HeroAgility("Melee", item_blade, item_circlet, item_iron_branch, item_iron_branch,
                          item_iron_branch, item_slippers_of_agility, 600)
# Buying an item for Drow Ranger
print(DrowRanger.damage)
DrowRanger.buy_item(item_circlet)
print(DrowRanger.damage)
# Drow Ranger has been attacked by Monkey King
print(DrowRanger.health)
DrowRanger.get_damage(Monkey_King.damage)
print(DrowRanger.health)
