from src.GameLogic.GenericGameLogic import GenericGameLogic


class FightCycle(GenericGameLogic):
    def __init__(self, printMethod, data):
        super().__init__(printMethod,data)
        self.turn_order = None
        self.current_character = None
        self.index = 0

    async def getMessage(self, message, actionPrompt):
        if not message.author.name == self.current_character.user:
            await self.printMethod(message.channel, "WAIT YOUR TURN")
            return
        await actionPrompt.do_action(message)
        await self.end_turn(message)

    async def end_turn(self, message):
        self.index = (self.index + 1) % (len(self.turn_order))
        self.current_character = self.turn_order[self.index]
        await self.printMethod(message.channel, "It is now {}'s turn".format(self.current_character.name))
        if self.current_character.is_npc():
            await self.printMethod(message.channel, self.current_character.do_combat())
            await self.end_turn(message)

    async def start_cycle(self, message):
        # Init the fight
        self.index = 0
        self.turn_order = sorted(self.data.get_characters_from_current_room(),
                                 key=lambda c: c.speed, reverse=True)
        self.current_character = self.turn_order[self.index]
        await self.printMethod(message.channel, "The fight is on between {} and {}"
                         .format(", ".join([c.name for c in self.data.get_player_characters_from_current_room()])
                                 ,", ".join([c.name for c in self.data.get_npcs_from_current_room()])))
        if self.current_character.is_npc():
            await self.printMethod(message.channel, self.current_character.do_combat())

