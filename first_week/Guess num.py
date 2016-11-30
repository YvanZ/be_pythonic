#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def play_game(num):
    while True:
        a = int(raw_input("Please input a number: "))
        if a > num:
            print "The number is bigger"
        elif a < num:
            print "The number is smaller"
        else :
            print "You are right!"
            break

def main():
    print "--------begin game---------"
    num = random.randint(0,99)
    play_game(num)

if __name__ ==  '__main__':
    main()
