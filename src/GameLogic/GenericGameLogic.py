class GenericGameLogic:
    def __init__(self, print_method, data):
        self.printMethod = print_method
        self.data = data

    def print_message(self, channel, to_print):
        print("here 1")
        self.printMethod(channel, to_print)
