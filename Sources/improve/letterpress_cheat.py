# use python -m cProfile letterpress_cheat.py

words_anagram_dict = {}
words_anagrams = []


def create_anagram_dict():
    with open("/usr/share/dict/words", "r") as words_file:
        for word in words_file.readlines():
            word = word.lower().rstrip()
            if word.isalpha():
                word_anagram = ''.join(sorted(word))
                words_anagram_dict.setdefault(word_anagram, []).append(word)
# Computationally Heavy
#               if word_anagram not in words_anagrams:
#                   words_anagrams.append(word_anagram)
#       words_anagrams.sort()


def save_anagram_dict():
    with open("./anagrams.txt", "w") as anagram_file:
        for anagram in words_anagram_dict:
            anagram_file.write('{anagram} : {words} \n'.format(
                anagram=anagram,
                words=' '.join(words_anagram_dict[anagram]))
            )


if __name__ == '__main__':
    create_anagram_dict()
    save_anagram_dict()

