import pickledb

db = pickledb.load("words.db", False)

with open("data/Collins Scrabble Words (2019) with definitions.txt", 'r') as fin:
    for line in fin:
        word_def = line.split('\t')
        if len(word_def[0]) == 5:
            db.set(word_def[0], word_def[1])

db.dump()