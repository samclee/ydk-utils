from draft_generator import generate_deck_dict_v1, generate_deck_dict_classic, combine_ydks
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        print("Generating deck")
        if sys.argv[1] == "--d":
            if len(sys.argv) >= 3:
                generate_deck_dict_v1(sys.argv[2])
            else:
                generate_deck_dict_v1()
        if sys.argv[1] == "--c":
            if len(sys.argv) >= 3:
                generate_deck_dict_classic(sys.argv[2])
            else:
                generate_deck_dict_classic()
    else:
        print("Generating pool")
        combine_ydks(["m1.ydk", "m2.ydk", "spells.ydk", "traps.ydk"], "pool.ydk")