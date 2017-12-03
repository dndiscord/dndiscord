import random
import copy

from src.Objects.Key import Key
from src import Constants

class Room:
    def __init__(self, data, parent=None):
        self.data = data
        self.populated = False
        self.desc = "UNPOPULATED"
        self.doors = []
        self.items = []
        self.parent = parent
        if parent is not None:
            self.doors.append(parent) # door back where we came from

    def populate(self):
        num_doors = random.randint(min(1, len(self.data.doors)), min(3, len(self.data.doors)))
        if len(self.data.rooms) == 0:
            return
        self.desc = random.sample(self.data.rooms, 1)[0]
        self.data.rooms.remove(self.desc)
        dirs = random.sample(self.data.doors, num_doors)
        for name in dirs:
            self.data.doors.remove(name)
        for name in dirs:
            door = Door(self, name, random.random() > 0.2)
            door.dest.populate()
            self.doors.append(door)

    def describe(self):
        return self.desc + " with doors " + str(list(map(lambda x: x.desc(), self.doors))) + " and keys " + str(list(map(lambda k: k.door + " key", self.items)))

    def show(self):
        print(self.describe())
        for door in self.doors:
            if door.dest != self:
                door.show()
                door.dest.show()

class Door:
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
    for door in room.doors:
        if not door.locked or door.name in map(lambda k: k.door, keys):
            if door.dest != room:
                reached.extend(reachable_rooms(door.dest, keys))
    return reached

def reachable_keys(rooms):
    reached = []
    for room in rooms:
        reached.extend(room.items)
    return reached

def locked_doors(rooms, keys):
    reached = []
    for room in rooms:
        for door in room.doors:
            if door.locked and door.name not in map(lambda k: k.door, keys):
                reached.append(door)
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
    generate(len(Constants.doors), root)
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

