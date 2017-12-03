from src import Constants
from src.GameLogic.GenericGameLogic import GenericGameLogic


class CharacterAction(GenericGameLogic):
    def __init__(self, print_method, data):
        super().__init__(print_method, data)

    async def do_action(self, message):
        message.content.lower()
        input_components = message.content.split(' ')
        character = self.data.get_character_by_user(message.author.name)
        if character is None:
            await self.printMethod(message.channel, "Hero for {} does not exist!".format(message.author.name))
            return
        action = input_components[1]
        # If you need to use an action
        item_use_actions = Constants.action_vocabulary['item_use']['character_interact']
        item_use_actions.extend(Constants.action_vocabulary['item_use']['item_interact'])
        if action in item_use_actions:
            print("doing item action")
            await self.do_item_action(input_components, character, message)
        else:
            print("Nope")
            return

    async def do_item_action(self, input_components, character, message):
        item_name = input_components[2]
        target_name = input_components[3]
        target = self.data.get_from_current_room(target_name)
        item = next(iter([i for i in character.inventory if i.name.lower() == item_name.lower()] or []), None)
        if item is None:
            await self.printMethod(message.channel, "{} does not have a {}!".format(character.name, item_name))
            return
        if target is None:
            await self.printMethod(message.channel, "{} does not exist!".format(target_name))
            return
        await self.printMethod(message.channel, character.use_item(item, target))