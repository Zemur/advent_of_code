if __name__ == '__main__':
    with open('input', 'r') as f:
        positions = list(map(int, f.read().split(',')))

    min_pos = min(positions)
    max_pos = max(positions)
    destination = range(min_pos, max_pos)
    total_fuel_spent = []

    for i in destination:
        fuel_spent = 0
        for pos in positions:
            fuel_spent += abs(pos - i)
        total_fuel_spent.append(fuel_spent)
    print(min(total_fuel_spent))
