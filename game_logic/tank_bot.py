import threading
import time
import window.window
import constants.constants
import random
import window.object_tank


class ThreadBotTank:
    def __init__(self, m_win, colour, x, y):
        self.m_win = m_win
        self.colour = colour
        self.x = x
        self.y = y
        self.last_target = x
        self.target = 1
        self.wrong_vector = []
        self.bot = window.object_tank.DriveTank(m_win, self.colour, self.x, self.y)
        self.start_bot = threading.Thread(target=lambda: ThreadBotTank.bot_tank_thread(self, True))

    def likely_v(self, current_vectors):
        likely_vector = random.randrange(100)
        if likely_vector <= 30:
            return current_vectors[0]
        elif likely_vector <= 90:
            return current_vectors[1]
        elif likely_vector <= 100:
            return current_vectors[2]

    def choice_vector(self):
        current_vectors = constants.constants.VECTOR.copy()
        # хрень. это не работает
        if self.bot.x == 1 and (self.bot.y != 1 and self.bot.y != 31):
            current_vectors = ['right', 'down', 'left']
            return ThreadBotTank.likely_v(self, current_vectors)
        elif self.bot.y == 1 and (self.bot.x != 1 and self.bot.x != 31):
            current_vectors = ['down', 'right', 'top']
            return ThreadBotTank.likely_v(self, current_vectors)
        elif self.bot.x == 31 and (self.bot.y != 1 and self.bot.y != 31):
            current_vectors = ['left', 'top', 'right']
            return ThreadBotTank.likely_v(self, current_vectors)
        elif self.bot.y == 31 and (self.bot.x != 1 and self.bot.x != 31):
            current_vectors = ['top', 'left', 'down']
            return ThreadBotTank.likely_v(self, current_vectors)

        elif self.bot.x == 1 and self.bot.y == 1:
            current_vectors.remove('left')
            current_vectors.remove('top')
            return random.choice(current_vectors)
        elif self.bot.x == 31 and self.bot.y == 1:
            current_vectors.remove('left')
            current_vectors.remove('down')
            return random.choice(current_vectors)
        elif self.bot.x == 1 and self.bot.y == 31:
            current_vectors.remove('right')
            current_vectors.remove('top')
            return random.choice(current_vectors)
        elif self.bot.x == 31 and self.bot.y == 31:
            current_vectors.remove('right')
            current_vectors.remove('down')
            return random.choice(current_vectors)
        else:
            return random.choice(current_vectors)

    def attack(self, vector):
        if vector == 'top':
            for i in range(self.bot.x - 2, -1, -1):
                if self.bot.m_win.tiles_massive[i][self.bot.y]['bg'] == constants.constants.COLOUR_TANK_PERSON:
                    return True
        elif vector == 'down':
            for i in range(self.bot.x + 2, 31):
                if self.bot.m_win.tiles_massive[i][self.bot.y]['bg'] == constants.constants.COLOUR_TANK_PERSON:
                    return True
        elif vector == 'left':
            for i in range(self.bot.y - 2, -1, -1):
                if self.bot.m_win.tiles_massive[self.bot.x][i]['bg'] == constants.constants.COLOUR_TANK_PERSON:
                    return True
        elif vector == 'right':
            for i in range(self.bot.y + 2, 31):
                if self.bot.m_win.tiles_massive[self.bot.x][i]['bg'] == constants.constants.COLOUR_TANK_PERSON:
                    return True
        else:
            return False

    def bot_tank_thread(self, flag=True):
        while flag is True:
            if self.bot.flag_hit is True:
                break
                # тут нужно очищать поле от танка'
            else:
                self.target = random.choice(constants.constants.STEP_LIST)
                vector = ThreadBotTank.choice_vector(self)
                while (self.bot.x or self.bot.y) != self.target:
                    if ThreadBotTank.attack(self, vector) is True:
                        ball_bot = window.object_tank.FireBall(self.bot)
                        thread_ball = threading.Thread(target=ball_bot.fire)
                        thread_ball.start()
                        time.sleep(0.5)
                    self.bot.drive(vector)
                    if (self.bot.flag_border or self.bot.flag_barrier or self.bot.flag_hit) is True:
                        break
                    time.sleep(0.1)
        print('поток остановлен', self)

    def thread_bot_tank_start(self):
        self.start_bot.start()


if __name__ == '__main__':
    m_win = window.window.MainWindow()
    bot1 = ThreadBotTank(m_win, constants.constants.COLOUR_TANK_BOT, 1, 1)
    bot2 = ThreadBotTank(m_win, constants.constants.COLOUR_TANK_BOT, 31, 1)
    bot3 = ThreadBotTank(m_win, constants.constants.COLOUR_TANK_BOT, 31, 31)
    bot4 = ThreadBotTank(m_win, constants.constants.COLOUR_TANK_BOT, 1, 31)
    bot1.thread_bot_tank_start()
    bot2.thread_bot_tank_start()
    bot3.thread_bot_tank_start()
    bot4.thread_bot_tank_start()

    m_win.win_task()

'''
цикл движения
                    if target_vector == 'top':
                        if self.bot.flag_border is True or self.bot.flag_barrier is True:
                            self.wrong_vector += [target_vector]
                            i = count_step
                        else:
                            self.bot.drive(target_vector)
                    elif target_vector == 'down':
                        if self.bot.flag_border is True or self.bot.flag_barrier is True:
                            self.wrong_vector += [target_vector]
                            i = count_step
                        else:
                            self.bot.drive(target_vector)
                    elif target_vector == 'left':
                        if self.bot.flag_border is True or self.bot.flag_barrier is True:
                            self.wrong_vector += [target_vector]
                            i = count_step
                        else:
                            self.bot.drive(target_vector)
                    elif target_vector == 'right':
                        if self.bot.flag_border is True or self.bot.flag_barrier is True:
                            self.wrong_vector += [target_vector]
                            i = count_step
                        else:
                            self.bot.drive(target_vector)
'''

'''
старый алгоритм движения
            if self.bot.flag_hit is True:
                break
                # тут нужно очищать поле от танка'
            else:
                if self.bot.flag_border is True or self.bot.flag_barrier is True:
                    target_vector = random.choice(constants.constants.VECTOR)
                    while target_vector in self.wrong_vector:
                        target_vector = random.choice(constants.constants.VECTOR)
                    self.bot.flag_border = False
                    self.bot.flag_barrier = False
                    self.wrong_vector = []
                else:
                    target_vector = random.choice(constants.constants.VECTOR)

                i = self.target
                self.target = random.choice(constants.constants.STEP_LIST)
                while i != self.target:
                    if self.bot.flag_border is True or self.bot.flag_barrier is True:
                        self.wrong_vector += [target_vector]
                        i = self.target
                    else:
                        self.bot.drive(target_vector)
                    if i < self.target:
                        i += 1
                    elif i > self.target:
                        i -= 1
                    time.sleep(0.1)
'''
