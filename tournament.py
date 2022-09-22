from __future__ import annotations

from stack_adt import ArrayStack

"""
"""
__author__ = "Scaffold by Jackson Goerner, Code by ______________"

from poke_team import PokeTeam
from battle import Battle
from linked_list import LinkedList
from battle import Battle

class Tournament:
    
    def __init__(self, battle: Battle|None=None) -> None:
        self.teams = None
        self.battle_mode = None
        self.tournament_list = LinkedList()

        if battle is None:
            self.battle = Battle()
        else :
            self.battle = battle

    def set_battle_mode(self, battle_mode: int) -> None:
        self.battle_mode = battle_mode

    def is_valid_tournament(self, tournament_str: str) -> bool:
        
        str_split_postfix = tournament_str.split()
        postfix_operands = LinkedList()
        s = LinkedList()

        for i in str_split_postfix:
            # Push operands
            if i != '+':
                s.insert(0, i)
                postfix_operands.insert(len(postfix_operands),i)
            else:
                op1 = s[0]
                s.delete_at_index(0)
                op2 = s[0]
                s.delete_at_index(0)
                s.insert(0, "( " + op2 + " " + i + " " +
                        op1 + " )")

        result_infix = s[0][1:-1]

        str_split_infix = result_infix.split()
        infix_operands = LinkedList()

        for i in str_split_infix:
            if i != '+' and i != '(' and i != ')':
                infix_operands.insert(len(infix_operands),i)

        if len(infix_operands) == len(postfix_operands):
            return True
        else:
            return False
         

    def is_balanced_tournament(self, tournament_str: str) -> bool:
        # 1054 only
        raise NotImplementedError()

    def start_tournament(self, tournament_str: str) -> None:
        
        if not type(tournament_str) == str :
            raise TypeError("A string is expected for tournament_str")

        if self.is_valid_tournament(tournament_str) :
            tournament_str_split = tournament_str.split()

            self.teams = LinkedList()
            team_names = LinkedList()

            for i in tournament_str_split :
                if i != '+' :             
                     team_names.insert(len(team_names),i)  

            for j in range(len(team_names)):
                poke_team = PokeTeam.random_team(team_names[j],self.battle_mode)
                self.teams.insert(len(self.teams),poke_team)

            for i in range(len(tournament_str_split)):
                for j in range(len(self.teams)):
                    if tournament_str_split[i] == self.teams[j].team_name :
                        self.tournament_list.insert(i,self.teams[j])
                        break
                else:
                    self.tournament_list.insert(i,tournament_str_split[i])

    
    def advance_tournament(self) -> tuple[PokeTeam, PokeTeam, int] | None:
        index = self.tournament_list.index("+")
        poketeam1 = self.tournament_list[index-2]
        poketeam2 = self.tournament_list[index-1]
        result = self.battle.battle(poketeam1,poketeam2)

        if result == 1 :
            self.tournament_list.delete_at_index(index)
            self.tournament_list.remove(poketeam2)
        elif result == 2:
            self.tournament_list.delete_at_index(index)
            self.tournament_list.remove(poketeam1)

        return (poketeam1,poketeam2,result)


    def linked_list_of_games(self) -> LinkedList[tuple[PokeTeam, PokeTeam]]:
        l = LinkedList()
        while True:
            res = self.advance_tournament()
            if res is None:
                break
            l.insert(0, (res[0], res[1]))
        return l
    
    def linked_list_with_metas(self) -> LinkedList[tuple[PokeTeam, PokeTeam, list[str]]]:
        l = LinkedList()
        while True:
            res = self.advance_tournament()
            if res is None:
                break
            
            
            l.insert(0, (res[0], res[1],res[2]))
        return l
    
    def flip_tournament(self, tournament_list: LinkedList[tuple[PokeTeam, PokeTeam]], team1: PokeTeam, team2: PokeTeam) -> None:
        # 1054
        raise NotImplementedError()
