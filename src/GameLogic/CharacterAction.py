from src import Constants
from src.GameLogic.GenericGameLogic import GenericGameLogic
from src.Objects.Character import Character


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
            await self.do_item_action(action, input_components[2], input_components[3], character, message.channel)
        else:
            await self.do_non_item_action(input_components[2], action, character, message.channel)

    async def do_item_action(self, action, item_name, target_name, character, channel):
        target = await self.get_target(target_name, channel)
        if target is None: return
        item = next(iter([i for i in character.inventory if i.name.lower() == item_name.lower()] or []), None)
        if item is None:
            await self.printMethod(channel, "{} does not have a {}!".format(character.name, item_name))
            return
        await self.printMethod(channel, character.use_item(item, target, action))

    async def get_target(self, name, channel):
        target = self.data.get_from_current_room(name)
        if target is None:
            await self.printMethod(channel, "{} does not exist!".format(name))
        return target

    async def do_non_item_action(self, name, action, character, channel):
        target = await self.get_target(name,channel)
        if target is None:
            return
        if action in Constants.action_vocabulary['non_item_use']['character_interact'] and not isinstance(target, Character):
            await self.printMethod(channel, "You can't {} with an inanimate object".format(action))
            return
        await self.printMethod(channel, character.use_person(target, action))


