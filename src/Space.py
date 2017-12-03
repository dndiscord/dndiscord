import random
import copy

from src.Objects.Key import Key
from src import Constants
from src.Objects.Item import Item

class Room:
    def __init__(self, data, parent=None):
        self.data = data
        self.doors = []
        self.objects = []
        self.populate()
        if parent is not None:
            self.doors.append(parent) # door back where we came from
            self.objects.append(parent)

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
            door = Door(name, self, random.random() > 0.2)
            self.doors.append(door)
            self.objects.append(door)

    def describe(self):
        return self.desc + " with doors " + str(list(map(lambda x: x.description, self.doors))) + " and keys " + str([x.door + " key" for x in self.objects if isinstance(x, Key)])

    def show(self):
        print(self.describe())
        for door in self.doors:
            if door.dest != self:
                door.show()
                door.dest.show()

class Door(Item):
    def __init__(self, name, src, locked, dest=None):
        super().__init__({
                Constants.name: name + "Door",
                Constants.description: "A door",
                Constants.value: 13,
                Constants.effect: "smother",
                Constants.health: 10000,
                Constants.attack: 100,
                Constants.inventory: []
                })
        self.locked = locked
        self.src = src
        self.dest = dest or Room(src.data, self)
        self.update_desc(src)

    def update_desc(self, src):
        self.description = ["A unlocked ", "A locked "][int(self.locked)] + "door to " + self.other_side(src).desc + " labelled " + self.name

    def other_side(self, src):
        return [self.src, self.dest][int(self.src == src)]

    def side_side(self, src):
        return [self.dest, self.src][int(self.src == src)]

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
        reached.extend([x for x in room.objects if isinstance(x, Key)])
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
        key = Key({
                Constants.name: lock.name + "Key",
                Constants.description: "A key to the " + lock.name + " door",
                Constants.value: 100,
                Constants.effect: "poke",
                Constants.health: 5,
                Constants.attack: 2,
                Constants.inventory: []
                }, lock.name, room)
        room.objects.append(key)

