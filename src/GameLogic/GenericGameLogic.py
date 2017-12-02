class GenericGameLogic:
    def __init__(self, print_method, data):
        self.printMethod = print_method
        self.data = data

    async def print_message(self, message):
        self.printMethod(message)
