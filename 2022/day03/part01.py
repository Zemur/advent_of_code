def find_common_items(first_compartment, second_compartment):
    return [ord(i)-96 if i.islower() else ord(i)-38 for i in second_compartment if i in first_compartment][0]


if __name__ == '__main__':
    priorities = []
    with open('input') as f:
        rucksacks = f.readlines()

    for rucksack in rucksacks:
        priorities.append(find_common_items(rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]))

    print(sum(priorities))
