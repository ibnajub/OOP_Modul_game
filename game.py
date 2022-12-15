# Файл game.py - основний файл, який запускається для гри.

import settings
import game_exceptions
import models

'''
- Містить блок на перевірку імені модуля (main)
- В середині if блок try/except.
- try запускає функцію play()
- except обробляє два винятки:
  - GameOver - виводить на екран повідомлення про завершення гри, записує результат в таблицю рекордів.
  - KeyboardInterrupt - pass.
- finally виводить на екран "Good bye!" '''


def play():
    """
- Гравець вводить ім'я
- Створюється об'єкт player
- level = 1
- Створюється об'єкт enemy.
- В бескінечному циклі викликаються методи attack та defence об'єкту player
- при виникненні винятку EnemyDown підвищує рівень гри на 1, створює новий об'єкт Enemy з новим рівнем """

    name = input('Input you name: ')
    mode_multiplayer = 1
    while True:
        command = input('input "start" or "start hard" or "help":')
        if command == 'help':
            print(settings.HELP_CONST)
        elif command == 'start':
            break
        elif command == 'start hard':
            mode_multiplayer = settings.HARD_MODE_MULTIPLAYER_CONST
            break
        elif command == 'show scores':
            # виводить записи із файлу scores.txt
            read_score(settings.FILE_SCORES_CONST)

        elif command == 'exit':
            raise KeyboardInterrupt

        else:
            print('Wrong command!')

    player = models.Player(name, settings.PLAYER_LIVES_CONST, mode_multiplayer, settings.ALLOWED_ATTACKS_CONST)
    level = settings.GAME_LEVEL_CONST
    lives = level * mode_multiplayer
    enemy = models.Enemy(level, lives)
    while True:
        try:
            player.attack(enemy)
            # подсчет балов
        except game_exceptions.EnemyDown:
            player.score += 5 * mode_multiplayer
            print(f'-----Enemy down!----- scores: {player.score}')
            level += 1
            lives = level * mode_multiplayer
            enemy = models.Enemy(level, lives)

        player.defence(enemy)
        # подсчет балов


def read_score(file):
    with open(file) as fl:
        print('-------SCORE TABLE-------\n'
              '-rank- | -name- | -score- | -date-')
        rank = 1
        for string in fl:
            # перенос строки есть уже в файле потому выключим перенос в самом print  end='' иначе лишняя строка
            print(f'  {rank}  |  {string}', end='')
            rank += 1


# ---------------------------
if __name__ == '__main__':
    try:
        play()
    except game_exceptions.GameOver:
        print("Game Over!")

    except KeyboardInterrupt:
        pass

    finally:
        read_score(settings.FILE_SCORES_CONST)
        print("\n---Good bye!----")
