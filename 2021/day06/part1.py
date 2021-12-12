if __name__ == '__main__':
    with open('input', 'r') as f:
        lanternfish = list(map(int, f.read().split(',')))
    current_day = 0
    max_days = 80
    i = 0
    print(f"Initial state: {lanternfish}")
    while current_day < max_days:
        new_fish = 0
        for i in range(len(lanternfish)):
            if lanternfish[i] - 1 >= 0:
                lanternfish[i] -= 1
            else:
                lanternfish[i] = 6
                new_fish += 1
        current_day += 1
        for i in range(new_fish):
            lanternfish.append(8)
        print(f"After {current_day} day(s):", ','.join([str(i) for i in lanternfish]))

    print(len(lanternfish))
