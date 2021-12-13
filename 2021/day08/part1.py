if __name__ == '__main__':
    sorted_outputs = []
    # digits = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    # unique_digits = {1: 'cf', 4: 'bcdf', 7: 'acf', 8: 'abcdefg'}
    num_unique_digits = 0

    with open('input', 'r') as f:
        output_values = [i.split('|')[1].strip().split(' ') for i in f.readlines()]

    for output in output_values:
        sorted_outputs.append([''.join(sorted(i)) for i in output])

    for sorted_output in sorted_outputs:
        for digit in sorted_output:
            if len(digit) in [2, 3, 4, 7]:
                if len(digit) == 8:
                    print(digit)
                num_unique_digits += 1

    print(num_unique_digits)



