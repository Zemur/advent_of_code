if __name__ == '__main__':
    num_unique_digits = 0

    with open('input', 'r') as f:
        output_values = [i.split('|')[1].strip().split(' ') for i in f.readlines()]

    for output in output_values:
        for digit in output:
            if len(digit) in [2, 3, 4, 7]:
                num_unique_digits += 1

    print(num_unique_digits)



