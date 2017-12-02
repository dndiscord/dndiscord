from src import Constants, Data
from src.GameLogic.GenericGameLogic import GenericGameLogic
from src.Objects.Character import Character
from src.Objects.Item import Item


class CreateCharacter(GenericGameLogic):
    def __init__(self, print_method, data):
        super().__init__(print_method, data)

    def getMessage(self, message):
        if message.content == "testing":
            self.assign_stats("carlos", "human", "drunk")

    def assign_stats(self, name, race, occupation):
        hp = 120
        spd = 15
        attk = 10
        mp = 15
        crt = 2
        value = 500

        if race == 'elf': 
            spd += 10
            attk += 5
            mp +=10
            crt +=2
            items = [Item({
                Constants.name: "Bow",
                Constants.description: "A simple wooden bow",
                Constants.value: 100,
                Constants.effect: "shoot",
                Constants.health: 200
            })]
       
        elif race == 'dwarf':
            spd -= 5
            hp += 90
            mp -= 5
            item = Item({
                Constants.name: "Hammer",
                Constants.description: "A hammer that weighs almost as much as a cow",
                Constants.value: 100,
                Constants.effect: "pound",
                Constants.health: 200
            })
 
        elif race == 'troll':
            hp += 90
            attk += 10
            spd -= 10
            mp -=15
            item = [Item({
                Constants.name: "Club",
                Constants.description: "A massive club that looks like an uprooted tree",
                Constants.value: 100,
                Constants.effect: "smash",
                Constants.health: 200
            })]
            
        elif race == 'gnome':
            hp -=20
            spd +=20
            attk += 5
            crt+=5
            items = [Item({
                Constants.name: "Spear",
                Constants.description: "A basic spear",
                Constants.value: 80,
                Constants.effect: "impale",
                Constants.health: 200
            })]
 
        elif race == 'human':
            hp += 20
            attk +=10
            mp +=5
            spd +=5
            items = [Item({
                Constants.name: "Sword",
                Constants.description: "A simple sword",
                Constants.value: 100,
                Constants.effect: "slash",
                Constants.health: 200
            }), Item({
                Constants.name: "Shield",
                Constants.description: "A simple shield",
                Constants.value: 50,
                Constants.effect: "block",
                Constants.health: 500
            })
            ]
            
        if occupation == 'thief':
            spd += 10
            hp -=10
            attk += 5
            crt +=1

        elif occupation == 'smith':
            hp += 20
        
        elif occupation == 'drunk':
            attk -= 4
            crt += 4
        elif occupation == 'librarian':
            hp += 5
            mp += 10

        elif occupation == 'hunter':
            attk += 5
            crt +=5

        descript = "You are " + name + " the " + race + " " + occupation + "."
        characterDict = {Constants.health: hp,
                         Constants.value: value,
                         Constants.attack: attk,
                         Constants.speed: spd,
                         Constants.mana: mp,
                         Constants.crit:crt,
                         Constants.name:name,
                         Constants.description: descript,
                         Constants.inventory: items
                         }
        newCharacter = Character(characterDict)
        self.data.add_character(newCharacter)
        self.data.gamestage = Data.GameStage.MOVE





