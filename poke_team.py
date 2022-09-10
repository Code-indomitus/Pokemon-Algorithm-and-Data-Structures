from __future__ import annotations

import aiohttp.hdrs

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from enum import Enum, auto
from pokemon_base import PokemonBase
from random_gen import RandomGen
from array_sorted_list import ArraySortedList
from queue_adt import CircularQueue
from stack_adt import  ArrayStack



class Action(Enum):
    ATTACK = auto()
    SWAP = auto()
    HEAL = auto()
    SPECIAL = auto()
    
class Criterion(Enum):
    SPD = auto()
    HP = auto()
    LV = auto()
    DEF = auto()

class PokeTeam:

    class AI(Enum):
        ALWAYS_ATTACK = auto()
        SWAP_ON_SUPER_EFFECTIVE = auto()
        RANDOM = auto()
        USER_INPUT = auto()

    def __init__(self, team_name: str, team_numbers: list[int], battle_mode: int, ai_type: PokeTeam.AI, criterion=None, criterion_value=None) -> None:

        if not type(team_name) == str:
            raise TypeError("A string is expected for Team Name.")
        if not type(battle_mode) == int:
            raise TypeError("An integer is expected for Battle Mode.")
        if not (battle_mode == 0 or battle_mode == 1 or battle_mode == 2):
            raise ValueError("Invalid Battle Mode.")
        if battle_mode == 2 and criterion == None :
            raise Exception("Criterion is not specified for Battle Mode 2")
        # Check if the number of pokemons exceeds 6
        sum = 0
        for num in team_numbers:
            sum += num
        if sum > 6:
            raise ValueError("Number of pokemons exceeds team limit")

        self.num_of_pokemons = sum

        self.team_name = team_name
        self.team_numbers = team_numbers
        self.battle_mode = battle_mode
        self.ai_type = ai_type

        self.criterion = criterion
        # team will be the data type according to battle mode
        self.team = None

        self.set_team()
        self.fill_team()

        self.num_of_heals = 3

    @classmethod
    def random_team(cls, team_name: str, battle_mode: int, team_size=None, ai_mode=None, **kwargs)-> PokeTeam:

        NUM_OF_RANDOMS = 4

        if team_size is None:
            lo = 6//2
            hi = 6
            team_size = RandomGen.randint(lo, hi)

        random_team_numbers = ArraySortedList(6)

        random_team_numbers.add(List(None,0))
        random_team_numbers.add(List(None, team_size))


        for i in range(NUM_OF_RANDOMS):
            random_number = RandomGen.random(0, team_size)
            random_team_numbers.add(List(None,random_number))

        # array that stores the number of each pokemon
        team_numbers = []
        for i in range(0, len(team_numbers) - 1):
            team_numbers.append(team_numbers[i + 1] - team_numbers[i])

        if ai_mode is None:
            ai_mode = AI.RANDOM


            # rand_num = RandomGen.randint(1, 4)
            # if rand_num == 1:
            #     ai_mode = AI.ALWAYS_ATTACK
            # elif rand_num == 2:
            #     ai_mode = AI.SWAP_ON_SUPER_EFFECTIVE
            # elif rand_num == 3:
            #     ai_mode = AI.RANDOM
            # elif rand_num == 4:
            #     ai_mode = AI.USER_INPUT

        random_team = PokeTeam(team_name,team_numbers,battle_mode,ai_mode)

        return random_team


    def return_pokemon(self, pokemon: PokemonBase) -> None:
        if self.battle_mode == 0: # ArrayStack
            self.team.push(pokemon)
        if self.battle_mode == 1: # CircularQueue
            self.team.append(pokemon)
        if self.battle_mode == 2: # ArraySortedList
            self.team.add(pokemon)

    def retrieve_pokemon(self) -> PokemonBase | None:
        if self.is_empty():
            pokemon = None
        elif self.battle_mode == 0:  # ArrayStack
            pokemon = self.team.pop()
        elif self.battle_mode == 1:  # CircularQueue
            pokemon = self.team.serve()
        elif self.battle_mode == 2:  # ArraySortedList
            pokemon = self.team.delete_at_index(0)

    # TODO
    def special(self):
        if self.battle_mode == 0:  # ArrayStack
            pass

        if self.battle_mode == 1:  # CircularQueue
            pass

        if self.battle_mode == 2:  # ArraySortedList
            pass


    def regenerate_team(self):
        for pokemons in self.team:
            pokemons.heal()

        self.num_of_heals = 3

    # TODO
    def __str__(self):
        raise NotImplementedError()

    def is_empty(self):
        is_empty = len(self.team) == 0
        return is_empty


    # FIXME if required
    def choose_battle_option(self, my_pokemon: PokemonBase, their_pokemon: PokemonBase) -> Action:
        if self.ai_type == PokeTeam.AI.ALWAYS_ATTACK:
            action = Action.ATTACK
        elif self.ai_type == PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE:  # UNCLEAR
            if their_pokemon.get_attack_damage() * their_pokemon.get_effective_multiplier(my_pokemon) >= 1.5 * my_pokemon.get_attack_damage():
                action = Action.SWAP
            else:
                action = Action.ATTACK
        elif self.ai_type == PokeTeam.AI.RANDOM:
            if self.num_of_heals <= 0:
                rand_num = RandomGen.randint(1, 3)
                if rand_num == 3:
                    rand_num += 1
            else:
                rand_num = RandomGen.randint(1, 4)
            action = Action(rand_num)
        elif self.ai_type == PokeTeam.AI.USER_INPUT:
            print("Available Actions:")
            print("(1) Attack")
            print("(2) Swap")
            print("(3) Heal")
            print("(4) Special")
            choice = int(input("Enter Option: "))
            action = Action(choice)

        return action


    # TODO
    def set_team(self):
        if self.battle_mode == 0: # ArrayStack
            self.team = ArrayStack(self.num_of_pokemons)
        elif self.battle_mode == 1: # CircularQueue
            self.team = CircularQueue(self.num_of_pokemons)
        elif self.battle_mode == 2: # ArraySortedList
            self.team = ArraySortedList(self.num_of_pokemons)

    def fill_team(self):
        pass




    @classmethod
    def leaderboard_team(cls):
        raise NotImplementedError()
