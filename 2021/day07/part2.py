if __name__ == '__main__':
    with open('input', 'r') as f:
        positions = list(map(int, f.read().split(',')))

    min_pos = min(positions)
    max_pos = max(positions)
    destinations = range(min_pos, max_pos)
    all_fuels = []

    for dest in destinations:
        total_fuel = []
        for pos in positions:
            fuel_spent = abs(pos - dest)
            fuel_to_position = ((fuel_spent**2 + fuel_spent) / 2)
            total_fuel.append(fuel_to_position)
        all_fuels.append(sum(total_fuel))

    print(int(min(all_fuels)))
