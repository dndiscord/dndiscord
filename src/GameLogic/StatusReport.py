from src.GameLogic.GenericGameLogic import GenericGameLogic


class StatusReport(GenericGameLogic):
    def __init__(self, print_method, data):
        super().__init__(print_method, data)

    async def print_current_statuses(self, message):
        await self.printMethod(message.channel, "Your environment: \nYou are in {}\n{}"
                               .format(
                                   self.data.current_room.describe(),
                                   "".join(["-------------------\nname: {}\ndescription: {}\nhealth: {}\n"
                                               .format(i.name, i.description, i.health)
                                                for i in self.data.current_room.objects])))

    async def print_my_status(self,message):
        character = self.data.get_character_by_user(message.author.name)
        await self.printMethod(message.channel, "Description:\n{}\nInventory:\n{}"
                                   .format(character.description, "".join(["name: {}, description: {}\n".format(i.name,i.description) for i in character.inventory])))
