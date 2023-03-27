from random import randint


class Warrior:

    def make_health(self, value):
        self.health = value

    def make_kick(self, enemy):
        enemy.health -= 20


unit_1 = Warrior()
unit_2 = Warrior()

unit_1.make_health(100)
unit_2.make_health(100)

while unit_1.health > 0 and unit_2.health > 0:
    n = randint(1, 2)
    if n == 1:
        unit_1.make_kick(unit_2)
        print('Воин unit_1 атакует!')
        print('У воина unit_2 осталось', unit_2.health)
    else:
        unit_2.make_kick(unit_1)
        print('Воин unit_2 атакует!')
        print('У воина unit_1 осталось', unit_1.health)

print(('Воин Unit_2 победил!', 'Воин Unit_1 победил!')[unit_1.health > unit_2.health])


