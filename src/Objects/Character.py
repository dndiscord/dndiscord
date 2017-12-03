from src import Constants
from src.Objects.GenericObject import GenericObject


class Character(GenericObject):
    def __init__(self, characterconfig):
        super().__init__(characterconfig)
        self.crit = characterconfig[Constants.crit]
        self.speed = characterconfig[Constants.speed]
        self.mana = characterconfig[Constants.mana]
        self.user = characterconfig[Constants.user]

    def receive(self, change):
        baseResult = super().receive(change)
        if isinstance(baseResult, list):
            # Return the loot
            return baseResult
        #Handle peaceful interactions with other characters

    def use_item(self, item, target, action, data):
        # Result contains a payload of data to apply to the target
        result = item.activate(self, True)
        result[Constants.action] = action
        maybe_loot = target.receive(result)
        if maybe_loot is not None:
            self.inventory.extend(maybe_loot)
        return result[Constants.description]

    # Non item use, already validated for character vs object
    def use_target(self, target, action, data):
        if action == Constants.trade:
            target.receive({})
        elif action == Constants.take:
            event_description = "{} took the {}".format(self.name, target.name)
            object = target.receive({Constants.attack: 0, Constants.effect: None, Constants.action: action,
                                     Constants.description: event_description})
            self.inventory.append(object)
            data.current_room.objects = [o for o in data.current_room.objects if o.name is not object.name]
            return event_description

