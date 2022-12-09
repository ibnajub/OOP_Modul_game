#Файл game.py - основний файл, який запускається для гри.

import  settings
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
   player =  models.Player(name, settings.PLAYER_LIVES_CONST, settings.GAME_LEVEL_CONST)
   enemy = models.Enemy(settings.ENEMY_LIVES_CONST )
    while true:
        try:
           player.attack(enemy)
           # подсчет балов
        except game_exceptions.EnemyDown:
            settings.GAME_LEVEL_CONST += 1
            level = settings.ENEMY_LIVES_CONST + settings.GAME_LEVEL_CONST
            enemy = models.Enemy( level )


   player.defence(enemy_obj)
    # подсчет балов



if __name__ == '__main__':
    try:
        play()
    except game_exceptions.GameOver:
        print("Game Over!")

    except KeyboardInterrupt:
        pass


    finally:
        print("Good bye!")

