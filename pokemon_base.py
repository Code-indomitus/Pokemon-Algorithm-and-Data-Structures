from __future__ import annotations
from abc import ABC, abstractmethod 
from typing import TypeVar, Generic 
from enum import Enum
from random_gen import RandomGen

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

class PokeType(Enum):
    FIRE = "Fire"
    GRASS = "Grass"
    WATER = "Water"
    GHOST = "Ghost"
    NORMAL = "Normal"

class StatusEffect(Enum):
    NONE = "None"
    BURN = "Burn"
    POISON = "Poison"
    PARALYSIS = "Paralysis"
    SLEEP = "Sleep"
    CONFUSTION = "Confusion"


T = TypeVar('T')

class PokemonBase(ABC, Generic[T]):

    def __init__(self, hp: int, poke_type: PokeType) -> None:
        # pre condition
        if hp <= 0:
            raise ValueError("Max hp must be greater than zero!")
        self.hp = hp
        self.poke_type = poke_type
        self.status = StatusEffect.NONE
        self.max = self.hp

    def is_fainted(self) -> bool:
        if self.hp <= 0:
            return True
        else:
            return False
    
    def get_hp(self):
        return self.hp
    
    def heal(self):
        self.hp = self.max
        self.status = StatusEffect.NONE
    
    @abstractmethod
    def get_level(self):
        pass
    
    @abstractmethod
    def level_up(self) -> None:
        pass

    @abstractmethod
    def get_speed(self) -> int:
        pass

    @abstractmethod
    def get_attack_damage(self) -> int:
        pass

    @abstractmethod
    def get_defence(self) -> int:
        pass

    def lose_hp(self, lost_hp: int) -> None:
        self.hp -= lost_hp

    @abstractmethod
    def defend(self, damage: int) -> None:
        pass      

    # @abstractmethod
    def attack(self, other: PokemonBase):
        # Step 1: Status effects on attack damage / redirecting attacks
        # Step 2: Do the attack
        # Step 3: Losing hp to status effects
        # Step 4: Possibly applying status effects

        if self.status.value == "Sleep":
            return 
    
        if self.status.value == "Confusion" and RandomGen.random_chance(0.5):
            other = self
        
        effective_attack = self.get_attack_damage() * self.get_effective_multiplier(other)
        defence_calculation = other.defend(effective_attack)
        other.lose_hp(defence_calculation)

        if RandomGen.random_chance(0.2):
            other.status = self.get_inflict_status()
            if other.status.value == "Burn":
                other.lose_hp(1)
            elif other.status.value == "Poison":
                other.lose_hp(3)

    @abstractmethod
    def get_poke_name(self) -> str:
        pass

    def __str__(self) -> str:
        pokemon_string = "LV. " + str(self.get_level()) + " " + self.get_poke_name() + ": " + str(self.hp) + " HP"
        return pokemon_string

    @abstractmethod
    def should_evolve(self) -> bool:
        pass

    @abstractmethod
    def can_evolve(self) -> bool:
        pass

    @abstractmethod
    def get_evolved_version(self) -> PokemonBase:
        pass

    def get_effective_multiplier(self, other: PokemonBase) -> float:
        if self.poke_type.value == "Fire":
            if other.poke_type.value == "Fire":
                multiplier = 1
            elif other.poke_type.value == "Grass":
                multiplier = 2
            elif other.poke_type.value == "Water":
                multiplier = 0.5
            elif other.poke_type.value == "Ghost":
                multiplier = 1
            elif other.poke_type.value == "Normal":
                multiplier = 1
    
        elif self.poke_type.value == "Grass":
            if other.poke_type.value == "Fire":
                multiplier = 0.5
            elif other.poke_type.value == "Grass":
                multiplier = 1
            elif other.poke_type.value == "Water":
                multiplier = 2
            elif other.poke_type.value == "Ghost":
                multiplier = 1
            elif other.poke_type.value == "Normal":
                multiplier = 1

        elif self.poke_type.value == "Water":
            if other.poke_type.value == "Fire":
                multiplier = 2
            elif other.poke_type.value == "Grass":
                multiplier = 0.5
            elif other.poke_type.value == "Water":
                multiplier = 1
            elif other.poke_type.value == "Ghost":
                multiplier = 1
            elif other.poke_type.value == "Normal":
                multiplier = 1

        elif self.poke_type.value == "Ghost":
            if other.poke_type.value == "Fire":
                multiplier = 1.25
            elif other.poke_type.value == "Grass":
                multiplier = 1.25
            elif other.poke_type.value == "Water":
                multiplier = 1.25
            elif other.poke_type.value == "Ghost":
                multiplier = 2
            elif other.poke_type.value == "Normal":
                multiplier = 0

        elif self.poke_type.value == "Normal":
            if other.poke_type.value == "Fire":
                multiplier = 1.25
            elif other.poke_type.value == "Grass":
                multiplier = 1.25
            elif other.poke_type.value == "Water":
                multiplier = 1.25
            elif other.poke_type.value == "Ghost":
                multiplier = 0
            elif other.poke_type.value == "Normal":
                multiplier = 1

        return multiplier

    def get_inflict_status(self) -> StatusEffect:

        if self.poke_type.value == "Fire":
            new_status = StatusEffect.BURN
        elif self.poke_type.value == "Grass":
            new_status = StatusEffect.POISON
        elif self.poke_type.value == "Water":
            new_status = StatusEffect.PARALYSIS
        elif self.poke_type.value == "Ghost":
            new_status = StatusEffect.SLEEP
        elif self.poke_type.value == "Normal":
            new_status = StatusEffect.CONFUSTION
        
        return new_status

    def get_status_effect(self) -> StatusEffect:
        return self.status

    def set_status_effect(self, new_status_effect: StatusEffect):
        self.status = new_status_effect
