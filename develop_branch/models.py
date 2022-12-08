# В файлі models.py зберігати класи гравця та противника.


class Enemy():
    '''
- Атрибути класу - level, lives.
- Конструктор приймає тільки аргумент level. Кількість життів = рівень противника.

- Містить два методи:
  - статичний select_attack(): повертає випадкове число від 1 до 3.
  - decrease_lives(self): зменшує кількість життів на 1. Коли життів стає 0, викликає виняток EnemyDown.'''

    pass


class Player()
    '''  
- Атрибути: name, lives, score, allowed_attacks.
- Конструктор приймає ім'я гравця. 
  - Кількість життів отримується з settings. 
  - Рахунок дорівнює нулю.

- Методи: 
  - статичний fight(attack, defense) - повертає результат атаки/захисту:
    - 0 нічия
    - -1 aтака/захист невдалі.
    - 1 атака/захист вдалі.

  - decrease_lives(self) - те саме, що і Enemy.decrease_lives(), викликає виняток GameOver.

  - attack(self, enemy_obj) 
    - отримує input (1, 2, 3) від користувача;
    - обирає атаку противника з об'екту enemy_obj; 
    - викликає метод fight(); 
    - Якщо результат 0 - вивести "It's a draw!"
    - Якщо 1 = "You attacked successfully!" та зменшує кількість життів противника на 1;
    - Якщо -1 = "You missed!"

  - defence(self, enemy_obj) - такий самий, як метод attack(), тільки в метод fight першим передається атака противника
  , та при вдалій атаці противника викликається метод decrease_lives гравця.
'''
    pass
