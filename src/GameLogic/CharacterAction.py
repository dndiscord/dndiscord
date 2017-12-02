from src.GameLogic.GenericGameLogic import GenericGameLogic


class CharacterAction(GenericGameLogic):
    def __init__(self, print_method, data):
        super().__init__(print_method, data)

    async def do_action(self, message):
        hero_name = message.content.split(' ')[0].split(':')[1]
        await self.printMethod(message.channel, hero_name+" did something")

