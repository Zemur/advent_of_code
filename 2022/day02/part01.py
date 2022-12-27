def score_for_selected(shape_selected):
    match shape_selected:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3


def round_score(round):
    """
    :param round:
    :return result_score:

    A, X Rock
    B, Y Paper
    C, Z Scissors

    This will return one of the following:
    - 6 for a win
    - 3 for a draw
    - 0 for a loss

    """
    match round[0]:
        # Opponent threw rock
        case 'A':
            match round[1]:
                case 'X':
                    return 3
                case 'Y':
                    return 6
                case 'Z':
                    return 0
        case 'B':
            match round[1]:
                case 'X':
                    return 0
                case 'Y':
                    return 3
                case 'Z':
                    return 6
        case 'C':
            match round[1]:
                case 'X':
                    return 6
                case 'Y':
                    return 0
                case 'Z':
                    return 3


if __name__ == '__main__':
    with open('input') as f:
        rounds = [i.strip('\n').split() for i in f.readlines()]
    round_scores = []
    for r in rounds:
        round_scores.append(score_for_selected(r[1]) + round_score(r))
    print(sum(round_scores))
