# use python -m cProfile letterpress_cheat.py
import pickle
from itertools import combinations

PICKLE_WORD_FILE = "anagram-dictionary.pickle"
WORDS_FILE = "/usr/share/dict/words"


def create_anagram_dict():
    """Creates a dictionary of all possible anagrams associated with their corresponding words"""
    try:
        with open(WORDS_FILE, "r") as words_file:
            words_anagram_dict = {}
            for word in words_file.readlines():
                word = word.lower().rstrip()
                if word.isalpha() and (2 < len(word) < 12):
                    word_anagram = tuple(sorted(word))
                    words_anagram_dict.setdefault(word_anagram, []).append(word)
        return words_anagram_dict
    except FileNotFoundError:
        print("words file not found, maybe you are not in a Linux system,"
              "\ntry modify code to use another path for file\n")


def find_possible_words(anagrams, available_letters):
    """return an ordered list of all possible words that can be made with available letters"""
    found_words = []
    already_visited = {}
    assert (len(available_letters) > 2)
    letters_deck = sorted(available_letters)
    for k in range(len(letters_deck), 2, -1):
        for comb in combinations(letters_deck, k):
            try:
                already_visited[comb]
            except KeyError:
                already_visited[comb] = True
                try:
                    found_words.extend(anagrams[comb])
                except KeyError:
                    pass
    return found_words


if __name__ == '__main__':
    try:
        with open(PICKLE_WORD_FILE, "rb") as f:
            words_anagrams = pickle.load(f)
    except FileNotFoundError:
        words_anagrams = create_anagram_dict()
        pickle.dump(words_anagrams, open(PICKLE_WORD_FILE, "wb"))

    words = find_possible_words(words_anagrams, "plheouitrtobhfeghyuj")
    print(words)

