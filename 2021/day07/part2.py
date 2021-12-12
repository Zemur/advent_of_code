if __name__ == '__main__':
    with open('input', 'r') as f:
        positions = list(map(int, f.read().split(',')))

    destinations = range(min(positions), max(positions))
    all_fuels = []

    for dest in destinations:
        total_fuel = []
        for pos in positions:
            fuel_spent = abs(pos - dest)
            total_fuel.append(((fuel_spent**2 + fuel_spent) / 2))
        all_fuels.append(sum(total_fuel))

    print(int(min(all_fuels)))
