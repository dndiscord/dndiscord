from src.GameLogic.GenericGameLogic import GenericGameLogic


class CharacterAction(GenericGameLogic):
    def __init__(self, print_method, data):
        super().__init__(print_method, data)

    async def do_action(self, message):
        input_components = message.content.split(' ')
        hero_name = input_components[0].split(':')[1]
        item_name = message.content.split[1]
        character = self.data.get_character(hero_name)
        if character is None:
            await self.printMethod(message.channel, "{} does not exist!".format(hero_name))
            return
        item = next(iter([i for i in character.inventory if i.name == item_name] or []),None)
        if item is None:
            await self.printMethod(message.channel, "{} does not have a {}!".format(hero_name, item_name))
            return
        await self.printMethod(message.channel, item.activate(character, True))

