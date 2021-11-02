import random
import copy
import pdb

def shuffle(items):
    items_copy = copy.copy(items)
    n = len(items_copy)
    for i in range(n-2):
        j = random.randint(i, n-1)
        items_copy[i], items_copy[j] = items_copy[j], items_copy[i]
    return items_copy

def sample_random(items, num, unique = False):
    if (num > len(items)):
        error = "Num {} is bigger than item len {}".format()
        raise 
    if unique:
        return sample_random_unique(items, num)
    else:
        return sample_random_repeats(items, num)

def sample_random_unique(items, num):
    shuffled_items = shuffle(items)
    return shuffled_items[:num]

def sample_random_repeats(items, num):
    new_list = []
    n = len(items)
    for i in range(num):
        random_item = items[random.randint(0, n-1)]
        new_list.append(random_item)
    return new_list
