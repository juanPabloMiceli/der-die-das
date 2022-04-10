#!/usr/bin/env python3

import requests
import sys, os
import urllib3
from threading import Thread

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def get_code(article, word):
    with requests.Session() as session:
        with session.get(f"https://der-artikel.de/{article}/{word}.html", verify = False) as r:
            return r.status_code

def is_der(word):
    return 200 == get_code("der", word)

def is_die(word):
    return 200 == get_code("die", word)

def is_das(word):
    return 200 == get_code("das", word)

def get_article(word):
    der_thread = ThreadWithReturnValue(target = is_der, args=[word])
    die_thread = ThreadWithReturnValue(target = is_die, args=[word])
    das_thread = ThreadWithReturnValue(target = is_das, args=[word])

    der_thread.start()
    die_thread.start()
    das_thread.start()

    if der_thread.join():
        return "der " + word
    if die_thread.join():
        return "die " + word
    if das_thread.join():
        return "das " + word
    return f"{word} not found :("


def main():
    if(len(sys.argv) != 2):
        print("Use: python3 derDieDas <word>")
        exit(1)

    article = get_article(sys.argv[1].capitalize())
    print(article)


if __name__ == "__main__":
    # Disable anoying warning, I don't really care der-artikel hasn't TLS. 
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()