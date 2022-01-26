from random_word import RandomWords
import enchant

r_generate = RandomWords()
d = enchant.Dict("en_US")
words = []

for _ in range(10):
    word = r_generate.get_random_word(hasDictionaryDef = "true", minLength = 5, maxLength = 5)
    while not d.check(word):
        word = r_generate.get_random_word(hasDictionaryDef = "true", minLength = 5, maxLength = 5)
    words.append(word)

print(words)

