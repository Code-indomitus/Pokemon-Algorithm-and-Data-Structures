from __future__ import annotations
from inspect import stack
# from sys import last_value


"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from enum import Enum, auto
from pokemon_base import PokemonBase
from pokemon import *
from random_gen import RandomGen
from array_sorted_list import ArraySortedList
from queue_adt import CircularQueue
from stack_adt import  ArrayStack
from sorted_list import ListItem
from pokemon_base import StatusEffect



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


        self.num_of_heals = 3

    @classmethod
    def random_team(cls, team_name: str, battle_mode: int, team_size=None, ai_mode=None, criterion = None)-> PokeTeam:

        NUM_OF_RANDOMS = 4

        if team_size is None:
            lo = 6//2
            hi = 6
            team_size = RandomGen.randint(lo, hi)

        random_team_numbers = ArraySortedList(6)

        random_team_numbers.add(ListItem(None,0))
        random_team_numbers.add(ListItem(None, team_size))


        for i in range(NUM_OF_RANDOMS):
            random_number = RandomGen.randint(0, team_size)
            random_team_numbers.add(ListItem(None,random_number))

        # array that stores the number of each pokemon
        team_numbers = []
        for i in range(0, len(random_team_numbers) - 1):
            team_numbers.append(random_team_numbers[i+1].key - random_team_numbers[i].key)

        if ai_mode is None:
            ai_mode = PokeTeam.AI.RANDOM


            # rand_num = RandomGen.randint(1, 4)
            # if rand_num == 1:
            #     ai_mode = AI.ALWAYS_ATTACK
            # elif rand_num == 2:
            #     ai_mode = AI.SWAP_ON_SUPER_EFFECTIVE
            # elif rand_num == 3:
            #     ai_mode = AI.RANDOM
            # elif rand_num == 4:
            #     ai_mode = AI.USER_INPUT

        random_team = PokeTeam(team_name,team_numbers,battle_mode,ai_mode, criterion = criterion)

        return random_team

    # FIXME If required
    def return_pokemon(self, pokemon: PokemonBase) -> None:

        if not pokemon.is_fainted():
            pokemon.set_status_effect(StatusEffect.NONE)

            if self.battle_mode == 0: # ArrayStack
                self.team.push(pokemon)
            elif self.battle_mode == 1: # CircularQueue
                self.team.append(pokemon)
            elif self.battle_mode == 2: # ArraySortedList
                if self.criterion == Criterion.SPD:
                    self.team.add(ListItem(pokemon, pokemon.get_speed()))
                elif self.criterion == Criterion.HP:
                    self.team.add(ListItem(pokemon, pokemon.get_hp()))
                elif self.criterion == Criterion.LV:
                    self.team.add(ListItem(pokemon, pokemon.get_level()))
                elif self.criterion == Criterion.DEF:
                    self.team.add(ListItem(pokemon, pokemon.get_defence()))
            
    # FIXME If required
    def retrieve_pokemon(self) -> PokemonBase | None:
        if self.is_empty():
            pokemon = None
        elif self.battle_mode == 0:  # ArrayStack
            pokemon = self.team.pop()
        elif self.battle_mode == 1:  # CircularQueue
            pokemon = self.team.serve()
        elif self.battle_mode == 2:  # ArraySortedList
            pokemon = self.team.delete_at_index(0).value
        
        return pokemon

    # TODO implement special method for battle mode 2
    def special(self):
        if self.battle_mode == 0:  # ArrayStack
            temp_stack = ArrayStack(len(self.team) - 2)

            first_pokemon = self.team.pop()

            while len(self.team) > 1:
                temp_stack.push(self.team.pop())
            
            last_pokemon =self.team.pop()

            self.team.push(first_pokemon)

            while len(temp_stack) > 0:
                self.team.push(temp_stack.pop())
            
            self.team.push(last_pokemon)


        if self.battle_mode == 1:  # CircularQueue
            half_number = len(self.team) // 2
            temp_stack = ArrayStack(half_number)

            for _ in range(half_number):
                temp_stack.push(self.team.serve())
            
            for _ in range(half_number):
                self.team.append(temp_stack.pop())


        # TODO implement special method for battle mode 2
        if self.battle_mode == 2:  # ArraySortedList
            self.team.reverse_order()


    def regenerate_team(self):
        self.set_team()
        self.num_of_heals = 3

    # FIXME string implementation for battle mode 2
    def __str__(self) -> str:
        result = self.team_name + " " + "(" + str(self.battle_mode) + ")" + ": "

        pokemon_str_list = ""

        if self.battle_mode == 0:  # ArrayStack
            stack_length = len(self.team)
            for _ in range(stack_length):
                pokemon_str_list += str(self.team.peek()) + ", "
                self.team.length -= 1
            self.team.length = stack_length
                
        elif self.battle_mode == 1:  # CircularQueue
            for _ in range(len(self.team)):
                pokemon = self.team.serve()
                pokemon_str_list += str(pokemon) + ", "
                self.team.append(pokemon)

        # FIXME string implementation for battle mode 2
        elif self.battle_mode == 2:  # ArraySortedList
            for i in range(len(self.team)):
                pokemon = self.team[i].value
                pokemon_str_list += str(pokemon) + ", "

        result += "[" + pokemon_str_list[0:-2] + "]"
        return result

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

    # FIXME if required
    def set_team(self):
        if self.battle_mode == 0: # ArrayStack
            self.team = ArrayStack(self.num_of_pokemons)
            self.fill_team_mode_zero()
        elif self.battle_mode == 1: # CircularQueue
            self.team = CircularQueue(self.num_of_pokemons)
            self.fill_team_mode_one()
        elif self.battle_mode == 2: # ArraySortedList
            self.team = ArraySortedList(self.num_of_pokemons)
            self.fill_team_mode_two()
            self.team.reverse_order()

    # FIXME if required
    def fill_team_mode_zero(self):
        for i in range(len(self.team_numbers)-1,-1,-1):

            for j in range(self.team_numbers[i]):
                
                if i == 0:
                    pokemon = Charmander()
                elif i == 1:
                    pokemon = Bulbasaur()
                elif i == 2:
                    pokemon = Squirtle()
                elif i == 3:
                    pokemon = Gastly()
                elif i == 4:
                    pokemon = Eevee()
                self.team.push(pokemon)

    # FIXME if required
    def fill_team_mode_one(self):
        for i in range(len(self.team_numbers)):

            for j in range(self.team_numbers[i]):
                if i == 0:
                    pokemon = Charmander()
                elif i == 1:
                    pokemon = Bulbasaur()
                elif i == 2:
                    pokemon = Squirtle()
                elif i == 3:
                    pokemon = Gastly()
                elif i == 4:
                    pokemon = Eevee()
                self.team.append(pokemon)

    # FIXME if required
    def fill_team_mode_two(self):
        for i in range(len(self.team_numbers)):

            for j in range(self.team_numbers[i]):
                if i == 0:
                    pokemon = Charmander()
                elif i == 1:
                    pokemon = Bulbasaur()
                elif i == 2:
                    pokemon = Squirtle()
                elif i == 3:
                    pokemon = Gastly()
                elif i == 4:
                    pokemon = Eevee()
                    
                if self.criterion == Criterion.SPD:
                    self.team.add(ListItem(pokemon, pokemon.get_speed()))
                elif self.criterion == Criterion.HP:
                    self.team.add(ListItem(pokemon, pokemon.get_hp()))
                elif self.criterion == Criterion.LV:
                    self.team.add(ListItem(pokemon, pokemon.get_level()))
                elif self.criterion == Criterion.DEF:
                    self.team.add(ListItem(pokemon, pokemon.get_defence()))
    
    def get_team_numbers(self):
        return self.team_numbers

    @classmethod
    def leaderboard_team(cls):
        raise NotImplementedError()
