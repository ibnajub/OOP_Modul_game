# В файлі models.py зберігати класи гравця та противника.
import random
import game_exceptions


# import settings

class Enemy:
    """- Атрибути класу - level, lives.
- Конструктор приймає тільки аргумент level. Кількість життів = рівень противника.

- Містить два методи:
  - статичний select_attack(): повертає випадкове число від 1 до 3.
  - decrease_lives(self): зменшує кількість життів на 1. Коли життів стає 0, викликає виняток EnemyDown."""

    def __init__(self, level, lives):
        self.level = level
        self.lives = lives
        print(f"level: {self.level} | Enemy lives: {self.lives}")

    @staticmethod
    def select_attack():
        return random.randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        # print(f"enemy lives: {self.lives}")
        if self.lives == 0:
            raise game_exceptions.EnemyDown()


class Player:
    """- Атрибути: name, lives, score, allowed_attacks.
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
"""

    def __init__(self, name, lives, mode_multiplayer, allowed_attacks):
        self.name = name
        self.score = 0
        self.lives = lives  # settings.PLAYER_LIVES_CONST
        self.allowed_attacks = allowed_attacks
        self.mode_multiplayer = mode_multiplayer
        print(f'Player lives: {self.lives} , score: {self.score}')

    @staticmethod
    def fight(attack, defense):
        """' чаклуна(1), воїна(2) чи розбійника(3) '
                            'Чаклун перемагає воїна. Воїн перемагає розбійника. Розбійник перемагає чаклуна."""

        if attack == defense:
            return 0
        elif (attack == 1 and defense == 2) \
                or (attack == 2 and defense == 3) \
                or (attack == 3 and defense == 1):
            return 1
        else:
            return -1

    def attack(self, enemy_obj):
        hero_list = self.allowed_attacks
        while True:
            player_hero = input('ATTACK! select wizard(1), warrior(2), bandit(3) '
                                '(wizard win warrior. warrior win bandit. bandit win wizard):')
            if player_hero in hero_list:  # hero_list
                break
            elif player_hero == "exit":  # не работает Control+C
                raise KeyboardInterrupt
            else:
                print('Wrong Hero!')
        enemy_hero = Enemy.select_attack()
        print(f'Enemy is  {enemy_hero}')
        res_fight = Player.fight(int(player_hero), enemy_hero)
        if res_fight == 0:
            print("It's a draw!")
        elif res_fight == 1:
            enemy_obj.decrease_lives()
            # (!!)если будет исключение в decrease_lives то балы тут не насчитает,
            # (они будут в другом месте +5 scores) и счетчик жизней не покажет (print(f"Player lives)
            self.score += 1 * self.mode_multiplayer
            print(f"You attacked successfully! score: {self.score}")
        else:
            print("You missed!!")
        # итог по жизням
        print(f"Player lives: {self.lives} | Enemy lives: {enemy_obj.lives}")

    def defence(self, enemy_obj):
        hero_list = self.allowed_attacks
        while True:
            player_hero = input('DEFENCE! select wizard(1), warrior(2), bandit(3) '
                                '(wizard win warrior. warrior win bandit. bandit win wizard):')
            if player_hero in hero_list:
                break
            elif player_hero == "exit":  # не работает Control+C
                raise KeyboardInterrupt
            else:
                print('Wrong Hero!')

        enemy_hero = Enemy.select_attack()
        print(f'Enemy is  {enemy_hero}')
        res_fight = Player.fight(enemy_hero, int(player_hero))
        if res_fight == 0:
            print("It's a draw!")
        elif res_fight == 1:
            print("You fail defence!!")
            # (!!)если будет исключение в decrease_lives счетчик жизней (print(f"Player liv) не покожет , тк конец игры
            self.decrease_lives()
        else:
            print("You defense successfully!")
        # итог по жизням
        print(f"Player lives: {self.lives} | Enemy lives: {enemy_obj.lives}")

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            hard_norm_s = ('Hard' if self.mode_multiplayer > 1 else 'Normal')
            raise game_exceptions.GameOver(self.name, self.score, hard_norm_s)
