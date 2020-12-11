import re


def load_passport_batch(passport_file):
    with open(passport_file) as f:
        passport_batch = f.read().split('\n\n')

    for i in range(len(passport_batch)):
        p_list = passport_batch[i].replace('\n', ' ').replace(':', ' ').split(' ')
        passport_batch[i] = dict(zip(p_list[::2], p_list[1::2]))

    return passport_batch


def validate_passport(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    if all(field in passport.keys() for field in required_fields):
        if not 1920 <= int(passport['byr']) <= 2002:
            return False
        if not 2010 <= int(passport['iyr']) <= 2020:
            return False
        if not 2020 <= int(passport['eyr']) <= 2030:
            return False
        if passport['hgt'][-2:] == 'cm':
            if not 150 <= int(passport['hgt'][:-2]) <= 193:
                return False
        elif passport['hgt'][-2:] == 'in':
            if not 59 <= int(passport['hgt'][:-2]) <= 76:
                return False
        else:
            return False
        if not re.search("^#([A-Fa-f0-9]{6})$", passport['hcl']):
            return False
        if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        if not re.search("^[0-9]{9}$", passport['pid']):
            return False
        return True
    return False


if __name__ == '__main__':
    passport_count = 0
    for p in load_passport_batch('input'):
        if validate_passport(p):
            passport_count += 1
    print(passport_count)

