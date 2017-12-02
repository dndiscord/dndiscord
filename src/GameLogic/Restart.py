from src.GameLogic.GenericGameLogic import GenericGameLogic


class Restart(GenericGameLogic):
    def __init__(self, userCommunication, data):
        super.__init__(userCommunication, data)

    def restart(self):
        self