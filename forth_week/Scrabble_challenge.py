#!/usr/bin/env python
#coding:utf-8
from __future__ import print_function
import sys

#Step 1: construct a word list
def get_all_words(file_name):
    all_words = []
    with open(file_name) as f:
        for line in f:
            all_words.append(line.strip())
    return all_words

#Step 3: find valid words
def find_valid_words(all_words, rack):
    valid_words = []
    for word in all_words:
        rack_characters = list(rack)
        word_characters = list(word)
        valid = True
        for char in word_characters:
            if char in rack_characters:
                rack_characters.remove(char)
            else:
                valid = False
                break

        if valid:
            valid_words.append(word)
    return [ word.lower() for word in valid_words ]

#Step 4: scoring
def count_scores(words):
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
    words_dict = {}
    for word in words:
        words_dict[word] = sum(scores[char] for char in word)
    return words_dict

def main():
    #Step 2: get the rack
    if len(sys.argv) != 2:
        raise SystemExit('Usage: scrabble.py [RACK]')
    rack = sys.argv[1].upper()

    all_words = get_all_words('sowpods.txt')
    valid_words = find_valid_words(all_words, rack)

    words_dict = count_scores(valid_words)
    for val, key in sorted(words_dict.iteritems(), key=lambda (k,v): (v)):
        print(val, key)

if __name__ == '__main__':
    main()
