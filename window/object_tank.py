import window.window
import constants.constants
import time


class Tank:
    def __init__(self, colour='black', x=10, y=10, orientation='top'):
        self.colour = colour  # цвет танка
        self.x = x  # положение центра танка
        self.y = y
        self.orientation = orientation  # ориентация танка
        self.coordinates = [[self.x, self.y],
                            [self.x, self.y + 1],
                            [self.x, self.y - 1],
                            [self.x + 1, self.y + 1],
                            [self.x + 1, self.y - 1],
                            [self.x - 1, self.y]]  # координаты частей тела танка
        self.coordinates_add = [[self.x - 1, self.y + 1], [self.x - 1, self.y - 1], [self.x + 1, self.y]]
        # координаты частей поля в квадрате танка

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
            self.coordinates_add = [[self.x, self.y + 1], [self.x - 1, self.y - 1], [self.x + 1, self.y - 1]]
        elif self.orientation == 'right':
            self.coordinates = [[self.x, self.y],
                                [self.x - 1, self.y],
                                [self.x + 1, self.y],
                                [self.x - 1, self.y - 1],
                                [self.x + 1, self.y - 1],
                                [self.x, self.y + 1]]
            self.coordinates_add = [[self.x, self.y - 1], [self.x - 1, self.y + 1], [self.x + 1, self.y + 1]]
        elif self.orientation == 'down':
            self.coordinates = [[self.x, self.y],
                                [self.x, self.y + 1],
                                [self.x, self.y - 1],
                                [self.x - 1, self.y + 1],
                                [self.x - 1, self.y - 1],
                                [self.x + 1, self.y]]
            self.coordinates_add = [[self.x - 1, self.y], [self.x + 1, self.y - 1], [self.x + 1, self.y + 1]]
        elif self.orientation == 'top':
            self.coordinates = [[self.x, self.y],
                                [self.x, self.y + 1],
                                [self.x, self.y - 1],
                                [self.x + 1, self.y + 1],
                                [self.x + 1, self.y - 1],
                                [self.x - 1, self.y]]
            self.coordinates_add = [[self.x - 1, self.y + 1], [self.x - 1, self.y - 1], [self.x + 1, self.y]]

        return self.coordinates, self.coordinates_add


class FireBall:
    def __init__(self, game):
        self.game = game
        self.x = game.person_tank.x
        self.y = game.person_tank.y
        self.vector = game.person_tank.orientation
        self.time_pause = 0.05
        self.flag_hit_border = False

    def fire(self):
        if self.vector == 'top':
            for i in range(self.x - 3, -1, -1):
                if self.game.m_win.tiles_massive[i][self.y]['bg'] == constants.constants.COLOUR_GAME_BORDER:
                    self.flag_hit_border = True
                else:
                    if self.game.m_win.tiles_massive[i][self.y]['bg'] == constants.constants.COLOUR_TANK_PERSON or \
                            self.game.m_win.tiles_massive[i][self.y]['bg'] == constants.constants.COLOUR_TANK_BOT:
                        self.flag_hit_border = True
                    self.game.m_win.tiles_massive[i][self.y]['bg'] = constants.constants.COLOUR_BULLET
                    self.game.m_win.tiles_massive[i+1][self.y]['bg'] = constants.constants.COLOUR_GAME_POLE
                time.sleep(self.time_pause)
                if self.flag_hit_border is True:
                    break
            self.game.m_win.tiles_massive[0][self.y]['bg'] = constants.constants.COLOUR_GAME_POLE
        elif self.vector == 'down':
            for i in range(self.x + 3, constants.constants.SIZE_POLE):
                if self.game.m_win.tiles_massive[i][self.y]['bg'] == constants.constants.COLOUR_GAME_BORDER:
                    self.flag_hit_border = True
                else:
                    if self.game.m_win.tiles_massive[i][self.y]['bg'] == constants.constants.COLOUR_TANK_PERSON or \
                            self.game.m_win.tiles_massive[i][self.y]['bg'] == constants.constants.COLOUR_TANK_BOT:
                        self.flag_hit_border = True
                    self.game.m_win.tiles_massive[i][self.y]['bg'] = constants.constants.COLOUR_BULLET
                    self.game.m_win.tiles_massive[i-1][self.y]['bg'] = constants.constants.COLOUR_GAME_POLE
                time.sleep(self.time_pause)
                if self.flag_hit_border is True:
                    break
            self.game.m_win.tiles_massive[constants.constants.SIZE_POLE - 1][self.y]['bg'] = \
                constants.constants.COLOUR_GAME_POLE
        elif self.vector == 'right':
            for i in range(self.y + 3, constants.constants.SIZE_POLE):
                if self.game.m_win.tiles_massive[self.x][i]['bg'] == constants.constants.COLOUR_GAME_BORDER:
                    self.flag_hit_border = True
                else:
                    if self.game.m_win.tiles_massive[self.x][i]['bg'] == constants.constants.COLOUR_TANK_PERSON or \
                            self.game.m_win.tiles_massive[self.x][i]['bg'] == constants.constants.COLOUR_TANK_BOT:
                        self.flag_hit_border = True
                    self.game.m_win.tiles_massive[self.x][i]['bg'] = constants.constants.COLOUR_BULLET
                    self.game.m_win.tiles_massive[self.x][i-1]['bg'] = constants.constants.COLOUR_GAME_POLE
                time.sleep(self.time_pause)
                if self.flag_hit_border is True:
                    break
            self.game.m_win.tiles_massive[self.x][constants.constants.SIZE_POLE - 1]['bg'] = \
                constants.constants.COLOUR_GAME_POLE
        elif self.vector == 'left':
            for i in range(self.y - 3, -1, -1):
                if self.game.m_win.tiles_massive[self.x][i]['bg'] == constants.constants.COLOUR_GAME_BORDER:
                    self.flag_hit_border = True
                else:
                    if self.game.m_win.tiles_massive[self.x][i]['bg'] == constants.constants.COLOUR_TANK_PERSON or \
                            self.game.m_win.tiles_massive[self.x][i]['bg'] == constants.constants.COLOUR_TANK_BOT:
                        self.flag_hit_border = True
                    self.game.m_win.tiles_massive[self.x][i]['bg'] = constants.constants.COLOUR_BULLET
                    self.game.m_win.tiles_massive[self.x][i+1]['bg'] = constants.constants.COLOUR_GAME_POLE
                time.sleep(self.time_pause)
                if self.flag_hit_border is True:
                    break
            self.game.m_win.tiles_massive[self.x][0]['bg'] = constants.constants.COLOUR_GAME_POLE


class DriveTank:
    def __init__(self, m_win, colour='black', x=10, y=10):
        self.x = x  # текушие координаты танка
        self.y = y
        self.last_x = self.x  # предыдущие координаты танка
        self.last_y = self.y
        self.correction_x = 0  # коэфициенты смещение танка в зависимости от направления
        self.correction_y = 0
        self.border = 0  # переменная для уточнения достижения границы поля
        self.orientation = 'top'
        self.last_orientation = 'top'
        self.check_list_new_step = [[0, 0], [0, 0], [0, 0]]  # массив коэф.для проверки наличия препятствия перед танком
        self.m_win = m_win  # переменная класса текущего игрового окна
        self.person_tank = window.object_tank.Tank(colour)
        self.flag_border = False
        self.flag_hit = False
        self.flag_barrier = False
        for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour

    def check_available_step(self):  # проверка на препятствия
        if self.m_win.tiles_massive[self.x + self.check_list_new_step[0][0]][self.y + self.check_list_new_step[0][1]]['bg'] == constants.constants.COLOUR_GAME_POLE and \
                self.m_win.tiles_massive[self.x + self.check_list_new_step[1][0]][self.y + self.check_list_new_step[1][1]]['bg'] == constants.constants.COLOUR_GAME_POLE and \
                self.m_win.tiles_massive[self.x + self.check_list_new_step[2][0]][self.y + self.check_list_new_step[2][1]]['bg'] == constants.constants.COLOUR_GAME_POLE:
            return True
        else:
            return False

    def check_hit(self):
        for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
            if self.m_win.tiles_massive[i[0]][i[1]]['bg'] == constants.constants.COLOUR_BULLET:
                return True
        return False

    def paint_step(self):  # отрисовка нового положения танка
        for i in self.person_tank.paint_tank(self.last_orientation, self.last_x, self.last_y)[0]:
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = constants.constants.COLOUR_GAME_POLE
        for i in self.person_tank.paint_tank(self.last_orientation, self.last_x, self.last_y)[1]:
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = constants.constants.COLOUR_GAME_POLE
        for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
            self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour

    def drive(self, orientation):
        if orientation == 'top':
            self.border = self.x - 1
            self.check_list_new_step = [[-2, 0], [-2, -1], [-2, 1]]
            if orientation != self.orientation:
                self.last_orientation = self.orientation
                self.orientation = orientation
            else:
                self.last_orientation = self.orientation
                self.correction_x = -1
                self.correction_y = 0
        elif orientation == 'left':
            self.border = self.y - 1
            self.check_list_new_step = [[-1, -2], [0, -2], [1, -2]]
            if orientation != self.orientation:
                self.last_orientation = self.orientation
                self.orientation = orientation
            else:
                self.last_orientation = self.orientation
                self.correction_x = 0
                self.correction_y = -1
        elif orientation == 'down':
            self.border = self.x + 1
            self.check_list_new_step = [[2, 0], [2, -1], [2, 1]]
            if orientation != self.orientation:
                self.last_orientation = self.orientation
                self.orientation = orientation
            else:
                self.last_orientation = self.orientation
                self.correction_x = 1
                self.correction_y = 0
        elif orientation == 'right':
            self.border = self.y + 1
            self.check_list_new_step = [[-1, 2], [0, 2], [1, 2]]
            if orientation != self.orientation:
                self.last_orientation = self.orientation
                self.orientation = orientation
            else:
                self.last_orientation = self.orientation
                self.correction_x = 0
                self.correction_y = 1
        if DriveTank.check_hit(self) is False and self.flag_hit is False:
            if self.border != 0 and self.border != constants.constants.SIZE_POLE - 1:  # если не вышли за границы поля
                self.flag_border = False
                if DriveTank.check_available_step(self) is True:  # если перед танком нет препятствия
                    self.flag_barrier = False
                    self.last_x = self.x
                    self.last_y = self.y
                    self.x += self.correction_x  # сдвинем координату положения танка
                    self.y += self.correction_y
                    DriveTank.paint_step(self)
                else:
                    self.flag_barrier = True
                    DriveTank.paint_step(self)
            else:
                self.flag_border = True
                DriveTank.paint_step(self)
        else:
            self.flag_hit = True
            for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
                self.m_win.tiles_massive[i[0]][i[1]]['bg'] = constants.constants.COLOUR_GAME_POLE
        self.correction_x = 0  # сбросим сдвиг танка и коэффициенты на проверку возможности хода
        self.correction_y = 0
        self.check_list_new_step = [[0, 0], [0, 0], [0, 0]]
'''
    def w_press(self):
        if self.x - 1 != 0:  # если не вышли за границы поля
            if self.m_win.tiles_massive[self.x - 2][self.y]['bg'] == constants.constants.COLOUR_GAME_POLE and \
                    self.m_win.tiles_massive[self.x - 2][self.y + 1]['bg'] == constants.constants.COLOUR_GAME_POLE and \
                    self.m_win.tiles_massive[self.x - 2][self.y - 1]['bg'] == constants.constants.COLOUR_GAME_POLE:  # если перед танком нет препятствия
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:  # перекрасим положение танка в цвет поля
                    if self.m_win.tiles_massive[i[0]][i[1]]['bg'] == constants.constants.COLOUR_BULLET:           # проверим не попал ли в танк выстрел
                        self.flag_hit = True
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = constants.constants.COLOUR_GAME_POLE
                if self.orientation == 'top':
                    self.x -= 1  # сдвинем координату положения танка
                self.orientation = 'top'  # поменяем ориентацию танка для этого направления
                if self.flag_hit is False:  # если в танк не попали, то нарисуем новое положение танка
                    for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
                        self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour
            else:
                self.flag_barrier = True
                self.orientation = 'top'
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[1]:
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = constants.constants.COLOUR_GAME_POLE
        else:
            self.flag_border = True

    def a_press(self):
        if self.y - 1 != 0:
            if self.m_win.tiles_massive[self.x][self.y - 2]['bg'] == constants.constants.COLOUR_GAME_POLE and \
               self.m_win.tiles_massive[self.x + 1][self.y - 2]['bg'] == constants.constants.COLOUR_GAME_POLE and \
               self.m_win.tiles_massive[self.x - 1][self.y - 2]['bg'] == constants.constants.COLOUR_GAME_POLE:
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
                    if self.m_win.tiles_massive[i[0]][i[1]]['bg'] == constants.constants.COLOUR_BULLET:
                        self.flag_hit = True
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = constants.constants.COLOUR_GAME_POLE
                if self.orientation == 'left':
                    self.y -= 1
                self.orientation = 'left'
                if self.flag_hit is False:
                    for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
                        self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour
                    for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[1]:
                        self.m_win.tiles_massive[i[0]][i[1]]['bg'] = constants.constants.COLOUR_GAME_POLE
            else:
                self.flag_barrier = True
                self.orientation = 'left'
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[1]:
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = constants.constants.COLOUR_GAME_POLE
        else:
            self.flag_border = True

    def s_press(self):
        if self.x + 1 != constants.constants.SIZE_POLE - 1:
            if self.m_win.tiles_massive[self.x + 2][self.y]['bg'] == constants.constants.COLOUR_GAME_POLE and \
                    self.m_win.tiles_massive[self.x + 2][self.y + 1]['bg'] == constants.constants.COLOUR_GAME_POLE and \
                    self.m_win.tiles_massive[self.x + 2][self.y - 1]['bg'] == constants.constants.COLOUR_GAME_POLE:
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
                    if self.m_win.tiles_massive[i[0]][i[1]]['bg'] == constants.constants.COLOUR_BULLET:
                        self.flag_hit = True
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = constants.constants.COLOUR_GAME_POLE
                if self.orientation == 'down':
                    self.x += 1
                self.orientation = 'down'
                if self.flag_hit is False:
                    for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
                        self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour
                    for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[1]:
                        self.m_win.tiles_massive[i[0]][i[1]]['bg'] = constants.constants.COLOUR_GAME_POLE
            else:
                self.flag_barrier = True
                self.orientation = 'down'
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[1]:
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = constants.constants.COLOUR_GAME_POLE

        else:
            self.flag_border = True

    def d_press(self):
        if self.y + 1 != constants.constants.SIZE_POLE - 1:
            if self.m_win.tiles_massive[self.x][self.y + 2]['bg'] == constants.constants.COLOUR_GAME_POLE and \
                    self.m_win.tiles_massive[self.x + 1][self.y + 2]['bg'] == constants.constants.COLOUR_GAME_POLE and \
                    self.m_win.tiles_massive[self.x - 1][self.y + 2]['bg'] == constants.constants.COLOUR_GAME_POLE:
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
                    if self.m_win.tiles_massive[i[0]][i[1]]['bg'] == constants.constants.COLOUR_BULLET:
                        self.flag_hit = True
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = constants.constants.COLOUR_GAME_POLE
                if self.orientation == 'right':
                    self.y += 1
                self.orientation = 'right'
                if self.flag_hit is False:
                    for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
                        self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour
                    for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[1]:
                        self.m_win.tiles_massive[i[0]][i[1]]['bg'] = constants.constants.COLOUR_GAME_POLE
            else:
                self.flag_barrier = True
                self.orientation = 'right'
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour
                for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[1]:
                    self.m_win.tiles_massive[i[0]][i[1]]['bg'] = constants.constants.COLOUR_GAME_POLE
        else:
            self.flag_border = True
'''

'''
попадание пули
if self.m_win.tiles_massive[i[0]][i[1]]['bg'] == constants.constants.COLOUR_BULLET:           # проверим не попал ли в танк выстрел
    self.flag_hit = True
if self.flag_hit is False:  # если в танк не попали, то нарисуем новое положение танка
    for i in self.person_tank.paint_tank(self.orientation, self.x, self.y)[0]:
        self.m_win.tiles_massive[i[0]][i[1]]['bg'] = self.person_tank.colour
'''