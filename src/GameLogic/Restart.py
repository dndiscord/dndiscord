from src.GameLogic.GenericGameLogic import GenericGameLogic


class Restart(GenericGameLogic):
    def __init__(self, print_method, data):
        super.__init__(print_method, data)

    def restart(self):
        self