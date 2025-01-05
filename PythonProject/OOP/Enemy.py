class Enemy:
    types_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    #default constructor
    # def __init__(self):
    #     pass

    #no argument constructor
    # def __init__(self):
    #     print("Create new enemy!")
    #parameter constructor
    # def __init__(self,type_of_enemy,health_points,attack_damage):
    #     self.types_of_enemy = type_of_enemy
    #     self.health_points = health_points
    #     self.attack_damage = attack_damage

    #encapsulation
    def __init__(self,type_of_enemy,health_points,attack_damage):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f'I am a {self.__type_of_enemy}. Be prepared to fight')

    def walk_forward(self):
        print(f'{self.__type_of_enemy} moves closer to you.')

    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.health_points} damage')

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def special_attack(self):
        print('Enemy has no special attack!')