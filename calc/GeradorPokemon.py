import os
import csv
from os import listdir
from collections import OrderedDict



class GeradorPokémon:

    Pokémon = OrderedDict()

    Habilidades = OrderedDict()
    Moves = OrderedDict()








#INICIANDO CONSTRUTOR, LIMPANDO LISTAS E ATRIBUINDO ID AO NOME DOS POKÉMON
    def __init__(self, pokenome):
        self.pokenome = pokenome







        with open('data/pokemon.csv', 'r') as pokemon:
            reader = csv.DictReader(pokemon)
            for linhas in reader:
                self.Pokémon[linhas['identifier']] = linhas['id']
        self.pokenome = self.Pokémon[self.pokenome]
#FUNÇÕES QUE RETORNA OS POKÉMON/ID
    def poke_list(self):

        return  self.Pokémon



#RETORNA OS STATS DO POKÉMON
    def poke_stats(self):
        self.Pokémon_Stats = []
        with open('data/pokemon_stats.csv', 'r') as stats:
            reader = csv.DictReader(stats)

            for linhas in reader:
                if linhas['pokemon_id'] == self.pokenome:
                    self.Pokémon_Stats.append(linhas['base_stat'])


        return self.Pokémon_Stats


#RETORNA OS TYPES DOS POKÉMON
    def poke_types(self):
        self.Types = OrderedDict()

        self.Pokémon_Types = []
        self.Types_Pokémon = []


        with open('data/types.csv', 'r') as types:
            reader = csv.DictReader(types)
            for linhas in reader:
                self.Types[linhas['id']] = linhas['identifier']

        with open('data/pokemon_types.csv', 'r') as pokemon_types:
            reader = csv.DictReader(pokemon_types)
            for linhas in reader:
                if linhas['pokemon_id'] == self.pokenome:
                    self.Pokémon_Types.append(linhas['type_id'])
        cont = 0
        for c in self.Pokémon_Types:
            self.Types_Pokémon.append(self.Types[self.Pokémon_Types[cont]])
            cont += 1

        return self.Types_Pokémon


#RETORNA AS TRAITS DO POKÉMON

    def poke_traits(self):
        self.Pokémon_Abilities = []
        self.Abilities_Pokémon = []
        with open('data/abilities.csv', 'r') as abilities:
            reader = csv.DictReader(abilities)
            for linhas in reader:
                self.Habilidades[linhas['id']] = linhas['identifier']

        with open('data/pokemon_abilities.csv') as pokemon_abilities:
            reader = csv.DictReader(pokemon_abilities)
            for linhas in reader:
                if linhas['pokemon_id'] == self.pokenome:
                    self.Pokémon_Abilities.append(linhas['ability_id'])
        cont = 0
        for c in self.Pokémon_Abilities:
            self.Abilities_Pokémon.append(self.Habilidades[self.Pokémon_Abilities[cont]])
            cont += 1

        return  self.Abilities_Pokémon


#RETORNA OS MOVES DO POKÉMON

    def poke_moves(self):
        self.Pokémon_Moves = []
        self.Moves_Pokémon = []
        with open('data/moves.csv', 'r') as moves:
            reader = csv.DictReader(moves)
            for linhas in reader:
                self.Moves[linhas['id']] = linhas['identifier']

        with open('data/pokemon_moves.csv') as pokemon_moves:
            reader = csv.DictReader(pokemon_moves)
            for linhas in reader:
                if linhas['pokemon_id'] == self.pokenome:
                    self.Pokémon_Moves.append(linhas['move_id'])


            cont = 0
            for c in self.Pokémon_Moves:
                self.Moves_Pokémon.append(self.Moves[self.Pokémon_Moves[cont]])
                cont += 1
            self.Moves_Pokémon = sorted(set(self.Moves_Pokémon))
            return  self.Moves_Pokémon

def info(nome):
    player = GeradorPokémon(nome)
    stats = player.poke_stats()
    traits = player.poke_traits()
    types = player.poke_types()
    #moves = player.poke_moves()

    return stats, traits, types




