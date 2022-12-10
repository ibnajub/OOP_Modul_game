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
    '''
- Гравець вводить ім'я
- Створюється об'єкт player
- level = 1
- Створюється об'єкт enemy.
- В бескінечному циклі викликаються методи attack та defence об'єкту player
- при виникненні винятку EnemyDown підвищує рівень гри на 1, створює новий об'єкт Enemy з новим рівнем '''

    name = input('Input you name: ')
    while True:
        command = input('input start or help:')
        if command == 'help':
            print(settings.HELP_CONST)
        elif command == 'start':
            break
        elif command == 'show scores':
            # виводить записи із файлу scores.txt
            read_score('scores.txt')

        elif command == 'exit':
            raise KeyboardInterrupt

        else:
            print('Wrong command!')

    player = models.Player(name, settings.PLAYER_LIVES_CONST, settings.ALLOWED_ATTACKS_CONST)
    level = settings.GAME_LEVEL_CONST
    enemy = models.Enemy(level)
    while True:
        try:
            player.attack(enemy)
            # подсчет балов
        except game_exceptions.EnemyDown:
            player.score += 5
            level += 1
            print(f'-----Enemy down!----- scores: {player.score}')
            enemy = models.Enemy(level)

        player.defence(enemy)
        # подсчет балов


def read_score(file):
    with open('scores.txt') as fl:
        print('-------SCORE TABLE-------\n'
              '-rank- | -name- | -score- | -date-')
        rank = 1
        for string in fl:
            print(f' {rank} | {string}\n')
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
        print("\nGood bye!")
