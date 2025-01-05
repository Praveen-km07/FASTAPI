from Enemy import *
from Zombie import *
from Ogre import *
from Hero import *
from Weapon import *

# polymorphism
def battle(e1:Enemy,e2:Enemy):
    e1.talk()
    e2.talk()
    # e1.attack()
    # e2.attack()

    while e1.health_points > 0 and e2.health_points > 0:
        print('-----------------')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()}:{e1.health_points} HP left')
        print(f'{e2.get_type_of_enemy()}:{e2.health_points} HP left')
        e2.attack()
        e1.health_points -= e2.health_points
        e1.attack()
        e2.health_points -= e1.health_points

    print('-----------------')
    if e1.health_points > 0 :
        print(f'{e1.get_type_of_enemy()} wins!')
    else:
        print(f'{e2.get_type_of_enemy()} wins!')

# composition
def hero_battle(hero:Hero,enemy:Enemy):

    while hero.health_points > 0 and enemy.health_points > 0:
        print('-----------------')
        enemy.special_attack()
        print(f'Hero:{hero.health_points} HP left')
        print(f'{enemy.get_type_of_enemy()}:{enemy.health_points} HP left')
        enemy.attack()
        hero.health_points -= enemy.health_points
        hero.attack()
        enemy.health_points -= hero.health_points

    print('-----------------')
    if hero.health_points > 0 :
        print(f'Hero wins!')
    else:
        print(f'{enemy.get_type_of_enemy()} wins!')

# zombie = Enemy()
zombie = Enemy('New Zombie',2,20)
# big_zombie = Enemy('Big Zombie',3,30)
zombie.__type_of_enemy = 'ogre'
print(zombie.health_points)
print(f'{zombie.__type_of_enemy} has {zombie.health_points} health points and can do an attack of {zombie.attack_damage}')
# print(f'{big_zombie.types_of_enemy} has {big_zombie.health_points} health points and can do an attack of {big_zombie.attack_damage}')
print(zombie.get_type_of_enemy())

print(zombie.talk())
print(zombie.walk_forward())
print(zombie.attack())

inherit_zombie = Zombie(10,1)
print(inherit_zombie.get_type_of_enemy())
print(inherit_zombie.talk())
print(inherit_zombie.spread_disease())

ogre = Ogre(20,3)
print(ogre.talk())
print("********************")
battle(ogre,zombie)
battle(zombie,ogre)

print("****************")
hero = Hero(10,1)
weapon = Weapon('Sword',100)
hero.weapon = weapon
hero.equip_weapon()
hero_battle(hero,ogre)

