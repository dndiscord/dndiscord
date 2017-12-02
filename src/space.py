import random 
import time
import copy

from src.Objects.Key import Key
from src import Constants

class Room:
    def __init__(self, data, parent=None):
        self.data = data
        self.populated = False
        self.desc = "unpopulated"
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
        for direction in dirs:
            self.data.exit_names.remove(direction)
        for direction in dirs:
            exit = Exit(self, direction)
            exit.dest.populate()
            self.exits.append(exit)

    def describe(self):
        return self.desc + " with doors " + str(list(map(lambda x: x.direction, self.exits))) + " and keys " + str(list(map(lambda k: k.exit, self.items)))

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

def reachable_rooms(room, keys):
    reached = [room]
    for exit in room.exits:
        if exit.direction in map(lambda k: k.exit, keys):
            if exit.dest != room:
                reached.extend(reachable_rooms(exit.dest, keys))
    return reached

def reachable_keys(rooms):
    reached = []
    for room in rooms:
        reached.extend(room.items)
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
    while True:
        try:
            root = Room(copy.deepcopy(data))
            root.populate()
            generate(time.time(), len(Constants.exit_names), 0, root, root)
            return root
        except:
            print("mapgen failed, trying again...")

def generate(start_time, num_keys, keys, root, room):
    if time.time() - start_time > 3:
        raise "out of time"
    all_keys = (1 << num_keys) - 1
    if keys == all_keys: # all keys placed
        return solvable(num_keys, root)
    key_idxs = list(range(0, num_keys))
    random.shuffle(key_idxs)
    for key in key_idxs:
        if (keys & 1 << key) == 0: # need to place this key
            opts = []
            opts.append((True, room))
            for exit in room.exits:
                if exit.dest == room:
                    continue
                opts.append((False, exit.dest))
            random.shuffle(opts)
            for (place, next_room) in opts:
                key_item = Key(Constants.exit_names[key])
                if place:
                    room.items.append(key_item)
                    if generate(start_time, num_keys, keys | 1 << key, root, next_room):
                        return True
                    room.items.pop()
                else:
                    if generate(start_time, num_keys, keys, root, next_room):
                        return True



