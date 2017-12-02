from src.GameLogic.GenericGameLogic import GenericGameLogic


class CharacterAction(GenericGameLogic):
    def __init__(self, print_method, data):
        super().__init__(print_method, data)

    def do_action(self, content):
        hero_name = content.split(' ')[0].split(':')[1]
        self.print_message(" did something")

