# В файлі models.py зберігати класи гравця та противника.
import random
import game_exceptions


# import settings

class Enemy():
    '''
- Атрибути класу - level, lives.
- Конструктор приймає тільки аргумент level. Кількість життів = рівень противника.

- Містить два методи:
  - статичний select_attack(): повертає випадкове число від 1 до 3.
  - decrease_lives(self): зменшує кількість життів на 1. Коли життів стає 0, викликає виняток EnemyDown.'''

    def __init__(self, level):
        self.level = level
        self.lives =  level

    @staticmethod
    def select_attack():
        return random.randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise game_exceptions.EnemyDown()


class Player():
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

    def __init__(self, name, lives, allowed_attacks):
        self.name = name
        self.score = 0
        self.lives = lives  # settings.PLAYER_LIVES_CONST
        self.allowed_attacks = allowed_attacks

    @staticmethod
    def fight(attack, defense):
        '''' чаклуна(1), воїна(2) чи розбійника(3) '
                            'Чаклун перемагає воїна. Воїн перемагає розбійника. Розбійник перемагає чаклуна.'''

        if attack == defense:
            return 0
        elif (attack == 1 and defense == 2) \
                or (attack == 2 and defense == 3) \
                or (attack == 3 and defense == 1):
            return 1
        else:
            return -1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise game_exceptions.GameOver()

    def attack(self, enemy_obj):
        player_hero = input('attack , select чаклуна(1), воїна(2) чи розбійника(3) '
                            'Чаклун перемагає воїна. Воїн перемагає розбійника. Розбійник перемагає чаклуна.')
        enemy_hero = Enemy.select_attack()
        print(f'Enemy is  {enemy_hero}')
        res_fight = Player.fight(player_hero, enemy_hero)
        if res_fight == 0:
            print("It's a draw!")
        elif res_fight == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
        else:
            print("You missed!!")

    def defence(self, enemy_obj):
        player_hero = input('defence, select чаклуна(1), воїна(2) чи розбійника(3) '
                            'Чаклун перемагає воїна. Воїн перемагає розбійника. Розбійник перемагає чаклуна.')
        #Додати валідацію вводу корситувача.

        enemy_hero = Enemy.select_attack()
        print(f'Enemy is  {enemy_hero}' )
        res_fight = Player.fight(enemy_hero, player_hero)
        if res_fight == 0:
            print("It's a draw!")
        elif res_fight == 1:
            print("You defense successfully!")
        else:
            print("You fail defence!!")
            self.decrease_lives()
