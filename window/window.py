import tkinter
import constants.constants


class MainWindow:
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.geometry('1024x768')
        self.win.title('Танчики от Alex_Chel_Man Inc.')

        self.pole = tkinter.Frame(self.win, relief='sunken', borderwidth=3)
        self.pole.place(x=10, y=10)

        self.tiles_massive = list()
        for i in range(constants.constants.SIZE_POLE):
            self.tiles_massive.append([])
            for j in range(constants.constants.SIZE_POLE):
                self.tiles_massive[i] += [tkinter.Label(self.pole, height=1, width=2, borderwidth=1, relief='raised',
                                                        bg=constants.constants.COLOUR_GAME_POLE)]
                self.tiles_massive[i][j].grid(row=i, column=j)

        for i in range(3, constants.constants.SIZE_POLE - 3, 6):
            for j in range(3, constants.constants.SIZE_POLE - 3, 6):
                for k in range(3):
                    for m in range(3):
                        self.tiles_massive[i+k][j+m]['bg'] = constants.constants.COLOUR_GAME_BORDER

    def win_task(self):
        self.win.mainloop()


if __name__ == '__main__':
    m_win = MainWindow()
    m_win.win_task()

