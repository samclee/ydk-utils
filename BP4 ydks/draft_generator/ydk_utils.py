import string
import pdb
import os
from .selection_utils import sample_random

def parse_ydk_into_dict(fname):
    parsed_dict = {}
    cur_field_name = ""
    with open(fname, 'r') as f:
        for line in f:
            if line.isspace():
                continue
            elif line[0] in string.punctuation:
                cur_field_name = line[1:].rstrip()
                parsed_dict[cur_field_name] = []
            else:
                parsed_dict[cur_field_name].append(line.rstrip())
    return parsed_dict
            

def combine_ydks_into_dict(fname_list):
    big_ydk = {
        "main": [],
        "extra": [],
        "side": []
    }
    for fname in fname_list:
        cur_dict = parse_ydk_into_dict(fname)
        for key in big_ydk:
            big_ydk[key] += cur_dict[key]
    return big_ydk

def convert_dict_to_ydk(ydk_dict, fname):
    with open(fname, "w+") as f:
        f.write("#main\n")
        for card_id in ydk_dict["main"]:
            f.write(card_id + "\n")

        f.write("\n#extra\n")
        for card_id in ydk_dict["extra"]:
            f.write(card_id + "\n")
        
        f.write("\n!side\n")
        for card_id in ydk_dict["side"]:
            f.write(card_id + "\n")

def combine_ydks(fname_list, fname):
    big_dict = combine_ydks_into_dict(fname_list)
    convert_dict_to_ydk(big_dict, fname)

def generate_deck_dict_v1(deck_name = "new_deck.ydk"):
    monsters_dict = combine_ydks_into_dict(["m1.ydk", "m2.ydk"])
    # Extract list of each card type
    main_monsters_list =  monsters_dict["main"]
    extra_monsters_list = monsters_dict["extra"] + monsters_dict["side"]
    spells_list = parse_ydk_into_dict("spells.ydk")["main"]
    traps_list = parse_ydk_into_dict("traps.ydk")["main"]
    # Take sample from each list
    main_monster_sample = sample_random(main_monsters_list, 25)
    extra_monster_sample = sample_random(extra_monsters_list, 20)
    spells_sample = sample_random(spells_list, 15)
    traps_sample = sample_random(traps_list, 15)
    # Construct ydk dict
    deck_dict = {
        "main": main_monster_sample + spells_sample + traps_sample,
        "extra": extra_monster_sample[:10],
        "side": extra_monster_sample[10:]
    }
    # Save dict as ydk
    if not deck_name.endswith(".ydk"):
        deck_name += ".ydk"
    convert_dict_to_ydk(deck_dict, deck_name)

def generate_deck_dict_classic(deck_name = "new_deck.ydk"):
    monsters_dict = combine_ydks_into_dict(["peter-pool/m1.ydk", "peter-pool/m2.ydk", "peter-pool/m3.ydk"])
    # Extract list of each card type
    main_monsters_list =  monsters_dict["main"]
    extra_monsters_list = monsters_dict["extra"] + monsters_dict["side"]
    spells_list = parse_ydk_into_dict("peter-pool/spells.ydk")["main"]
    traps_list = parse_ydk_into_dict("peter-pool/traps.ydk")["main"]
    # Take sample from each list
    main_monster_sample = sample_random(main_monsters_list, 10)
    extra_monster_sample = sample_random(extra_monsters_list, 0)
    spells_sample = sample_random(spells_list, 5)
    traps_sample = sample_random(traps_list, 5)
    # Construct ydk dict
    deck_dict = {
        "main": main_monster_sample + spells_sample + traps_sample,
        "extra": extra_monster_sample,
        "side": []
    }
    # Save dict as ydk
    if not deck_name.endswith(".ydk"):
        deck_name += ".ydk"
    convert_dict_to_ydk(deck_dict, deck_name)
