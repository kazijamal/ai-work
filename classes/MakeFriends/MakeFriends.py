#! /usr/bin/python3

import sys


class Friend:

    def __init__(self, name, color, category):
        self.name = name
        self.color = color
        self.category = category


class FriendGroup:

    def __init__(self):
        self.friends = dict()

    def add(self, name, color, category):
        if self.friends.get(name) != None:
            self.friends[name].category = category
        else:
            new_friend = Friend(name, color, category)
            self.friends[name] = new_friend

    def delete(self, name):
        if self.friends.get(name) != None:
            self.friends.pop(name)
            return True
        else:
            return False

    def get_cat(self, name):
        print(name)
        if self.friends.get(name) != None:
            return self.friends[name].category
        else:
            return None

    def change_cat(self, old_category, new_category):
        num_changes = 0
        for name in self.get_names():
            curr_friend = self.friends[name]
            if curr_friend.category == old_category:
                curr_friend.category = new_category
                num_changes += 1
        return num_changes

    def get_friend(self, name):
        return self.friends.get(name)

    def get_names(self):
        return list(self.friends.keys())


def MakeFriends():
    fg = FriendGroup()

    f_in = open(sys.argv[1], 'r')
    s = f_in.read()
    f_in.close()
    if '\r\n' in s:
        commands = s.split('\r\n')
    else:
        commands = s.split('\n')
    f_out = open(sys.argv[2], 'w')

    for command in commands:
        args = command.split(',')
        if args[0] == 'add':
            fg.add(args[1], args[2], int(args[3]))
        elif args[0] == 'delete':
            fg.delete(args[1])
        elif args[0] == 'change_cat':
            fg.change_cat(int(args[1]), int(args[2]))
        elif args[0] == 'print':
            names = fg.get_names()
            names.sort()
            for name in names:
                friend = fg.friends[name]
                f_out.write(name + ',' + friend.color + ',' + str(friend.category) + '\n')

    f_out.close()
    print("output file", sys.argv[2], "was written to successfully")


def main():
    MakeFriends()


if __name__ == '__main__':
    main()
