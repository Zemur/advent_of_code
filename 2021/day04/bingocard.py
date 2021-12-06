import re


class BingoCard:
    def __init__(self, card):
        self.lines = card
        self.winning_sequence = []
        self.score_sum = 0

    def mark_card(self, num_to_mark):
        bold = '\033[1;36m'
        escape = '\033[0m'
        for line in self.lines:
            for number in range(len(line)):
                if line[number] == num_to_mark:
                    line[number] = f"{bold}{num_to_mark}{escape}"

    def pretty_print(self):
        for line in self.lines:
            print(' '.join(line))

    def calculate_score(self):
        for line in self.lines:
            for number in line:
                if not number.startswith('\x1b'):
                    self.score_sum += int(number)

    def is_winner(self):
        self.score_sum = 0
        ansi_escape = re.compile(r'(\x1b\[)[0-?]*[ -/]*[@-~]')

        for line in self.lines:
            if len([i for i in line if i.startswith('\x1b')]) == 5:
                self.winning_sequence = [int(ansi_escape.sub('', i)) for i in line]

        for col in [i for i in list(zip(*self.lines[::-1]))]:
            if len([i for i in col if i.startswith('\x1b')]) == 5:
                self.winning_sequence = [int(ansi_escape.sub('', i)) for i in col]

        if self.winning_sequence:
            self.calculate_score()
            return True
        else:
            return False
