"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by Jobin Mathew Dan"


from random_gen import RandomGen
from poke_team import Action, PokeTeam, Criterion
from pokemon_base import T, PokemonBase
from print_screen import print_game_screen

# from pokemon_base import 


class Battle:

    # team1 = None        # Player's pokemon team
    # team2 = None        # Enemey's pokemon team

    # trainer1 = ""
    # trainer2 = ""

    def __init__(self, verbosity = 0) -> None:
        pass

    def battle(self, team1: PokeTeam, team2: PokeTeam) -> int:
        
        # [Insert comments here]
        winner_result = None
        win_status = ""

        if not (team1.is_empty() and team2.is_empty()):
            pokemon1 = team1.retrieve_pokemon()
            pokemon2 = team2.retrieve_pokemon()


        while ((winner_result == None) and (not((team1.is_empty()) and (team2.is_empty)))):

            if (pokemon1.is_fainted()) and (pokemon2.is_fainted()):
                team1.return_pokemon(pokemon1)
                pokemon1 = team1.retrieve_pokemon()
                team2.return_pokemon(pokemon2)
                pokemon2 = team2.retrieve_pokemon()


            first_team_choice = team1.choose_battle_option(pokemon1, pokemon2)
            second_team_choice = team2.choose_battle_option(pokemon2, pokemon1) 

            if first_team_choice == Action.SWAP:
                team1.return_pokemon(pokemon1)
                pokemon1 = team1.retrieve_pokemon()
                winner_result, team1, team2, pokemon1, pokemon2 = self.check_other_team_actions(second_team_choice, team1, team2, pokemon1, pokemon2)

            elif first_team_choice == Action.SPECIAL:
                team1.return_pokemon(pokemon2)
                team1.special()
                pokemon1 = team1.retrieve_pokemon()
                winner_result, team1, team2, pokemon1, pokemon2  = self.check_other_team_actions(second_team_choice, team1, team2, pokemon1, pokemon2)

            elif first_team_choice == Action.HEAL:
                if team1.num_of_heals > 0:
                    pokemon1.heal()
                    team1.num_of_heals += 1
                    winner_result, team1, team2, pokemon1, pokemon2  = self.check_other_team_actions(second_team_choice, team1, team2, pokemon1, pokemon2)

                else:
                    winner_result = 2

            elif first_team_choice == Action.ATTACK and second_team_choice != Action.ATTACK:
                win_status, pokemon1, pokemon2, team2 = self.single_team_attack(pokemon2, pokemon1, team2)
                if win_status == None:
                    winner_result, team1, team2, pokemon1, pokemon2 = self.check_other_team_actions(second_team_choice, team1, team2, pokemon1, pokemon2)
                else: 
                    winner_result = 2

            #if both attack
            else:
                winner_result, pokemon1, pokemon2, team1, team2 = self.both_attack(pokemon1, pokemon2, team1, team2)
                
        #print ("Team 1 Pokemon is: ", end= ' ')
        #print (team1.retrieve_pokemon())
            
        if team1.is_empty() and team2.is_empty():
            winner_result = 0
        
        # remaining = []
        # while not team1.is_empty():
        #     remaining.append(team1.retrieve_pokemon())
        # print ()
        # print ("Length: " + str(len(remaining)))
        # print (remaining[0])
        
        return winner_result


    def check_other_team_actions(self, other_team_choice: Action, current_team: PokeTeam, other_team: PokeTeam, current_pokemon: PokemonBase, opponent_pokemon: PokemonBase) -> int:
        winner_result = None
        win_status = None
       
        if other_team_choice == Action.SWAP:
            other_team.return_pokemon(opponent_pokemon)
            opponent_pokemon = other_team.retrieve_pokemon()

        elif other_team_choice == Action.SPECIAL:
            other_team.return_pokemon(opponent_pokemon)
            other_team.special()
            opponent_pokemon = other_team.retrieve_pokemon()

        elif other_team_choice == Action.HEAL:
            #TODO check this heal > 0 part if it hasn't been already implemented in choose_battle_option (poke_team)
            if other_team.num_of_heals > 0:
                opponent_pokemon.heal()
                other_team.num_of_heals += 1
            else:
                winner_result = 1
                
        else: #time to attack
            win_status, opponent_pokemon, current_pokemon, current_team = self.single_team_attack(current_pokemon, opponent_pokemon, current_team)
            if win_status == "win":
                winner_result = 2
            else:
                pass
        return winner_result, current_team, other_team, current_pokemon, opponent_pokemon


    def single_team_attack (self, attacked_pokemon: PokemonBase, attacking_pokemon: PokemonBase, attacked_team: PokeTeam):
        
        attacker_win_status = None

        a = attacking_pokemon.get_hp()
        b = attacked_pokemon.get_hp()
        attacking_pokemon.attack(attacked_pokemon)
        c = attacked_pokemon.get_hp()
        if attacked_pokemon.is_fainted():
            attacking_pokemon.level_up()

            if attacking_pokemon.can_evolve() and attacking_pokemon.should_evolve():
                attacking_pokemon = attacking_pokemon.get_evolved_version()

            attacked_team.return_pokemon(attacked_pokemon)

            if not attacked_team.is_empty():
                attacked_pokemon = attacked_team.retrieve_pokemon()
            else:
                attacker_win_status = "win"
        
        else:
            c = attacked_pokemon.get_hp()
            attacked_pokemon.lose_hp(1)
            c = attacked_pokemon.get_hp()
            a = attacking_pokemon.get_hp()
            attacking_pokemon.lose_hp(1)
            a = attacking_pokemon.get_hp()

        return attacker_win_status, attacking_pokemon, attacked_pokemon, attacked_team

    
    def both_attack(self, first_pokemon: PokemonBase, second_pokemon: PokemonBase, first_team: PokeTeam, second_team: PokeTeam) -> int:
        winner_result = None
        
        pokemon1_speed = first_pokemon.get_speed()
        pokemon2_speed = second_pokemon.get_speed()

        if pokemon1_speed > pokemon2_speed:
            c = second_pokemon.get_hp()
            first_pokemon.attack(second_pokemon) 
            d = second_pokemon.get_hp()
            if not second_pokemon.is_fainted():  
                a = first_pokemon.get_hp()
                second_pokemon.attack(first_pokemon)
                b = first_pokemon.get_hp()
        
        elif pokemon2_speed > pokemon1_speed:
            a = first_pokemon.get_hp()
            second_pokemon.attack(first_pokemon)
            b = first_pokemon.get_hp()
            if not first_pokemon.is_fainted():
                c = second_pokemon.get_hp()
                first_pokemon.attack(second_pokemon)
                d = second_pokemon.get_hp()

        elif pokemon1_speed == pokemon2_speed:
            a = second_pokemon.get_hp()
            first_pokemon.attack(second_pokemon)
            b = second_pokemon.get_hp()
            c = first_pokemon.get_hp()
            second_pokemon.attack(first_pokemon)
            b = second_pokemon.get_hp()
            d = first_pokemon.get_hp()


        if first_pokemon.is_fainted() and not second_pokemon.is_fainted():
            second_pokemon.level_up()

            if second_pokemon.can_evolve() and second_pokemon.should_evolve():
                second_pokemon = second_pokemon.get_evolved_version()
            
            first_team.return_pokemon(first_pokemon)

            if not first_team.is_empty():
                first_pokemon = first_team.retrieve_pokemon()
            else:
                winner_result = 2
                second_team.return_pokemon(second_pokemon)

        elif second_pokemon.is_fainted() and not first_pokemon.is_fainted():
            first_pokemon.level_up()

            if first_pokemon.can_evolve() and first_pokemon.should_evolve():
                first_pokemon = first_pokemon.get_evolved_version()
                h = first_pokemon.get_hp()
            second_team.return_pokemon(second_pokemon)

            if not second_team.is_empty():
                second_pokemon = second_team.retrieve_pokemon()
            else:
                winner_result = 1
                first_team.return_pokemon(first_pokemon)

        elif (not first_pokemon.is_fainted()) and (not second_pokemon.is_fainted()):
            first_pokemon.lose_hp(1)
            b = first_pokemon.get_hp()
            second_pokemon.lose_hp(1)
            d = second_pokemon.get_hp()
            ###############################

        # if team2.is_empty():
        #     print (first_team.retrieve_pokemon())

        return winner_result, first_pokemon, second_pokemon, first_team, second_team



if __name__ == "__main__":
    # b = Battle(verbosity=3)
    # RandomGen.set_seed(16)
    # t1 = PokeTeam.random_team("Cynthia", 0, criterion=Criterion.SPD)
    # t1.ai_type = PokeTeam.AI.USER_INPUT
    # t2 = PokeTeam.random_team("Barry", 1)
    # print (b.battle(t1,t2))

    # RandomGen.set_seed(192837465)
    team1 = PokeTeam("Brock", [1, 1, 1, 1, 1], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.HP)
    team2 = PokeTeam("Misty", [0, 0, 0, 3, 3], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.SPD)
    b = Battle(verbosity=0)
    res = b.battle(team1, team2)

    # # arr = []
    # # while not team2.is_empty():
    # #         arr.append(team2.retrieve_pokemon())
    
    # # for i in range (len(arr)):
    # #     if i == 0:
    # #         print (arr[i].lose_hp(5))
    # #         print (arr[i])
    # #     else:
    # #         print (arr[i])
