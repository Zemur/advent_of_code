def score_for_selected(shape_selected):
    match shape_selected:
        case 'rock':
            return 1
        case 'paper':
            return 2
        case 'scissors':
            return 3


def round_score(round):
    """
    :param round:
    :return result_score:

    A Rock
    B Paper
    C Scissors

    X Lose
    Y Draw
    Z Win

    This will return one of the following:
    - 6 for a win
    - 3 for a draw
    - 0 for a loss
    """
    opponent_choice, intended_result = round
    match intended_result:
        case 'X':
            # Lose
            match opponent_choice:
                # What to lose to
                case 'A':
                    # Scissors
                    return score_for_selected('scissors')
                case 'B':
                    # Rock
                    return score_for_selected('rock')
                    pass
                case 'C':
                    # Paper
                    return score_for_selected('paper')
                    pass
        case 'Y':
            # Draw
            match opponent_choice:
                # What to draw to
                case 'A':
                    return score_for_selected('rock') + 3
                case 'B':
                    return score_for_selected('paper') + 3
                case 'C':
                    return score_for_selected('scissors') + 3
        case 'Z':
            # Win
            match opponent_choice:
                # What to win to
                case 'A':
                    return score_for_selected('paper') + 6
                case 'B':
                    return score_for_selected('scissors') + 6
                case 'C':
                    return score_for_selected('rock') + 6


if __name__ == '__main__':
    with open('input') as f:
        rounds = [i.strip('\n').split() for i in f.readlines()]
    round_scores = []
    for r in rounds:
        round_scores.append(round_score(r))
    print(sum(round_scores))
