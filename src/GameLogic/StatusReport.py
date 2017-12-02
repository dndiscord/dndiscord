from src.GameLogic.GenericGameLogic import GenericGameLogic


class StatusReport(GenericGameLogic):
    def __init__(self, print_method, data):
        super().__init__(print_method, data)

    async def print_current_statuses(self, message):
        print('here')
        await self.printMethod(message.channel, "Your environment: \n{}"
                               .format("".join(["name: {}\ndescription: {}\nhealth: {}\n-------------------"
                                               .format(i.name, i.description, i.health)
                                                for i in self.data.current_scenario])))
