from bingocard import BingoCard

if __name__ == '__main__':
    cards = []
    highest_score = 0
    winning_card = BingoCard
    nidx = 0
    num_winners = 0

    with open('input') as f:
        numbers_called = [i.strip() for i in f.readline().split(',')]
        card_input = f.readlines()
        splits = [i for i, x in enumerate(card_input) if x == '\n']

        for i in splits:
            cards.append(BingoCard([i.strip().split() for i in card_input[i: i+6] if i != '\n']))

    while num_winners < len(cards):
        print(f"Calling number {numbers_called[nidx]}!")
        for card in cards:
            if card.is_winner():
                continue
            card.mark_card(numbers_called[nidx])
            if card.is_winner():
                num_winners += 1
                card.pretty_print()
                print("final score:", card.score_sum * int(numbers_called[nidx]))
        nidx += 1
