# Файл game_exceptions.py буде містити спеціальні винятки, які будуть контролювати ігровий процес.

''' - **_Додаткове завдання:_**
    _Створити механізм збереження тільки топ 10 рекордів._'''
import datetime


class GameOver(Exception):
    ''' В класі має бути реалізований метод для збереження фінального рахунку гри по її завершенню.'''

    # записує результат в таблицю рекордів.
    # Додаткове завдання: Створити механізм збереження тільки топ 10 рекордів.
    def __init__(self, name,score ):
        GameOver(score, name)

    @staticmethod
    def save_score(score, name):
        with open('scores.txt', 'a+') as fl:
            fl.write(f"{name} | {score} | {datetime.datetime.now()}" + '\n')


class EnemyDown(Exception):
    ''' Функціонал не потрібен, тільки декларація.'''
    pass
