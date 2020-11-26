import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json"))


def Defn(key1):
    key1 = key1.lower()
    return data[key1]


while True:
    word = input("Enter a word to be searched:")
    x = get_close_matches(word, data, 1, 0.6)
    try:
        print(Defn(word))
    except KeyError:
        try:
            if x[0].isalpha():
                che = input("Did you mean " + x[0] + " ?If yes type Y, if No type N:")
                if che in "Yy":
                    print(Defn(x[0]))
                    continue
                elif che in "Nn":
                    continue
                else:
                    print("Seriously?")
                    exit()
        except IndexError:
            print("Invalid word: Please re-enter a valid word.")




