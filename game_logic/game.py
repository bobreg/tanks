import game_logic.tank_bot
import game_logic.tank_person
import window.window


def new_game():
    main_window = window.window.MainWindow()
    person = game_logic.tank_person.DriveTankPerson(main_window)
    bot1 = game_logic.tank_bot.ThreadBotTank(main_window, 'red', 3, 3)
    bot2 = game_logic.tank_bot.ThreadBotTank(main_window, 'red', 31, 31)
    bot3 = game_logic.tank_bot.ThreadBotTank(main_window, 'red', 31, 3)
    bot4 = game_logic.tank_bot.ThreadBotTank(main_window, 'red', 3, 31)
    person.thread_person_tank_start()
    bot1.thread_bot_tank_start()
    bot2.thread_bot_tank_start()
    bot3.thread_bot_tank_start()
    bot4.thread_bot_tank_start()
    main_window.win_task()


if __name__ == '__main__':
    new_game()
