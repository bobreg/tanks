import threading
import time
import window.window
import random
import window.object_tank

vector = ['top', 'down', 'left', 'right']


def go_bot_tank(bot, flag=True):
    global vector
    wrong_vector = []
    while flag is True:
        if bot.flag_border is True:
            target_vector = random.choice(vector)
            while target_vector is wrong_vector:
                target_vector = random.choice(vector)
            bot.flag_border = False
        else:
            wrong_vector = []
            target_vector = random.choice(vector)

        count_step = random.randrange(15, 20)
        i = 0
        while i < count_step:
            if target_vector == 'top':
                if bot.flag_border is True:
                    wrong_vector += target_vector
                    i = count_step
                else:
                    bot.w_press()
            elif target_vector == 'down':
                if bot.flag_border is True:
                    wrong_vector += target_vector
                    i = count_step
                else:
                    bot.s_press()
            elif target_vector == 'left':
                if bot.flag_border is True:
                    wrong_vector += target_vector
                    i = count_step
                else:
                    bot.a_press()
            elif target_vector == 'right':
                if bot.flag_border is True:
                    wrong_vector += target_vector
                    i = count_step
                else:
                    bot.d_press()
            i += 1
            time.sleep(0.07)


if __name__ == '__main__':
    m_win = window.window.MainWindow()
    bot1 = window.object_tank.DriveTank(m_win, 'red')
    bot2 = window.object_tank.DriveTank(m_win, 'red')
    bot3 = window.object_tank.DriveTank(m_win, 'red')
    bot4 = window.object_tank.DriveTank(m_win, 'red')
    start_bot1 = threading.Thread(target=go_bot_tank, args=(bot1, True))
    start_bot1.start()
    start_bot2 = threading.Thread(target=go_bot_tank, args=(bot2, True))
    start_bot2.start()
    start_bot3 = threading.Thread(target=go_bot_tank, args=(bot3, True))
    start_bot3.start()
    start_bot4 = threading.Thread(target=go_bot_tank, args=(bot4, True))
    start_bot4.start()
    m_win.win_task()
