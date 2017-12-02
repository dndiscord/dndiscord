from src.GameLogic.GenericGameLogic import GenericGameLogic


class CharacterAction(GenericGameLogic):
    def __init__(self, userCommunication, data):
        super().__init__(userCommunication, data)

    def do_action(self, content):
        hero_name = content.split(' ')[0].split(':')[1]
        self.print_message(hero_name+" did something")

