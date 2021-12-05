def find_common_bit(report_by_column, position_to_check, preferred_bit, most=True):
    num_zeros = report_by_column[position_to_check].count('0')
    num_ones = report_by_column[position_to_check].count('1')

    if num_zeros == num_ones:
        return preferred_bit
    elif most:
        if num_zeros > num_ones:
            return '0'
        elif num_ones > num_zeros:
            return '1'
    else:
        if num_zeros > num_ones:
            return '1'
        elif num_ones > num_zeros:
            return '0'


def read_rating(rating_input, precedent_bit, rating_to_read):
    column_report = list(zip(*rating_input[::-1]))
    column_position = 0
    bit_position = 0

    while len(rating_input) > 1:
        if rating_to_read == 'oxygen':
            bit_to_keep = find_common_bit(column_report, column_position, precedent_bit)
        elif rating_to_read == 'co2_scrubber':
            bit_to_keep = find_common_bit(column_report, column_position, precedent_bit, False)
        else:
            raise Exception("Rating not understood. Please specify 'oxygen' or 'co2_scrubber'.")
        rating_input = [i for i in rating_input if i[bit_position] == str(bit_to_keep)]
        column_report = list(zip(*rating_input[::-1]))
        bit_position += 1
        column_position += 1

    return int(rating_input[0], 2)


if __name__ == '__main__':
    with open('diagnostic_report', 'r') as f:
        report = [i.strip() for i in f.readlines()]

        oxygen_generator_rating = read_rating(report, 1, 'oxygen')
        co2_scrubber_rating = read_rating(report, 0, 'co2_scrubber')

        print(oxygen_generator_rating * co2_scrubber_rating)
