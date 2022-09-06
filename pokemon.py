"""
"""
from pokemon_base import PokemonBase, StatusEffect, PokeType
__author__ = "Scaffold by Jackson Goerner, Code by ______________"
   
class Charmander(PokemonBase):
    def __init__(self) -> None:
        self.level = 1
        self.max_hp = 8 + (1 * self.level)
        PokemonBase.__init__(self, self.max_hp, PokeType.FIRE)
    
    def level_up(self) -> None:
        self.level += 1
        new_max = 8 + (1 * self.level)
        self.hp = new_max - (self.max_hp - self.hp)
        self.max_hp = new_max
    
    def get_level(self):
        return self.level

    def get_speed(self) -> int:
        speed = 7 + (1 * self.level)
        if self.status.value == "Paralysis":
            speed = speed * 0.5 # speed is halved
        return speed

    def get_attack_damage(self) -> int:
        attack = 6 + (1 * self.level)
        if self.status.value == "Burn":
            attack = attack * 0.5 # attack is halved

        return attack

    def get_defence(self) -> int:
        defence_pts = 4
        return defence_pts

    def defend(self, damage:int) -> int:
        if damage > self.get_defence():
            lost_hp = damage
        else:
            lost_hp = damage // 2
        return lost_hp
    
    def get_poke_name(self) -> str:
        name = "Charmander"
        return name
    
    def should_evolve(self) -> bool:
        should_evolve = False
        if self.level == 3:
            should_evolve = True
        return should_evolve

    def can_evolve(self) -> bool:
        can_evolve = True
        return can_evolve

    def get_evolved_version(self) -> PokemonBase:
        hp_difference = self.max_hp - self.hp
        charizard = Charizard()
        charizard.lose_hp(hp_difference)
        return charizard

class Squirtle(PokemonBase):
    def __init__(self) -> None:
        self.level = 1
        self.max_hp = 12 + (1 * self.level)
        PokemonBase.__init__(self, self.max_hp, PokeType.WATER)
    
    def level_up(self) -> None:
        self.level += 1
        new_max = 12 + (1 * self.level)
        self.hp = new_max - (self.max_hp - self.hp)
        self.max_hp = new_max
    
    def get_level(self):
        return self.level

    def get_speed(self) -> int:
        speed = 7 
        if self.status.value == "Paralysis":
            speed = speed * 0.5 # speed is halved
        return speed

    def get_attack_damage(self) -> int:
        attack = 4 + (self.level // 2)
        if self.status.value == "Burn":
            attack = attack * 0.5 # attack is halved
        return attack

    def get_defence(self) -> int:
        defence_pts = 6 + self.level
        return defence_pts

    def defend(self, damage:int) -> int:
        if damage > (2 * self.get_defence()):
            lost_hp = damage
        else:
            lost_hp = damage // 2
        return lost_hp
    
    def get_poke_name(self) -> str:
        name = "Squirtle"
        return name
    
    def should_evolve(self) -> bool:
        should_evolve = False
        if self.level == 3:
            should_evolve = True
        return should_evolve

    def can_evolve(self) -> bool:
        can_evolve = True
        return can_evolve

    def get_evolved_version(self) -> PokemonBase:
        hp_difference = self.max_hp - self.hp
        blastoise = Blastoise()
        blastoise.lose_hp(hp_difference)
        return blastoise

class Bulbasaur(PokemonBase):
    def __init__(self) -> None:
        self.level = 1
        self.max_hp = 12 + (1 * self.level)
        PokemonBase.__init__(self, self.max_hp, PokeType.GRASS)
    
    def level_up(self) -> None:
        self.level += 1
        new_max = 12 + (1 * self.level)
        self.hp = new_max - (self.max_hp - self.hp)
        self.max_hp = new_max
    
    def get_level(self):
        return self.level

    def get_speed(self) -> int:
        speed = 7 + (self.level // 2) 
        if self.status.value == "Paralysis":
            speed = speed * 0.5 # speed is halved
        return speed

    def get_attack_damage(self) -> int:
        attack = 5
        if self.status.value == "Burn":
            attack = attack * 0.5 # attack is halved
        return attack

    def get_defence(self) -> int:
        defence_pts = 5
        return defence_pts

    def defend(self, damage:int) -> int:
        if damage > (self.get_defence() + 5):
            lost_hp = damage
        else:
            lost_hp = damage // 2
        return lost_hp
    
    def get_poke_name(self) -> str:
        name = "Bulbasaur"
        return name
    
    def should_evolve(self) -> bool:
        should_evolve = False
        if self.level == 2:
            should_evolve = True
        return should_evolve

    def can_evolve(self) -> bool:
        can_evolve = True
        return can_evolve

    def get_evolved_version(self) -> PokemonBase:
        hp_difference = self.max_hp - self.hp
        venusaur = Venusaur()
        venusaur.lose_hp(hp_difference)
        return venusaur

class Gastly(PokemonBase):
    def __init__(self) -> None:
        self.level = 1
        self.max_hp = 6 + (self.level // 2)
        PokemonBase.__init__(self, self.max_hp, PokeType.GHOST)
    
    def level_up(self) -> None:
        self.level += 1
        new_max = 6 + (self.level // 2)
        self.hp = new_max - (self.max_hp - self.hp)
        self.max_hp = new_max
    
    def get_level(self):
        return self.level

    def get_speed(self) -> int:
        speed = 7 + (self.level // 2) 
        if self.status.value == "Paralysis":
            speed = speed * 0.5 # speed is halved
        return speed

    def get_attack_damage(self) -> int:
        attack = 4
        if self.status.value == "Burn":
            attack = attack * 0.5 # attack is halved
        return attack

    def get_defence(self) -> int:
        defence_pts = 8
        return defence_pts

    def defend(self, damage:int) -> int:
        lost_hp = damage
        return lost_hp
    
    def get_poke_name(self) -> str:
        name = "Gastly"
        return name
    
    def should_evolve(self) -> bool:
        should_evolve = False
        if self.level == 1:
            should_evolve = True
        return should_evolve

    def can_evolve(self) -> bool:
        can_evolve = True
        return can_evolve

    def get_evolved_version(self) -> PokemonBase:
        hp_difference = self.max_hp - self.hp
        haunter = Haunter()
        haunter.lose_hp(hp_difference)
        return haunter

class Eevee(PokemonBase):
    def __init__(self) -> None:
        self.level = 1
        self.max_hp = 10
        PokemonBase.__init__(self, self.max_hp, PokeType.NORMAL)
    
    def level_up(self) -> None:
        self.level += 1
        new_max = 10
        self.hp = new_max - (self.max_hp - self.hp)
        self.max_hp = new_max
    
    def get_level(self):
        return self.level

    def get_speed(self) -> int:
        speed = 7 + self.level
        if self.status.value == "Paralysis":
            speed = speed * 0.5 # speed is halved
        return speed

    def get_attack_damage(self) -> int:
        attack = 6 + self.level
        if self.status.value == "Burn":
            attack = attack * 0.5 # attack is halved
        return attack

    def get_defence(self) -> int:
        defence_pts = 4 + self.level
        return defence_pts

    def defend(self, damage:int) -> int:
        if damage >= self.get_defence():
            lost_hp = damage
        else:
            lost_hp = 0
        return lost_hp
    
    def get_poke_name(self) -> str:
        name = "Eevee"
        return name
    
    def should_evolve(self) -> bool:
        should_evolve = False
        return should_evolve

    def can_evolve(self) -> bool:
        can_evolve = False
        return can_evolve

    def get_evolved_version(self) -> PokemonBase:
        return self

class Charizard(PokemonBase):
    def __init__(self) -> None:
        self.level = 3
        self.max_hp = 12 + (1 * self.level)
        PokemonBase.__init__(self, self.max_hp, PokeType.FIRE)
    
    def level_up(self) -> None:
        self.level += 1
        new_max = 12 + (1 * self.level)
        self.hp = new_max - (self.max_hp -self.hp)
        self.max_hp = new_max
    
    def get_level(self):
        return self.level

    def get_speed(self) -> int:
        speed = 9 + (1 * self.level)
        if self.status.value == "Paralysis":
            speed = speed * 0.5 # speed is halved
        return speed

    def get_attack_damage(self) -> int:
        attack = 10 + (2 * self.level)
        if self.status.value == "Burn":
            attack = attack * 0.5 # attack is halved
        return attack

    def get_defence(self) -> int:
        defence_pts = 4
        return defence_pts

    def defend(self, damage:int) -> int:
        if damage > self.get_defence():
            lost_hp = 2 * damage
        else:
            lost_hp = damage
        return lost_hp
    
    def get_poke_name(self) -> str:
        name = "Charizard"
        return name
    
    def should_evolve(self) -> bool:
        should_evolve = False
        return should_evolve

    def can_evolve(self) -> bool:
        can_evolve = False
        return can_evolve

    def get_evolved_version(self) -> PokemonBase:
        return self

class Blastoise(PokemonBase):
    def __init__(self) -> None:
        self.level = 3
        self.max_hp = 15 + (2 * self.level)
        PokemonBase.__init__(self, self.max_hp, PokeType.WATER)
    
    def level_up(self) -> None:
        self.level += 1
        new_max = 15 + (2 * self.level)
        self.hp = new_max - (self.max_hp -self.hp)
        self.max_hp = new_max
    
    def get_level(self):
        return self.level

    def get_speed(self) -> int:
        speed = 10
        if self.status.value == "Paralysis":
            speed = speed * 0.5 # speed is halved
        return speed

    def get_attack_damage(self) -> int:
        attack = 8 + (self.level // 2)
        if self.status.value == "Burn":
            attack = attack * 0.5 # attack is halved
        return attack

    def get_defence(self) -> int:
        defence_pts = 8 + (1 * self.level)
        return defence_pts

    def defend(self, damage:int) -> int:
        if damage > (2 * self.get_defence()):
            lost_hp = damage
        else:
            lost_hp = damage // 2
        return lost_hp
    
    def get_poke_name(self) -> str:
        name = "Blastoise"
        return name
    
    def should_evolve(self) -> bool:
        should_evolve = False
        return should_evolve

    def can_evolve(self) -> bool:
        can_evolve = False
        return can_evolve

    def get_evolved_version(self) -> PokemonBase:
        return self

class Venusaur(PokemonBase):
    def __init__(self) -> None:
        self.level = 2
        self.max_hp = 20 + (self.level // 2)
        PokemonBase.__init__(self, self.max_hp, PokeType.GRASS)
    
    def level_up(self) -> None:
        self.level += 1
        new_max = 20 + (self.level // 2)
        self.hp = new_max - (self.max_hp -self.hp)
        self.max_hp = new_max
    
    def get_level(self):
        return self.level

    def get_speed(self) -> int:
        speed = 3 + (self.level // 2)
        if self.status.value == "Paralysis":
            speed = speed * 0.5 # speed is halved
        return speed

    def get_attack_damage(self) -> int:
        attack = 5
        if self.status.value == "Burn":
            attack = attack * 0.5 # attack is halved
        return attack

    def get_defence(self) -> int:
        defence_pts = 10
        return defence_pts

    def defend(self, damage:int) -> int:
        if damage > (self.get_defence() + 5):
            lost_hp = damage
        else:
            lost_hp = damage // 2
        return lost_hp
    
    def get_poke_name(self) -> str:
        name = "Venusaur"
        return name
    
    def should_evolve(self) -> bool:
        should_evolve = False
        return should_evolve

    def can_evolve(self) -> bool:
        can_evolve = False
        return can_evolve

    def get_evolved_version(self) -> PokemonBase:
        return self

class Haunter(PokemonBase):
    def __init__(self) -> None:
        self.level = 1
        self.max_hp = 9 + (self.level // 2)
        PokemonBase.__init__(self, self.max_hp, PokeType.GHOST)
    
    def level_up(self) -> None:
        self.level += 1
        new_max = 9 + (self.level // 2)
        self.hp = new_max - (self.max_hp -self.hp)
        self.max_hp = new_max
    
    def get_level(self):
        return self.level

    def get_speed(self) -> int:
        speed = 6
        if self.status.value == "Paralysis":
            speed = speed * 0.5 # speed is halved
        return speed

    def get_attack_damage(self) -> int:
        attack = 8
        if self.status.value == "Burn":
            attack = attack * 0.5 # attack is halved
        return attack

    def get_defence(self) -> int:
        defence_pts = 6
        return defence_pts

    def defend(self, damage:int) -> int:
        lost_hp = damage 
        return lost_hp
    
    def get_poke_name(self) -> str:
        name = "Haunter"
        return name
    
    def should_evolve(self) -> bool:
        should_evolve = False
        if self.level == 3:
            should_evolve = True
        return should_evolve

    def can_evolve(self) -> bool:
        can_evolve = True
        return can_evolve

    def get_evolved_version(self) -> PokemonBase:
        hp_difference = self.max_hp - self.hp
        gengar = Gengar()
        gengar.lose_hp(hp_difference)
        return gengar

class Gengar(PokemonBase):
    def __init__(self) -> None:
        self.level = 3
        self.max_hp = 12 + (self.level // 2)
        PokemonBase.__init__(self, self.max_hp, PokeType.GHOST)
    
    def level_up(self) -> None:
        self.level += 1
        new_max = 12 + (self.level // 2)
        self.hp = new_max - (self.max_hp -self.hp)
        self.max_hp = new_max
    
    def get_level(self):
        return self.level

    def get_speed(self) -> int:
        speed = 12
        if self.status.value == "Paralysis":
            speed = speed * 0.5 # speed is halved
        return speed

    def get_attack_damage(self) -> int:
        attack = 18
        if self.status.value == "Burn":
            attack = attack * 0.5 # attack is halved
        return attack

    def get_defence(self) -> int:
        defence_pts = 3
        return defence_pts

    def defend(self, damage:int) -> int:
        lost_hp = damage 
        return lost_hp
    
    def get_poke_name(self) -> str:
        name = "Gengar"
        return name
    
    def should_evolve(self) -> bool:
        should_evolve = False
        return should_evolve

    def can_evolve(self) -> bool:
        can_evolve = False
        return can_evolve

    def get_evolved_version(self) -> PokemonBase:
        return self


