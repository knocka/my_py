#!/usr/bin/env python3

import sys
import time
from urllib.request import urlopen

def logme(m):
    t1 = time.time();
    print(t1)


def fetch_word():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            time.sleep(1)
            logme(line)
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
                print([len(word) for word in story_words])
        for word in story_words:
            print(word)


if __name__ == '__main__':
    fetch_word()
