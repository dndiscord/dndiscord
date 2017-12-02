from src import Constants, Data
from src.GameLogic.GenericGameLogic import GenericGameLogic
from src.Objects.Character import Character
from src.Objects.Item import Item


class CreateCharacter(GenericGameLogic):
    def __init__(self, print_method, data):
        super().__init__(print_method, data)
        self.name = "default"
        self.race = "default"
        self.occupation = "default"

    async def getMessage(self, message):
        text = message.content
        # if text == "testing":
        #     self.assign_stats("carlos", "human", "drunk")
        if text.startswith('!credits'):
            await self.printMethod(message.channel, "Invalid command")
        elif self.name == "default":
            self.name = text
        elif self.race == "default":
            if text == "elf" or text == "dwarf" or text == "human" or text == "gnome" or text == "troll":
                self.race = text
        elif self.occupation == "default":
            if text == "drunk" or text == "smith" or text == "hunter" or text == "librarian" or text == "thief":
                self.occupation = text

        if self.name == "default":
            await self.printMethod(message.channel, "Enter your character's name:")
        elif self.race == "default":
            await self.printMethod(message.channel, "Enter your character's race: (elf, human, dwarf, troll, gnome)")
        elif self.occupation == "default":
            await self.printMethod(message.channel, "Enter your character's occupation (thief, librarian, hunter, smith, drunk)")
        else:
            await self.printMethod(message.channel, "You are " + self.name + " the " + self.race + " " + self.occupation + ".")
            self.assign_stats()
            self.data.gamestage = Data.GameStage.MOVE

    def assign_stats(self):
        hp = 120
        spd = 15
        attk = 10
        mp = 15
        crt = 2
        value = 500

        if self.race == 'elf':
            spd += 10
            attk += 5
            mp +=10
            crt +=2
            items = [Item({
                Constants.name: "Bow",
                Constants.description: "A simple wooden bow",
                Constants.value: 100,
                Constants.effect: "shoot",
                Constants.health: 200,
                Constants.attack:50
            })]
       
        elif self.race == 'dwarf':
            spd -= 5
            hp += 90
            mp -= 5
            item = Item({
                Constants.name: "Hammer",
                Constants.description: "A hammer that weighs almost as much as a cow",
                Constants.value: 100,
                Constants.effect: "pound",
                Constants.health: 200,
                Constants.attack: 100
            })
 
        elif self.race == 'troll':
            hp += 90
            attk += 10
            spd -= 10
            mp -=15
            item = [Item({
                Constants.name: "Club",
                Constants.description: "A massive club that looks like an uprooted tree",
                Constants.value: 100,
                Constants.effect: "smash",
                Constants.health: 200,
                Constants.attack: 100
            })]
            
        elif self.race == 'gnome':
            hp -=20
            spd +=20
            attk += 5
            crt+=5
            items = [Item({
                Constants.name: "Spear",
                Constants.description: "A basic spear",
                Constants.value: 80,
                Constants.effect: "impale",
                Constants.health: 200,
                Constants.attack: 100
            })]
 
        elif self.race == 'human':
            hp += 20
            attk += 10
            mp +=5
            spd +=5
            items = [Item({
                Constants.name: "Sword",
                Constants.description: "A simple sword",
                Constants.value: 100,
                Constants.effect: "slash",
                Constants.health: 200,
                Constants.attack: 20
            }), Item({
                Constants.name: "Shield",
                Constants.description: "A simple shield",
                Constants.value: 50,
                Constants.effect: "block",
                Constants.health: 500,
                Constants.attack: 10
            })
            ]
            
        if self.occupation == 'thief':
            spd += 10
            hp -=10
            attk += 5
            crt +=1

        elif self.occupation == 'smith':
            hp += 20
        
        elif self.occupation == 'drunk':
            attk -= 4
            crt += 4
        elif self.occupation == 'librarian':
            hp += 5
            mp += 10

        elif self.occupation == 'hunter':
            attk += 5
            crt +=5

        descript = "You are " + self.name + " the " + self.race + " " + self.occupation + "."
        print("here")
        characterDict = {Constants.health: hp,
                         Constants.value: value,
                         Constants.attack: attk,
                         Constants.speed: spd,
                         Constants.mana: mp,
                         Constants.crit: crt,
                         Constants.name: self.name,
                         Constants.description: descript,
                         Constants.inventory: items
                         }
        newCharacter = Character(characterDict)
        self.data.add_character(newCharacter)
        self.data.current_scenario.append(newCharacter)
        self.data.gamestage = Data.GameStage.MOVE





