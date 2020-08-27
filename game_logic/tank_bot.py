import threading
import time
import window.window
import random
import window.object_tank

vector = ['top', 'down', 'left', 'right']


def go_bot_tank(flag=True):
    global vector
    wrong_vector = []
    while flag is True:
        if bot.flag_border is True:
            target_vector = random.choice(vector)
            while target_vector is wrong_vector:
                print(wrong_vector)
                target_vector = random.choice(vector)
        else:
            wrong_vector = []
            target_vector = random.choice(vector)
        count_step = random.randrange(5, 15)
        i = 0
        while i < count_step:
            if target_vector is 'top':
                if bot.flag_border is True:
                    wrong_vector.append(target_vector)
                    i = count_step
                bot.w_press()
            elif target_vector is 'down':
                if bot.flag_border is True:
                    wrong_vector.append(target_vector)
                    i = count_step
                bot.s_press()
            elif target_vector is 'left':
                if bot.flag_border is True:
                    wrong_vector.append(target_vector)
                    i = count_step
                bot.a_press()
            elif target_vector is 'right':
                if bot.flag_border is True:
                    wrong_vector.append(target_vector)
                    i = count_step
                bot.d_press()
            time.sleep(0.05)


if __name__ == '__main__':
    bot = window.object_tank.DriveTank('red')
    start_bot = threading.Thread(target=go_bot_tank)
    start_bot.start()
    bot.m_win.win_task()
