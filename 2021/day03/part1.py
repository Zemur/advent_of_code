if __name__ == '__main__':
    with open('diagnostic_report', 'r') as f:
        report = [list(i.strip()) for i in f.readlines()]

    report_by_column = list(zip(*report[::-1]))
    gamma_rate = 0
    epsilon_rate = 0
    most_common_bit_per_column = ''

    for i in report_by_column:
        most_common_bit_per_column += max(i, key=i.count)

    least_common_bit_per_column = ''.join('1' if x == '0' else '0' for x in most_common_bit_per_column)

    gamma_rate = int(most_common_bit_per_column, 2)
    epsilon_rate = int(least_common_bit_per_column, 2)

    print(gamma_rate * epsilon_rate)
