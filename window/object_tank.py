import tkinter


class Tank:
    def __init__(self, colour='black', x=10, y=10, orientation='top'):
        self.colour = colour
        self.x = x
        self.y = y
        self.orientation = orientation

    def paint_tank(self):
        if self.orientation == 'top':
            coordinates = [[self.x, self.y],
                           [self.x - 1, self.y],
                           [self.x + 1, self.y],
                           [self.x - 1, self.y + 1],
                           [self.x + 1, self.y + 1],
                           [self.x, self.y - 1]]
        elif self.orientation == 'down':
            coordinates = [[self.x, self.y],
                           [self.x - 1, self.y],
                           [self.x + 1, self.y],
                           [self.x - 1, self.y - 1],
                           [self.x + 1, self.y - 1],
                           [self.x, self.y + 1]]
        elif self.orientation == 'right':
            coordinates = [[self.x, self.y],
                           [self.x, self.y + 1],
                           [self.x, self.y - 1],
                           [self.x - 1, self.y + 1],
                           [self.x - 1, self.y - 1],
                           [self.x + 1, self.y]]
        elif self.orientation == 'left':
            coordinates = [[self.x, self.y],
                           [self.x, self.y + 1],
                           [self.x, self.y - 1],
                           [self.x + 1, self.y + 1],
                           [self.x + 1, self.y - 1],
                           [self.x - 1, self.y]]

        return coordinates
