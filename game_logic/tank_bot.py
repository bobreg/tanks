import threading
import time
import window.window
import random
import window.object_tank

vector = ['top', 'down', 'left', 'right']


class ThreadBotTank:
    def __init__(self, m_win, colour, x, y):
        self.m_win = m_win
        self.colour = colour
        self.x = x
        self.y = y
        self.wrong_vector = []
        self.bot = window.object_tank.DriveTank(m_win, self.colour, self.x, self.y)
        self.start_bot = threading.Thread(target=lambda: ThreadBotTank.bot_tank_thread(self, True))

    def bot_tank_thread(self, flag=True):
        global vector
        while flag is True:
            if self.bot.flag_border is True:
                target_vector = random.choice(vector)
                while target_vector is self.wrong_vector:
                    target_vector = random.choice(vector)
                self.bot.flag_border = False
            else:
                self.wrong_vector = []
                target_vector = random.choice(vector)

            count_step = random.randrange(15, 20)
            i = 0
            while i < count_step:
                if target_vector == 'top':
                    if self.bot.flag_border is True:
                        self.wrong_vector += target_vector
                        i = count_step
                    else:
                        self.bot.w_press()
                elif target_vector == 'down':
                    if self.bot.flag_border is True:
                        self.wrong_vector += target_vector
                        i = count_step
                    else:
                        self.bot.s_press()
                elif target_vector == 'left':
                    if self.bot.flag_border is True:
                        self.wrong_vector += target_vector
                        i = count_step
                    else:
                        self.bot.a_press()
                elif target_vector == 'right':
                    if self.bot.flag_border is True:
                        self.wrong_vector += target_vector
                        i = count_step
                    else:
                        self.bot.d_press()
                i += 1
                time.sleep(0.1)

    def thread_bot_tank_start(self):
        self.start_bot.start()


if __name__ == '__main__':
    m_win = window.window.MainWindow()
    bot1 = ThreadBotTank(m_win, 'red', 3, 3)
    bot2 = ThreadBotTank(m_win, 'red', 31, 3)
    bot3 = ThreadBotTank(m_win, 'red', 31, 31)
    bot4 = ThreadBotTank(m_win, 'red', 3, 31)
    bot1.thread_bot_tank_start()
    bot2.thread_bot_tank_start()
    bot3.thread_bot_tank_start()
    bot4.thread_bot_tank_start()

    m_win.win_task()
