import itertools
import math


def get_target_product(expense_report_file, target_number, amount_to_sum):
    with open(expense_report_file) as f:
        expense_report = [int(x) for x in f.readlines()]

    for i in itertools.combinations(expense_report, amount_to_sum):
        if sum(i) == target_number:
            return math.prod(i)


if __name__ == '__main__':
    print(get_target_product('input', 2020, 3))
