import random 
from src.Objects.Key import Key
from src import Constants

class Room:
    def __init__(self, data, parent=None):
        self.data = data
        self.populated = False
        self.desc = "unpopulated"
        self.exits = []
        self.items = []
        if parent is not None:
            self.exits.append(parent) # door back where we came from

    def populate(self):
        self._populate_inner(None, [])

    def _populate_inner(self, back, keys):
        num_exits = random.randint(1, 3)
        if num_exits > len(self.data.exit_names):
            return
        self.desc = random.sample(self.data.rooms, 1)[0]
        self.data.rooms.remove(self.desc)
        dirs = random.sample(self.data.exit_names, num_exits)
        for direction in dirs:
            self.data.exit_names.remove(direction)
        random.shuffle(dirs)
        for direction in dirs:
            exit = Exit(self, direction)
            self.exits.append(exit)
            key = Key(exit)
            keys.append(key)
            if random.random() > 0.5: # place key in adjacent room
                exit.dest._populate_inner(exit, keys)
            else: # place key here
                key = keys[0]
                del keys[0]
                key.room = self
                self.items.append(key)

    def describe(self):
        return self.desc + " with doors " + str(list(map(lambda x: x.direction, self.exits))) + " and keys " + str(list(map(lambda k: k.exit.direction, self.items)))

    def show(self):
        print(self.describe())
        for exit in self.exits:
            if exit.dest != self:
                exit.show()
                exit.dest.show()

class Exit:
    def __init__(self, src, direction):
        self.data = src.data
        self.src = src
        self.direction = direction
        self.dest = Room(src.data, self)

    def show(self):
        print("door named " + self.direction + " to " + self.dest.desc)
