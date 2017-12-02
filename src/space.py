import random
import copy

from src.Objects.Key import Key
from src import Constants

class Room:
    def __init__(self, data, parent=None):
        self.data = data
        self.populated = False
        self.desc = "UNPOPULATED"
        self.exits = []
        self.items = []
        self.parent = parent
        if parent is not None:
            self.exits.append(parent) # door back where we came from

    def populate(self):
        num_exits = random.randint(min(1, len(self.data.exit_names)), min(3, len(self.data.exit_names)))
        if len(self.data.rooms) == 0:
            return
        self.desc = random.sample(self.data.rooms, 1)[0]
        self.data.rooms.remove(self.desc)
        dirs = random.sample(self.data.exit_names, num_exits)
        for name in dirs:
            self.data.exit_names.remove(name)
        for name in dirs:
            exit = Exit(self, name, random.random() > 0.5)
            exit.dest.populate()
            self.exits.append(exit)

    def describe(self):
        return self.desc + " with doors " + str(list(map(lambda x: x.desc(), self.exits))) + " and keys " + str(list(map(lambda k: k.exit + " key", self.items)))

    def show(self):
        print(self.describe())
        for exit in self.exits:
            if exit.dest != self:
                exit.show()
                exit.dest.show()

class Exit:
    def __init__(self, src, name, locked):
        self.locked = locked
        self.data = src.data
        self.src = src
        self.name = name
        self.dest = Room(src.data, self)

    def desc(self):
        return ["unlocked ", "locked "][int(self.locked)] + self.name + " door"

    def show(self):
        print("door named " + self.name + " to " + self.dest.desc)

def reachable_rooms(room, keys):
    reached = [room]
    for exit in room.exits:
        if exit.name in map(lambda k: k.exit, keys):
            if exit.dest != room:
                reached.extend(reachable_rooms(exit.dest, keys))
    return reached

def reachable_keys(rooms):
    reached = []
    for room in rooms:
        reached.extend(room.items)
    return reached

def locked_doors(rooms, keys):
    reached = []
    for room in rooms:
        for exit in room.exits:
            if exit.locked and exit.name not in map(lambda k: k.exit, keys):
                reached.append(exit)
    return reached

def solvable(num_keys, root):
    reached_rooms = [root]
    found_keys = reachable_keys(reached_rooms)
    prev_reached_rooms = None
    while reached_rooms != prev_reached_rooms:
        prev_reached_rooms = reached_rooms
        reached_rooms = reachable_rooms(root, found_keys)
        found_keys = reachable_keys(reached_rooms)
    return len(found_keys) == num_keys

def make_rooms(data):
    root = Room(data)
    root.populate()
    generate(len(Constants.exit_names), root)
    return root

def generate(num_keys, root):
    rooms = [root]
    while not solvable(num_keys, root):
        keys = reachable_keys(rooms)
        rooms = reachable_rooms(root, keys)
        locked = locked_doors(rooms, keys)
        if locked == []:
            break
        lock = random.choice(locked)
        room = random.choice(rooms)
        key = Key(lock.name, room)
        room.items.append(key)

# places the keys in the room that's the least accessible from the start
# might be better to place it in the room that's the least accessible from the current room
def generate2(num_keys, root):
    rooms = [root]
    while not solvable(num_keys, root):
        keys = reachable_keys(rooms)
        rooms = reachable_depths(root, keys)
        random.shuffle(rooms)
        q = queue.PriorityQueue()
        for room in rooms:
            q.put(room)
        rooms = list(map(lambda x: x[1], rooms))
        locked = locked_doors(rooms, keys)
        lock = random.choice(locked)
        room = q.get()[1]
        key = Key(lock.name, room)
        room.items.append(key)
