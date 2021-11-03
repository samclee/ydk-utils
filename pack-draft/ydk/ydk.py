from copy import copy
from pathlib import Path
import pdb

MAIN_MARKER = '#main'
EXTRA_MARKER = '#extra'
SIDE_MARKER = '!side'

class Ydk:
    def __init__(self, main_list: list[str],
        extra_list: list[str],
        side_list: list[str]):
        self.main = copy(main_list)
        self.extra = copy(extra_list)
        self.side = copy(side_list)
    
    def __add__(self, other):
        return Ydk(
            self.main + other.main,
            self.extra + other.extra,
            self.side + other.side
        )
    
    def get_lists(self):
        return (self.main, self.extra, self.side)

def file_to_ydk(fname: Path) -> Ydk:
    MAIN_KEY = 'main'
    EXTRA_KEY = 'extra'
    SIDE_KEY = 'side'

    ydk_dict = {
        MAIN_KEY: [],
        EXTRA_KEY: [],
        SIDE_KEY: []
    }
    cur_key = 'main'
    with open(fname, 'r') as f:
        for line in f:
            line = line.rstrip()
            if not line: continue
            if line == '#created by ...': continue

            if line == MAIN_MARKER:
                cur_key = MAIN_KEY
            elif line == EXTRA_MARKER:
                cur_key = EXTRA_KEY
            elif line == SIDE_MARKER:
                cur_key = SIDE_KEY
            else:
                ydk_dict[cur_key].append(line)
    return Ydk(ydk_dict[MAIN_KEY],
        ydk_dict[EXTRA_KEY],
        ydk_dict[SIDE_KEY])