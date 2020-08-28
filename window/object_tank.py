import window.window
import time


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


class FireBall:
    def __init__(self, game):
        self.game = game
        self.x = game.person_tank.x
        self.y = game.person_tank.y
        self.vector = game.person_tank.orientation
        self.time_pause = 0.05

    def fire(self):
        if self.vector == 'top':
            for i in range(self.x - 3, -1, -1):
                self.game.m_win.tiles_massive[i][self.y]['bg'] = 'orange'
                self.game.m_win.tiles_massive[i+1][self.y]['bg'] = window.window.colour1
                time.sleep(self.time_pause)
            self.game.m_win.tiles_massive[0][self.y]['bg'] = window.window.colour1
        elif self.vector == 'down':
            for i in range(self.x + 3, 35):
                self.game.m_win.tiles_massive[i][self.y]['bg'] = 'orange'
                self.game.m_win.tiles_massive[i-1][self.y]['bg'] = window.window.colour1
                time.sleep(self.time_pause)
            self.game.m_win.tiles_massive[34][self.y]['bg'] = window.window.colour1
        elif self.vector == 'right':
            for i in range(self.y + 3, 35):
                self.game.m_win.tiles_massive[self.x][i]['bg'] = 'orange'
                self.game.m_win.tiles_massive[self.x][i-1]['bg'] = window.window.colour1
                time.sleep(self.time_pause)
            self.game.m_win.tiles_massive[self.x][34]['bg'] = window.window.colour1
        elif self.vector == 'left':
            for i in range(self.y - 3, -1, -1):
                self.game.m_win.tiles_massive[self.x][i]['bg'] = 'orange'
                self.game.m_win.tiles_massive[self.x][i+1]['bg'] = window.window.colour1
                time.sleep(self.time_pause)
            self.game.m_win.tiles_massive[self.x][0]['bg'] = window.window.colour1


class DriveTank:
    def __init__(self, m_win, colour='black', x=10, y=10):
        self.x = x
        self.y = y
        self.orientation = 'top'
        self.m_win = m_win
        self.person_tank = window.object_tank.Tank(colour)
        self.flag_border = False
        for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour

    def w_press(self):
        if self.x - 1 != 0:
            if self.m_win.tiles_massive[self.x - 2][self.y]['bg'] == window.window.colour1 and \
               self.m_win.tiles_massive[self.x - 2][self.y + 1]['bg'] == window.window.colour1 and \
               self.m_win.tiles_massive[self.x - 2][self.y - 1]['bg'] == window.window.colour1:
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = window.window.colour1
                self.x -= 1
                self.orientation = 'top'
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour
            else:
                self.flag_border = True
        else:
            self.flag_border = True

    def a_press(self):
        if self.y - 1 != 0:
            if self.m_win.tiles_massive[self.x][self.y - 2]['bg'] == window.window.colour1 and \
               self.m_win.tiles_massive[self.x + 1][self.y - 2]['bg'] == window.window.colour1 and \
               self.m_win.tiles_massive[self.x - 1][self.y - 2]['bg'] == window.window.colour1:
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = window.window.colour1
                self.y -= 1
                self.orientation = 'left'
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour
            else:
                self.flag_border = True
        else:
            self.flag_border = True

    def s_press(self):
        if self.x + 1 != 34:
            if self.m_win.tiles_massive[self.x + 2][self.y]['bg'] == window.window.colour1 and \
                    self.m_win.tiles_massive[self.x + 2][self.y + 1]['bg'] == window.window.colour1 and \
                    self.m_win.tiles_massive[self.x + 2][self.y - 1]['bg'] == window.window.colour1:
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = window.window.colour1
                self.x += 1
                self.orientation = 'down'
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour
            else:
                self.flag_border = True
        else:
            self.flag_border = True

    def d_press(self):
        if self.y + 1 != 34:
            if self.m_win.tiles_massive[self.x][self.y + 2]['bg'] == window.window.colour1 and \
                    self.m_win.tiles_massive[self.x + 1][self.y + 2]['bg'] == window.window.colour1 and \
                    self.m_win.tiles_massive[self.x - 1][self.y + 2]['bg'] == window.window.colour1:
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = window.window.colour1
                self.y += 1
                self.orientation = 'right'
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour
            else:
                self.flag_border = True
        else:
            self.flag_border = True
