from src import Constants
from src.GameLogic.GenericGameLogic import GenericGameLogic


class CharacterAction(GenericGameLogic):
    def __init__(self, print_method, data):
        super().__init__(print_method, data)

    async def do_action(self, message):
        input_components = message.content.split(' ')
        hero_name = input_components[0].split(':')[1]
        character = self.data.get_character(hero_name)
        if character is None:
            await self.printMethod(message.channel, "Hero {} does not exist!".format(hero_name))
            return

        if input_components[1] == Constants.status:
            await self.printMethod(message.channel, "Description:\n{}\nInventory:\n{}"
                                   .format(character.description, "".join(["name: {}, description: {}\n".format(i.name,i.description) for i in character.inventory])))
            return

        item_name = input_components[1]
        target_name = input_components[2]
        target = self.data.get_from_current_scenario(target_name)
        item = next(iter([i for i in character.inventory if i.name == item_name] or []), None)
        if item is None:
            await self.printMethod(message.channel, "{} does not have a {}!".format(hero_name, item_name))
            return
        if target is None:
            await self.printMethod(message.channel, "{} does not exist!".format(target_name))
            return
        await self.printMethod(message.channel, character.use_item(item, target))
