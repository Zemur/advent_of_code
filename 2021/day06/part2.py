import pandas as pd
import numpy as np
import sys
from collections import Counter

if __name__ == '__main__':
    with open('input', 'r') as f:
        lanternfish = list(map(int, f.read().split(',')))
    max_days = 256

    timers = Counter({timer: 0 for timer in range(10)})
    lanternfish = Counter(lanternfish)
    lanternfish.update(timers)
    for day in range(max_days):
        lanternfish[7] += lanternfish.get(0, 0)
        lanternfish[9] += lanternfish.get(0, 0)
        lanternfish = {i: lanternfish.get(i + 1, 0) for i in lanternfish}

    print(sum(lanternfish.values()))