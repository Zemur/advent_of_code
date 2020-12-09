def old_password_is_valid(passwd):
    min_occurrences, max_occurrences, letter_to_look_for, pass_string = passwd

    if int(min_occurrences) <= pass_string.count(letter_to_look_for) <= int(max_occurrences):
        return True
    return False


def password_is_valid(passwd):
    first_position, second_position, letter_to_look_for, pass_string = passwd
    if ((pass_string[int(first_position) - 1] == letter_to_look_for or
            pass_string[int(second_position) - 1] == letter_to_look_for) and
            pass_string[int(first_position) -1] != pass_string[int(second_position)-1]):
        print('True', passwd)
        return True
    return False


def validate_passwords(password_file):
    full_p_list = []
    valid_p_list = []

    with open(password_file) as f:
        for line in f.readlines():
            full_p_list.append([x.strip() for x in line.replace('-', ' ', ).replace(':', '').split(' ')])

    for passwd in full_p_list:
        if password_is_valid(passwd):
            valid_p_list.append(passwd)

    return valid_p_list


if __name__ == '__main__':
    print(len(validate_passwords('input')))
