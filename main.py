import pickledb
import random

db = pickledb.load("words.db", False)

words = list(db.getall())
print(len(words))