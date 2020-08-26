import tkinter


def main_window():
    win = tkinter.Tk()
    win.geometry('1024x768')
    win.title('Танчики от Alex_Chel_Man Inc.')

    pole = tkinter.Frame(win, relief='sunken', borderwidth=3)
    pole.place(x=10, y=10)

    tiles_massive = list()
    for i in range(35):
        tiles_massive.append([])
        for j in range(35):
            tiles_massive[i] += [tkinter.Label(pole, height=1, width=2, borderwidth=1, relief='raised')]
            tiles_massive[i][j].grid(row=i, column=j)

    win.mainloop()


if __name__ == '__main__':
    main_window()
