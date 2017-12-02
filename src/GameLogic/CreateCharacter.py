from src import Constants, Data
from src.GameLogic.GenericGameLogic import GenericGameLogic
from src.Objects.Character import Character
from src.Objects.Item import Item


class CreateCharacter(GenericGameLogic):
    def __init__(self, print_method, data):
        super().__init__(print_method, data)
        self.traits = {}

    def configured(self, user, trait):
        return user in self.traits.keys() and trait in self.traits[user].keys()

    async def getMessage(self, message):
        text = message.content
        user = message.author.name
        # if text == "testing":
        #     self.assign_stats("carlos", "human", "drunk")
        if not self.configured(user, 'name'):
            self.traits[user] = {}
            self.traits[user]['name'] = text
            await self.printMethod(message.channel, "{}, enter your character's race: (elf, human, dwarf, troll, gnome)".format(user))

        elif not self.configured(user, 'race'):
            if text == "elf" or text == "dwarf" or text == "human" or text == "gnome" or text == "troll":
                self.traits[user]['race'] = text
                await self.printMethod(message.channel,
                                       "{}, enter your character's occupation (thief, librarian, hunter, smith, drunk)".format(user))

        elif not self.configured(user, 'occupation'):
            if text == "drunk" or text == "smith" or text == "hunter" or text == "librarian" or text == "thief":
                self.traits[user]['occupation'] = text
                current_user = self.traits[user]
                await self.printMethod(message.channel, "{}, you are {}, the {} {}."
                                       .format(user, current_user['name'], current_user['race'], current_user['occupation']))
                self.assign_stats(current_user['race'], current_user['occupation'], current_user['name'])
                self.data.gamestage = Data.GameStage.MOVE

    def assign_stats(self,race,occupation, name):
        hp = 120
        spd = 15
        attk = 10
        mp = 15
        crt = 2
        value = 500

        if race == 'elf':
            spd += 10
            attk += 5
            mp += 10
            crt += 2
            items = [Item({
                Constants.name: "Bow",
                Constants.description: "A simple wooden bow",
                Constants.value: 100,
                Constants.effect: "shoot",
                Constants.health: 200,
                Constants.attack: 50
            })]
       
        elif race == 'dwarf':
            spd -= 5
            hp += 90
            mp -= 5
            items = Item({
                Constants.name: "Hammer",
                Constants.description: "A hammer that weighs almost as much as a cow",
                Constants.value: 100,
                Constants.effect: "pound",
                Constants.health: 200,
                Constants.attack: 100
            })
 
        elif race == 'troll':
            hp += 90
            attk += 10
            spd -= 10
            mp -=15
            items = [Item({
                Constants.name: "Club",
                Constants.description: "A massive club that looks like an uprooted tree",
                Constants.value: 100,
                Constants.effect: "smash",
                Constants.health: 200,
                Constants.attack: 100
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
                Constants.health: 200,
                Constants.attack: 100
            })]
 
        elif race == 'human':
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
        print("here")
        characterDict = {Constants.health: hp,
                         Constants.value: value,
                         Constants.attack: attk,
                         Constants.speed: spd,
                         Constants.mana: mp,
                         Constants.crit: crt,
                         Constants.name: name,
                         Constants.description: descript,
                         Constants.inventory: items
                         }
        newCharacter = Character(characterDict)
        self.data.add_character(newCharacter)
        self.data.current_scenario.append(newCharacter)
        self.data.gamestage = Data.GameStage.MOVE





