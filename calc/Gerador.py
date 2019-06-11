import os
import csv
from os import listdir
from collections import OrderedDict



ListaNomes = []
TypesLista = []
MovesLista = []
Dados_Moves = []


with open('data/pokemon.csv', 'r') as pokemon:
    reader = csv.DictReader(pokemon)
    for linhas in reader:
        ListaNomes.append(linhas['identifier'])

with open('data/types.csv', 'r') as types:
    reader = csv.DictReader(types)
    for linhas in reader:
        TypesLista.append(linhas['identifier'])


with open('data/moves.csv', 'r') as moves:
    reader = csv.DictReader(moves)
    for linhas in reader:
        MovesLista.append(linhas['identifier'])
        MovesLista = sorted(set(MovesLista))





def dados_moves(movimento):

    Dados_Moves.clear()

    with open('data/moves.csv', 'r') as moves:
        reader = csv.DictReader(moves)
        for linhas in reader:
            if linhas['identifier'] == movimento:
                Dados_Moves.append(linhas['power'])
                Dados_Moves.append(linhas['accuracy'])
                Dados_Moves.append(linhas['priority'])
                Dados_Moves.append(linhas['damage_class_id'])
                Dados_Moves.append(linhas['type_id'])
                Dados_Moves.append(linhas['target_id'])

    return Dados_Moves



def weak (TypeMove, TypeAlvo):

    with open('data/type_efficacy.csv', 'r') as efficacy:
        reader = csv.DictReader(efficacy)
        for linhas in reader:
            if linhas['damage_type_id'] == TypeMove:
                if linhas['target_type_id'] == TypeAlvo:
                    fator= linhas['damage_factor']

    return fator

def convertType (type):
    with open('data/types.csv', 'r') as types:
        reader = csv.DictReader(types)
        for linhas in reader:
            if linhas['identifier'] == type:
                idtype = linhas['id']
    return idtype


'''tipo = convertType('fire')
tipodois = convertType('grass')

print(weak(tipo, tipodois))

#print(convertType('fire'))'''

teste = dados_moves('absorb')
print(teste)
teste[5] = 20
print(teste)
print(dados_moves('absorb'))
