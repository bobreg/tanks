import tkinter
import window.window
import window.object_tank
import threading


class DriveTank:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.orientation = 'top'
        self.m_win = window.window.MainWindow()
        # self.m_win.win.bind('w', DriveTank.w_press)
        # self.m_win.win.bind('a', DriveTank.a_press)
        # self.m_win.win.bind('s', DriveTank.s_press)
        # self.m_win.win.bind('d', DriveTank.d_press)
        self.person_tank = window.object_tank.Tank()
        for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour

    def w_press(self, event):
        for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = 'tan1'
        self.y += 1
        self.orientation = 'top'
        for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour

    def a_press(self, event):
        for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = 'tan1'
        self.x -= 1
        self.orientation = 'left'
        for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour

    def s_press(self, event):
        for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = 'tan1'
        self.y += 1
        self.orientation = 'down'
        for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour

    def d_press(self, event):
        for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = 'tan1'
        self.y += 1
        self.orientation = 'right'
        for i in self.person_tank.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour


if __name__ == '__main__':
    game = DriveTank()
    game.m_win.win.bind('w', game.w_press)
    game.m_win.win.bind('a', game.a_press)
    game.m_win.win.bind('s', game.s_press)
    game.m_win.win.bind('d', game.d_press)
    game.m_win.win_task()
