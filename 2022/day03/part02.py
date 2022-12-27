def find_common_items(first_compartment, second_compartment):
    return [ord(i)-96 if i.islower() else ord(i)-38 for i in second_compartment if i in first_compartment][0]


def identify_badge_priorities(elves_items):
    return [ord(i)-96 if i.islower() else ord(i)-38 for i in elves_items[0] if i in elves_items[1] and i in elves_items[2]][0]


if __name__ == '__main__':
    badge_priorities = []
    with open('input') as f:
        i = 0
        tmp_group = []
        for elf in f.readlines():
            tmp_group.append(elf.strip())
            i += 1
            if i > 2:
                badge_priorities.append(identify_badge_priorities(tmp_group))
                i = 0
                tmp_group.clear()

    print(sum(badge_priorities))
