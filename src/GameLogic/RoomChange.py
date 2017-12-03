from src.GameLogic.GenericGameLogic import GenericGameLogic
from src.Space import Door

class RoomChange(GenericGameLogic):
    def __init__(self, print_method, data):
        super().__init__(print_method, data)

    async def parse_action(self, message):
        text = message.content
        user = message.author.name
        argv = text.split()
        if len(argv) == 1:
            await self.printMethod(message.channel, "Please specify something to do with the party.")
        else:
            interact_with = " ".join(argv[1:])
            await self.do_action(message, interact_with)

    async def do_action(self, message, action):
        room = self.data.current_room
        obj = [obj for obj in room.objects if obj.name == action]
        if len(obj) == 0:
            await self.printMethod(message.channel, "Couldn't find that object.")
            return
        obj = obj[0]
        if not isinstance(obj, Door):
            await self.printMethod(message.channel, "The party is unsure of how to collectively act towards that object.")
            return
        door = obj

        if door.locked:
            await self.printMethod(message.channel, "That door is locked. Use the key on it first.")
            return

        characters = self.data.get_player_characters_from_current_room()
        self.data.current_room.objects = [x for x in self.data.current_room.objects if x not in characters]
        self.data.current_room = door.other_side(self.data.current_room)
        self.data.current_room.objects.extend(characters)
        door.update_desc(self.data.current_room)
        await self.printMethod(message.channel, "The party is now in {}.".format(self.data.current_room.desc))


