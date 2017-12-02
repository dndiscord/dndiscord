from src import Constants


class GenericObject:
    # assign value, health, name, description
    def __init__(self,objectconfig):
        self.name = objectconfig[Constants.name]
        self.description = objectconfig[Constants.description]
        self.value = objectconfig[Constants.value]
