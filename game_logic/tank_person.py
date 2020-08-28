import keyboard
import threading
import time
import window.window
import window.object_tank


class DriveTankPerson:
    def __init__(self, m_win):
        self.m_win = m_win
        self.game = window.object_tank.DriveTank(self.m_win)
        self.thread = threading.Thread(target=lambda: DriveTankPerson.drive_thread(self, True))
        self.ball = None
        self.thread_ball = None

    def fire_ball_thread(self):
        self.ball = window.object_tank.FireBall(self.game)
        self.thread_ball = threading.Thread(target=self.ball.fire)
        self.thread_ball.start()

    def drive_thread(self, flag):
        while flag is True:
            w_button = keyboard.is_pressed('w')
            a_button = keyboard.is_pressed('a')
            s_button = keyboard.is_pressed('s')
            d_button = keyboard.is_pressed('d')
            space_button = keyboard.is_pressed('space')
            if w_button is True:
                self.game.w_press()
            if a_button is True:
                self.game.a_press()
            if s_button is True:
                self.game.s_press()
            if d_button is True:
                self.game.d_press()
            if space_button is True:
                DriveTankPerson.fire_ball_thread(self)
                time.sleep(0.1)
            time.sleep(0.1)

    def thread_person_tank_start(self):
        self.thread.start()


if __name__ == '__main__':
    main_win = window.window.MainWindow()
    game = DriveTankPerson(main_win)
    game.thread_person_tank_start()
    game.m_win.win_task()
