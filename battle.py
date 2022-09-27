"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from pokemon_base import PokemonBase
from random_gen import RandomGen
from poke_team import Action, PokeTeam, Criterion
from print_screen import print_game_screen
from linked_list import LinkedList

class Battle:
    
    def __init__(self, verbosity=0) -> None:
        pass

    def check_action_precedence(self, action1, action2):
        action_list = LinkedList()
        action_list.insert(0, Action.SWAP)
        action_list.insert(0, Action.SPECIAL)
        action_list.insert(0, Action.HEAL)
        action_list.insert(0, Action.ATTACK)

        if action_list.index(action1) == action_list.index(action2):
            return 0
        elif action_list.index(action1) > action_list.index(action2):
            return 1
        elif action_list.index(action1) < action_list.index(action2):
            return 2

    def battle(self, team1: PokeTeam, team2: PokeTeam) -> int:

        team1_used_max_heal = False
        team2_used_max_heal = False

        if (not team1.is_empty()) and (not team2.is_empty()):
            pokemon1 = team1.retrieve_pokemon()
            pokemon2 = team2.retrieve_pokemon()
        
        count = 0
        both_alive = False
        one_alive = False
        while ((not team1.is_empty()) and (not team2.is_empty())) or both_alive or one_alive:
            count += 1
            both_alive = False
            one_alive = False

            if (pokemon1.is_fainted()):
                pokemon1 = team1.retrieve_pokemon()

            if (pokemon2.is_fainted()):
                pokemon2 = team2.retrieve_pokemon()

            first_team_choice = team1.choose_battle_option(pokemon1, pokemon2)
            second_team_choice = team2.choose_battle_option(pokemon2, pokemon1)

            action_precedence_result = self.check_action_precedence(first_team_choice, second_team_choice)

            if action_precedence_result == 0:
                if first_team_choice == Action.SWAP:
                    team1.return_pokemon(pokemon1)
                    pokemon1 = team1.retrieve_pokemon()
                    team2.return_pokemon(pokemon2)
                    pokemon2 = team2.retrieve_pokemon()

                elif first_team_choice == Action.SPECIAL:
                    team1.return_pokemon(pokemon1)
                    team1.special()
                    pokemon1 = team1.retrieve_pokemon()
                    team2.return_pokemon(pokemon2)
                    team2.special()
                    pokemon2 = team2.retrieve_pokemon()

                elif first_team_choice == Action.HEAL:
                    if team1.num_of_heals == 0 and team2.num_of_heals == 0:
                        team1_used_max_heal = True
                        team2_used_max_heal = True 
                        break
                    elif team1.num_of_heals == 0:
                        team1_used_max_heal = True
                        break
                    elif team2.num_of_heals == 0:
                        team2_used_max_heal = True
                        break

                    pokemon1.heal()
                    team1.num_of_heals -= 1
                    pokemon2.heal()
                    team2.num_of_heals -= 1
                    
                elif first_team_choice == Action.ATTACK:
                    pokemon1, pokemon2 = self.both_attack(pokemon1, pokemon2)
               
            elif action_precedence_result == 1:
                if first_team_choice == Action.SWAP:
                    team1.return_pokemon(pokemon1)
                    pokemon1 = team1.retrieve_pokemon()

                elif first_team_choice == Action.SPECIAL:
                    team1.return_pokemon(pokemon1)
                    team1.special()
                    pokemon1 = team1.retrieve_pokemon()

                elif first_team_choice == Action.HEAL:
                    if team1.num_of_heals == 0:
                        team1_used_max_heal = True
                        break

                    pokemon1.heal()
                    team1.num_of_heals -= 1

                elif first_team_choice == Action.ATTACK:
                    a = pokemon2.get_hp()
                    pokemon1.attack(pokemon2)
                    b = pokemon1.get_hp()

                if second_team_choice == Action.SWAP:
                    team2.return_pokemon(pokemon2)
                    pokemon2 = team2.retrieve_pokemon()

                elif second_team_choice == Action.SPECIAL:
                    team2.return_pokemon(pokemon2)
                    team2.special()
                    pokemon2 = team2.retrieve_pokemon()

                elif second_team_choice == Action.HEAL:
                    if team2.num_of_heals == 0:
                        team2_used_max_heal = True
                        break

                    pokemon2.heal()
                    team2.num_of_heals -= 1

                elif second_team_choice == Action.ATTACK:
                    c = pokemon1.get_hp()
                    pokemon2.attack(pokemon1)
                    d = pokemon1.get_hp()

            elif action_precedence_result == 2:
                if second_team_choice == Action.SWAP:
                    team2.return_pokemon(pokemon2)
                    pokemon2 = team2.retrieve_pokemon()

                elif second_team_choice == Action.SPECIAL:
                    team2.return_pokemon(pokemon2)
                    team2.special()
                    pokemon2 = team2.retrieve_pokemon()

                elif second_team_choice == Action.HEAL:
                    if team2.num_of_heals == 0:
                        team2_used_max_heal = True
                        break

                    pokemon2.heal()
                    team2.num_of_heals -= 1

                elif second_team_choice == Action.ATTACK:
                    a = pokemon1.get_hp()
                    pokemon2.attack(pokemon1)
                    b = pokemon1.get_hp()

                if first_team_choice == Action.SWAP:
                    team1.return_pokemon(pokemon1)
                    pokemon1 = team1.retrieve_pokemon()

                elif first_team_choice == Action.SPECIAL:
                    team1.return_pokemon(pokemon1)
                    team1.special()
                    pokemon1 = team1.retrieve_pokemon()

                elif first_team_choice == Action.HEAL:
                    if team1.num_of_heals == 0:
                        team1_used_max_heal = True
                        break

                    pokemon1.heal()
                    team1.num_of_heals -= 1

                elif first_team_choice == Action.ATTACK:
                    c = pokemon2.get_hp()
                    pokemon1.attack(pokemon2)
                    d = pokemon2.get_hp()
            
            #checking level up and evolved versions
            if (not pokemon1.is_fainted()) and (not pokemon2.is_fainted()):
                pokemon1.lose_hp(1)
                pokemon2.lose_hp(1)
                if (not pokemon1.is_fainted()) and (not pokemon2.is_fainted()):
                    both_alive = True

            if pokemon1.is_fainted() and not pokemon2.is_fainted():
                pokemon2.level_up()
                
                team1.return_pokemon(pokemon1)

                if team1.is_empty():
                    team2.return_pokemon(pokemon2) #TODO CHECK IF CORRECT (UNSURE)
                
                if team2.is_empty():
                    one_alive = True

            elif pokemon2.is_fainted() and not pokemon1.is_fainted():
                pokemon1.level_up()

                team2.return_pokemon(pokemon2)

                if team2.is_empty():
                    team1.return_pokemon(pokemon1) #TODO CHECK IF CORRECT (UNSURE)
                
                if team1.is_empty():
                    one_alive = True

            elif pokemon1.is_fainted() and pokemon2.is_fainted():
                team1.return_pokemon(pokemon1)
                team2.return_pokemon(pokemon2)
            
            if not pokemon1.is_fainted():
                if pokemon1.can_evolve() and pokemon1.should_evolve():
                    pokemon1 = pokemon1.get_evolved_version()

            if not pokemon2.is_fainted():
                if pokemon2.can_evolve() and pokemon2.should_evolve():
                    pokemon2 = pokemon2.get_evolved_version()
            
##################################################################################################################
                
        if (team1_used_max_heal and team2_used_max_heal):
            winner_result = 0
        elif (team2_used_max_heal):
            winner_result = 1
        elif (team1_used_max_heal):
            winner_result = 2
        elif (team1.is_empty() and team2.is_empty()):
            winner_result = 0
        elif team2.is_empty() and not team1.is_empty():
            winner_result = 1
        elif team1.is_empty() and not team2.is_empty():
            winner_result = 2

        return winner_result
        
    def both_attack(self, first_pokemon: PokemonBase, second_pokemon: PokemonBase):
        
        pokemon1_speed = first_pokemon.get_speed()
        pokemon2_speed = second_pokemon.get_speed()

        if pokemon1_speed > pokemon2_speed:
            a = second_pokemon.get_hp()
            first_pokemon.attack(second_pokemon) 
            b = second_pokemon.get_hp()
            if not second_pokemon.is_fainted():  
                c = first_pokemon.get_hp()
                second_pokemon.attack(first_pokemon)
                d = first_pokemon.get_hp()
        
        elif pokemon2_speed > pokemon1_speed:
            c = first_pokemon.get_hp()
            second_pokemon.attack(first_pokemon)
            d = first_pokemon.get_hp()
            if not first_pokemon.is_fainted():
                a = second_pokemon.get_hp()
                first_pokemon.attack(second_pokemon)
                b = second_pokemon.get_hp()

        #FIXME: fainted pokemon still attacks (unsure)
        elif pokemon1_speed == pokemon2_speed:
            a = second_pokemon.get_hp()
            first_pokemon.attack(second_pokemon)
            b = second_pokemon.get_hp()
            c = first_pokemon.get_hp()
            second_pokemon.attack(first_pokemon)
            d = first_pokemon.get_hp()

        return first_pokemon, second_pokemon


if __name__ == "__main__":
    # b = Battle(verbosity=3)
    # RandomGen.set_seed(16)
    # t1 = PokeTeam.random_team("Cynthia", 0, criterion=Criterion.SPD)
    # t1.ai_type = PokeTeam.AI.USER_INPUT
    # t2 = PokeTeam.random_team("Barry", 1)
    RandomGen.set_seed(20)
    battle = Battle(verbosity=0)
    t1 = PokeTeam.random_team("Team 1", 0)
    t2 = PokeTeam.random_team("Team 2", 0)
    print (str(t1))
    print (str(t2))
    print(battle.battle(t1, t2))
    print (str(t1))
    print (str(t2))
