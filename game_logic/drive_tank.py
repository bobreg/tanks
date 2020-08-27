import keyboard
import threading
import time
import window.window
import window.object_tank


class FireBall:
    def __init__(self, game):
        self.game = game
        self.x = game.person_tank_object.x
        self.y = game.person_tank_object.y
        self.vector = game.person_tank_object.orientation

    def fire(self):
        if self.vector == 'top':
            for i in range(self.x - 3, -1, -1):
                self.game.m_win.tiles_massive[i][self.y]['bg'] = 'orange'
                self.game.m_win.tiles_massive[i+1][self.y]['bg'] = window.window.colour1
                time.sleep(0.05)
            self.game.m_win.tiles_massive[0][self.y]['bg'] = window.window.colour1
        elif self.vector == 'down':
            for i in range(self.x + 3, 35):
                self.game.m_win.tiles_massive[i][self.y]['bg'] = 'orange'
                self.game.m_win.tiles_massive[i-1][self.y]['bg'] = window.window.colour1
                time.sleep(0.05)
            self.game.m_win.tiles_massive[34][self.y]['bg'] = window.window.colour1
        elif self.vector == 'right':
            for i in range(self.y + 3, 35):
                self.game.m_win.tiles_massive[self.x][i]['bg'] = 'orange'
                self.game.m_win.tiles_massive[self.x][i-1]['bg'] = window.window.colour1
                time.sleep(0.05)
            self.game.m_win.tiles_massive[self.x][34]['bg'] = window.window.colour1
        elif self.vector == 'left':
            for i in range(self.y - 3, -1, -1):
                self.game.m_win.tiles_massive[self.x][i]['bg'] = 'orange'
                self.game.m_win.tiles_massive[self.x][i+1]['bg'] = window.window.colour1
                time.sleep(0.05)
            self.game.m_win.tiles_massive[self.x][0]['bg'] = window.window.colour1


class PersonTank:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.orientation = 'top'
        self.m_win = window.window.MainWindow()
        self.person_tank_object = window.object_tank.Tank()
        for i in self.person_tank_object.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank_object.colour

    def w_press(self):
        for i in self.person_tank_object.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = window.window.colour1
        if self.orientation == 'top' and self.x - 1 != 0:
            self.x -= 1
        self.orientation = 'top'
        for i in self.person_tank_object.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank_object.colour

    def a_press(self):
        for i in self.person_tank_object.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = window.window.colour1
        if self.orientation == 'left' and self.y - 1 != 0:
            self.y -= 1
        self.orientation = 'left'
        for i in self.person_tank_object.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank_object.colour

    def s_press(self):
        for i in self.person_tank_object.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = window.window.colour1
        if self.orientation == 'down' and self.x + 1 != 34:
            self.x += 1
        self.orientation = 'down'
        for i in self.person_tank_object.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank_object.colour

    def d_press(self):
        for i in self.person_tank_object.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = window.window.colour1
        if self.orientation == 'right' and self.y + 1 != 34:
            self.y += 1
        self.orientation = 'right'
        for i in self.person_tank_object.paint_tank(self.orientation, self.x, self.y):
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank_object.colour


def fire_ball_thread(flag, game):
    ball = FireBall(game)
    thread_ball = threading.Thread(target=ball.fire)
    thread_ball.start()


def drive_thread(flag, game):
    keyboard.add_hotkey('space', fire_ball_thread, args=(True, game), timeout=0.1)
    while flag is True:
        w_button = keyboard.is_pressed('w')
        a_button = keyboard.is_pressed('a')
        s_button = keyboard.is_pressed('s')
        d_button = keyboard.is_pressed('d')
        if w_button is True:
            game.w_press()
        if a_button is True:
            game.a_press()
        if s_button is True:
            game.s_press()
        if d_button is True:
            game.d_press()
        time.sleep(0.05)


if __name__ == '__main__':
    game = PersonTank()
    # game.m_win.win.bind('w', game.w_press)
    # game.m_win.win.bind('a', game.a_press)
    # game.m_win.win.bind('s', game.s_press)
    # game.m_win.win.bind('d', game.d_press)
    thread = threading.Thread(target=drive_thread, args=(True, game))
    thread.start()

    game.m_win.win_task()
