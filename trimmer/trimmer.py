import csv

class Card:
    def __init__(self, row):
        self.cardname = row[0]
        self.cardq = str(min(int(row[1]), 3))
        self.cardid = row[2]
        self.cardrarity = row[3]
        self.cardcondition = row[4]
        self.card_edition = row[5]
        self.cardset = row[6]
        self.cardcode = row[7]

    def to_row(self):
        return [self.cardname, self.cardq, self.cardid, self.cardrarity, self.cardcondition, self.card_edition, self.cardset, self.cardcode]

def trim_collection(fname = "Card Collection.csv"):
    new_fname = fname[:-4] + "_trimmed.csv"
    cur_card = None

    with open(fname, mode='r') as untrimmed:
        csv_reader = csv.reader(untrimmed, delimiter=",")
        with open(new_fname, mode='w+') as trimmed:
            csv_writer = csv.writer(trimmed, delimiter=",")
            row_num = 0
            for row in csv_reader:
                if row_num == 0:
                    csv_writer.writerow(row)
                elif row_num != 0:
                    if cur_card == None:
                        cur_card = Card(row)
                    elif row[0] != cur_card.cardname:
                        csv_writer.writerow(cur_card.to_row())
                        cur_card = Card(row)
                    else:
                        cur_card.cardq = str(min(int(cur_card.cardq) + int(row[1]), 3))

                row_num += 1

if __name__ == "__main__":
    trim_collection()