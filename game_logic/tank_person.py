import keyboard
import threading
import time
import window.window
import window.object_tank


def fire_ball_thread(flag, game):
    ball = window.object_tank.FireBall(game)
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
    game = window.object_tank.DriveTank()
    thread = threading.Thread(target=drive_thread, args=(True, game))
    thread.start()

    game.m_win.win_task()
