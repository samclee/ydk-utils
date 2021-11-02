from copy import copy

class Ydk():
    MAIN_MARKER = '#main'
    EXTRA_MARKER = '#extra'
    SIDE_MARKER = '!side'

    def __init__(self, fname: str):
        self.monsters = []
        self.extra = []
        self.side = []
        with open(fname, 'r') as f:
            for line in f:
                line = line.rstrip()
                if not line: continue

                if line == self.MAIN_MARKER:
                    print(line)
                elif line == self.EXTRA_MARKER:
                    print(line)
    
    def __init__(self, monster_list: list[str],
        extra_list: list[str],
        side_list: list[str]):
        self.monsters = copy(monster_list)
        self.extra = copy(extra_list)
        self.side = copy(side_list)
    
    def __add__(self, other):
        return Ydk(
            self.monsters + other.monsters,
            self.extra + other.extra,
            self.side + other.side
        )
    
    def get_lists(self):
        return (self.monsters, self.extra, self.side)