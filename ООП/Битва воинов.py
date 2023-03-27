from random import randint, choice, choices


class Soldier:
    health = 100

    def __init__(self, name):
        self.name = name

    def make_kick(self, enemy):
        level_damage = 10
        enemy.health -= level_damage
        print(f'{self.name} атакует {enemy.name}')
        print(f'{enemy.name} = {enemy.health}% здоровья')
        print(f'{self.name} = {self.health}% здоровья')
        print()


class Battle:
    result = 'Сражения не было'

    def battle(self, u1, u2):
        while u1.health > 0 and u2.health > 0:
            if u1.health <= 0 or u2.health <= 0:
                return
            if randint(1, 2) == 1:
                u1.make_kick(u2)
            else:
                u2.make_kick(u1)
            self.result = (f'{u2.name}', f'{u1.name}')[u1.health > u2.health] + ' победил!'

    def who_win(self):
        print(self.result)


# Создаем объекты класса Soldier и присваиваем им имена
# unit_1 = Soldier('Воин-1')
# unit_2 = Soldier('Воин-2')
unit_1 = Soldier('Супермент')
unit_2 = Soldier('Халк')

# Создаем объекты класса Battle
get_battle = Battle()

# Вызываем метод battle объекта get_battle
# начинаем битву
get_battle.battle(unit_1, unit_2)

# Вызываем метод who_win объекта get_battle
# определяем победителя
get_battle.who_win()
