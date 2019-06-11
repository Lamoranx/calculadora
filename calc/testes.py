from Gerador import *
from GeradorPokemon import *
import random


class OrdemPoke:

    def __init__(self, poke_dados):
        self.poke_dados = poke_dados

    def ordem_ataque(self):
        self.poke_dados_speed = {}

        self.stages = {'1': float(1.2), '2': float(1.4), '3': float(1.6), '4': float(1.8), '5': float(2),
                       '6': float(2.2),
                       '7': float(2.4), '8': float(2.6), '9': float(2.8), '10': float(3), '11': float(3.2),
                       '12': float(3.4),
                       '-1': float(0.83), '-2': float(0.74), '-3': float(0.625), '-4': float(0.55), '-5': float(0.5),
                       '-6': float(0.45),
                       '-7': float(0.416), '-8': float(0.384), '-9': float(0.357), '-10': float(0.333),
                       '-11': float(0.312), '-12': float(0.294)}

        for c in self.poke_dados:
            self.poke_dados_speed[c] =  [dados_moves(self.poke_dados[c][3])[2], info(self.poke_dados[c][0])[0][5], self.poke_dados[c][1], self.poke_dados[c][0]]
            self.poke_dados_speed[c][1] = int(self.poke_dados_speed[c][1]) + int(self.poke_dados[c][8])
            if int(self.poke_dados[c][13]) != 0:
                self.poke_dados_speed[c][1] = int(self.poke_dados_speed[c][1]) * self.stages[self.poke_dados[c][13]]


        self.lista_speed_ordenado = sorted(self.poke_dados_speed, key=self.poke_dados_speed.get, reverse=True)



    def hp(self):
        for c in self.lista_speed_ordenado:
            self.hp_base = int(info(self.poke_dados[c][0])[0][0])
            self.lv = int(self.poke_dados[c][1])
            self.hp_total = ((2 * self.hp_base) * self.lv / 100) + (self.lv) + 10
            self.poke_dados[c].append(int(self.hp_total))



    def sorteio_acc(self, atacante, alvo, move_atacante):
        self.atacante = atacante
        self.alvo = alvo
        self.move_atacante = move_atacante
        self.sorteio_num_acc = random.randrange(1, 101)
        if int(dados_moves(self.move_atacante)[1]) >= self.sorteio_num_acc:
            self.acertou = True

        else:
            self.acertou = False


        return  self.acertou