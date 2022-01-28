import pickledb
import random
from extra.letter import frequency
from pprint import pprint

db = pickledb.load("words.db", False)

words = list(db.getall())

for word in words:
    for i in range(5):
        frequency[word[i]]["Loc"][i] += 1
        frequency[word[i]]["Total"] += 1

with open("frequency.csv", 'w') as fout:
    fout.write("Letter, Position, , , , ,Total\n")
    for letter in frequency:
        fout.write(letter + ',')
        for i in range(5):
            fout.write(f"{frequency[letter]['Loc'][i]},")
        fout.write(f"{frequency[letter]['Total']}\n")