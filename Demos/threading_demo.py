#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'threading_demo.py'
# Author:   'yancai'

"""Documentation"""


import threading
import time


FRUITS = [
    "banana",
    "pear",
    "cherry"
]


def kid(fruit, n=1):
    for i in range(n):
        print("I want " + fruit)
        time.sleep(0.5)


def main():
    threads = []
    times_ = 3
    for i in range(times_):
        threads.append(threading.Thread(
            target=kid,
            args=(FRUITS[i], 10)
        ))

    for i in range(times_):
        threads[i].start()

    for i in range(times_):
        threads[i].join()

    raw_input("all done...")

if __name__ == "__main__":
    main()
    pass
