# Файл game_exceptions.py буде містити спеціальні винятки, які будуть контролювати ігровий процес.

''' - **_Додаткове завдання:_**
    _Створити механізм збереження тільки топ 10 рекордів._'''
import datetime


class GameOver(Exception):
    ''' В класі має бути реалізований метод для збереження фінального рахунку гри по її завершенню.'''

    # записує результат в таблицю рекордів.
    # Додаткове завдання: Створити механізм збереження тільки топ 10 рекордів.
    def __init__(self, name, score):
        GameOver.save_score(score, name)

    @staticmethod
    def save_score(score, name):
        with open('scores.txt', 'r') as fl:
            fl_list = []
            for string in fl:
                # вложеный список - с строками и столбцами
                fl_list.append(string.split('|'))
        # сортировка по столбцу по очкам требует вложеный tuple и еще предаварительно int короче ерунда
        # sorted(fl_list, key = itemgetter(2))

        # добавляем текущий результат игры
        fl_list.append([name, str(score), f'{datetime.datetime.now().strftime("%x %X")}\n'])

        # достаем лямбдой вложеное значение списка 2 столбец scores, конвертим в число и по нему сортируем
        fl_list.sort(key=lambda i: int(i[1]))

        # конвертим вложеный список в строку по разделителю, потом в наружном списке делаем срез первых 10 штук и
        # потом склеиваем в одну строку
        string_score = ''.join([" | ".join(i) for i in fl_list][0:9])

        # перезатираем файл
        with open('scores.txt', 'w') as fl:
            fl.write(string_score)

            # fl.write(f"{name} | {score} | {datetime.datetime.now()}" + '\n')


class EnemyDown(Exception):
    ''' Функціонал не потрібен, тільки декларація.'''
    pass


if __name__ == '__main__':
    # test
    GameOver.save_score(109999, 'dsfsdf')
