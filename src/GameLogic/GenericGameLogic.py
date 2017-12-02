class GenericGameLogic:
    def __init__(self, userCommunication, data):
        self.printMethod = userCommunication
        self.data = data

    async def print_message(self, message):
        self.printMethod(message)
