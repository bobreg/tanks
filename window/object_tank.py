import tkinter


class Tank:
    def __init__(self, colour='black', x=10, y=10, orientation='top'):
        self.colour = colour
        self.x = x
        self.y = y
        self.orientation = orientation
        self.coordinates = [[self.x, self.y],
                            [self.x - 1, self.y],
                            [self.x + 1, self.y],
                            [self.x - 1, self.y + 1],
                            [self.x + 1, self.y + 1],
                            [self.x, self.y - 1]]

    def paint_tank(self, orientation, x, y):
        self.x = x
        self.y = y
        self.orientation = orientation
        if self.orientation == 'left':
            self.coordinates = [[self.x, self.y],
                                [self.x - 1, self.y],
                                [self.x + 1, self.y],
                                [self.x - 1, self.y + 1],
                                [self.x + 1, self.y + 1],
                                [self.x, self.y - 1]]
        elif self.orientation == 'right':
            self.coordinates = [[self.x, self.y],
                                [self.x - 1, self.y],
                                [self.x + 1, self.y],
                                [self.x - 1, self.y - 1],
                                [self.x + 1, self.y - 1],
                                [self.x, self.y + 1]]
        elif self.orientation == 'down':
            self.coordinates = [[self.x, self.y],
                                [self.x, self.y + 1],
                                [self.x, self.y - 1],
                                [self.x - 1, self.y + 1],
                                [self.x - 1, self.y - 1],
                                [self.x + 1, self.y]]
        elif self.orientation == 'top':
            self.coordinates = [[self.x, self.y],
                                [self.x, self.y + 1],
                                [self.x, self.y - 1],
                                [self.x + 1, self.y + 1],
                                [self.x + 1, self.y - 1],
                                [self.x - 1, self.y]]

        return self.coordinates
