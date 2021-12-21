class Octopus(object):
    def __init__(self, energy):
        self.flashed = 0
        self.energy = energy
        self.times_flashed = 0

    def increase(self):
        self.energy += 1
        if self.energy > 9 and not self.flashed:
            self.to_flash()

    def to_flash(self):
        if not self.flashed:
            self.flashed = 1

    def flash(self):
        if self.flashed == 1:
            self.flashed = 2
            return True
        else:
            return False

    def reset(self):
        if self.flashed == 2:
            self.energy = 0
            self.flashed = 0
            return True
        else:
            return False
