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


            self.poke_dados_speed[c] = [dados_moves(self.poke_dados[c][3])[2], info(self.poke_dados[c][0])[0][5],
                                        self.poke_dados[c][1], self.poke_dados[c][0]]
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
            self.poke_dados[c].append(True)


    def sorteio_acc(self, atacante):

        self.atacante = self.poke_dados[atacante]
        self.alvo = self.poke_dados[self.atacante[14]]
        self.move_atacante = self.atacante[3]
        self.sorteio_num_acc = random.randrange(1, 101)
        if int(dados_moves(self.move_atacante)[1]) >= self.sorteio_num_acc:
            self.acertou = True

        else:
            self.acertou = False

        return self.acertou


    def sorteio_acc2(self, atacante, alvo):

        self.atacante = self.poke_dados[atacante]
        self.alvo = self.poke_dados[alvo]
        self.move_atacante = self.atacante[3]
        self.sorteio_num_acc = random.randrange(1, 101)
        if int(dados_moves(self.move_atacante)[1]) >= self.sorteio_num_acc:
            self.acertou = True

        else:
            self.acertou = False

        return self.acertou


    def calculo_dano(self, atacante, alvo):
        self.poke_one = self.poke_dados[atacante]
        self.poke_two = self.poke_dados[alvo]
        self.poke_one_lv = self.poke_one[1]
        self.move = self.poke_one[3]
        self.poke_one_trait = self.poke_one[2]
        self.poke_two_trait = self.poke_two[2]
        self.stats_atk_treinados = self.poke_one[4]
        self.stats_def_treinados = self.poke_two[5]
        self.stats_spatk_treinados = self.poke_one[6]
        self.stats_spdef_treinados = self.poke_two[7]
        self.stages_atk = self.poke_one[9]
        self.stages_def = self.poke_two[10]
        self.stages_spatk = self.poke_one[11]
        self.stages_spdef = self.poke_two[12]
        self.weather_rain = False
        self.weather_sandstorm = False
        self.weather_sunny = False

        self.move_type = int(dados_moves(self.move)[4])
        self.poke_one_type = []
        self.poke_one_type.append(int(convertType(info(self.poke_one[0])[2][0])))
        if len(info(self.poke_one[0])[2]) >= 2:
            self.poke_one_type.append(int(convertType(info(self.poke_one[0])[2][1])))

        self.poke_two_type = []
        self.poke_two_type.append(int(convertType(info(self.poke_two[0])[2][0])))
        if len(info(self.poke_two[0])[2]) >= 2:
            self.poke_two_type.append(int(convertType(info(self.poke_two[0])[2][1])))

        # TRAIT PROTEAN
        if self.poke_one_trait == 'protean':
            self.poke_one_type = [self.move_type]

        # TRAIT LIQUID VOICE
        self.liquid_voice = ['confide', 'disarming-voice', 'echoed-voice', 'hyper-voice', 'uproar', 'perish-song',
                             'round', 'sing', 'sparkling-aria']
        if self.poke_one_trait == 'liquid-voice':
            if self.move in self.liquid_voice:
                self.move_type = int(11)

        # AERILATE
        if self.poke_one_trait == 'aerilate' and self.move_type == 1:
            self.move_type = int(3)

        # TRAIT GALVANIZE
        if self.poke_one_trait == 'galvanize' and self.move_type == 1:
            self.move_type = int(13)

        # TRAIT REFRIGETARE
        if self.poke_one_trait == 'refrigerate' and self.move_type == 1:
            self.move_type = int(15)

        "WEARKNES"

        self.type_alvo = convertType(info(self.poke_two[0])[2][0])
        self.weakness_two = 1
        if len(info(self.poke_two[0])[2]) >= 2:
            self.type_alvo_two = convertType(info(self.poke_two[0])[2][1])
            self.weakness_two = weak(str(self.move_type), str(self.type_alvo_two))

        self.type_alvo_two = convertType(info(self.poke_two[0])[2][0])
        self.weaknes = weak(str(self.move_type), str(self.type_alvo_two))
        self.weaknes_final = float(self.weakness_two) * float(self.weaknes)
        if self.weaknes_final == 1.125:
            self.weaknes_final = 1
        "FIM DO WARKNES"

        # ================ POWER ====================
        # ==========================================
        # ==========================================
        "DEFINIDO STAB"
        if self.move_type in self.poke_one_type:
            self.stab = True

        else:
            self.stab = False

        self.stab_valor = float(1.2)
        "FIM DO STAB"

        # =================================
        # ========== CLASSE DE DANO ==========
        # =================================

        self.classe_dano = int(dados_moves(self.move)[3])

        if self.classe_dano == 2:
            self.atk = int(info(self.poke_one[0])[0][1]) + int(self.stats_atk_treinados)
            self.defe = int(info(self.poke_two[0])[0][2]) + int(self.stats_def_treinados)
            self.stage_valor = int(self.stages_atk) - int(self.stages_def)
        elif self.classe_dano == 3:
            self.atk = int(info(self.poke_one[0])[0][3]) + int(self.stats_spatk_treinados)
            self.defe = int(info(self.poke_two[0])[0][4]) + int(self.stats_spdef_treinados)
            self.stage_valor = int(self.stages_spatk) - int(self.stages_spdef)
            if self.weather_sandstorm == True:
                if int(6) in self.poke_two_type:
                    self.defe = self.defe * float(1.5)

        "FIM DA CLASSE DE DANO "

        # ADAPTABILITY
        if self.poke_one_trait == 'adaptability':
            self.stab_valor = float(1.4)

        # VALOR DO POWER
        self.power = int(dados_moves(self.move)[0])

        # =================================
        # ========== CLIMA RAIN AND SUNNY ==========
        # =================================

        if self.weather_rain == True:
            if self.move_type == 11:
                self.power = self.power * float(1.5)
            elif self.move_type == 10:
                self.power = self.power * float(0.5)

        if self.weather_sunny == True:
            if self.move_type == 10:
                self.power = self.power * float(1.5)
            elif self.move_type == 11:
                self.power = self.power * float(0.5)

        # TAIT SAND FORCE
        if self.poke_one_trait == 'sand-force' and self.weather_sandstorm == True:
            if self.move_type == 6:
                self.power = self.power * float(1.3)
            elif self.move_type == 5:
                self.power = self.power * float(1.3)
            elif self.move_type == 9:
                self.power = self.power * float(1.3)

        # TRAIT AERALITE
        if self.poke_one_trait == 'aerilate' and self.move_type == 3:
            self.power = self.power * float(1.2)
        # TRAIT GALVANIZE
        if self.poke_one_trait == 'galvanize' and self.move_type == 13:
            self.power = self.power * float(1.2)

        # TRAIT REFRIGERATE
        if self.poke_one_trait == 'refrigerate' and self.move_type == 13:
            self.power = self.power * float(1.2)

        # TRAIT TECHNICIAN
        if self.poke_one_trait == 'technician' and self.power <= 60:
            self.power = self.power * float(1.6)

        # VALOR DO STAB
        if self.stab == True:
            self.power = self.power * float(self.stab_valor)

        # TRAIT ANALYTIC
        if self.poke_one_trait == 'analytic':
            self.power = self.power * float(1.3)

        # TRAIT SHEER FORCE
        if self.poke_one_trait == 'sheer-force':
            self.power = self.power * float(1.3)

        # TRAIT TOUGH CLAWS
        if self.poke_one_trait == 'tough-claws':
            self.power = self.power * float(1.3)

        # TRAIT STAKEOUT
        if self.poke_one_trait == 'stakeout':
            self.power = self.power * 2

        # TRAIT STEELWORKER
        if self.poke_one_trait == 'steelworker' and self.move_type == 9:
            self.power = self.power * 2

        # TRAIT FLARE BOOST
        if self.poke_one_trait == 'flare-boost' and self.classe_dano == 3:
            self.power = self.power * float(1.5)

        # TRAIT IRON FIST
        self.iron_fist = ['bullet-punch', 'comet-punch', 'dizzy-punch', 'drain-punch', 'dynamic-punch', 'fire-punch',
                          'focus-punch', 'hammer-arm', 'ice-hammer', 'ice-punch', 'mach-punch', 'mega-punch',
                          'meteor-mash',
                          'power-up-punch', 'shadow-punch', 'sky-uppercut', 'thunder-punch']

        if self.poke_one_trait == 'iron-fist':
            if self.move in self.iron_fist:
                self.power = self.power * float(1.2)

        # TRAIT STRONG JAW
        self.strong_jaw = ['bite', 'crunch', 'fire-fang', 'hyper-fang', 'ice-fang', 'poison-fang', 'psychic-fang',
                           'tunder-fang']
        if self.poke_one_trait == 'strong-jaw':
            if self.move in self.strong_jaw:
                self.power = self.power * float(1.5)

        # TRAIT MEGA LAUNCHER
        self.mega_launcher = ['aura-sphere', 'dark-pulse', 'dragon-pulse', 'origin-pulse', 'water-pulse']
        if self.poke_one_trait == 'mega-launcher':
            if self.move in self.mega_launcher:
                self.power = self.power * float(1.2)

        # TRAIT NEUROFORCE
        if self.poke_one_trait == 'neuroforce' and self.weaknes_final >= 1.5:
            self.power = self.power * float(1.2)

        # TRAIT RECKLESS
        self.reckless = ['brave-bird', 'double-edge', 'flare-blitz', 'head-charge', 'head-smash', 'high-jump-kick',
                         'jump-kick',
                         'light-of-ruin', 'submission', 'take-down', 'volt-tackle', 'wood-hammer', 'wild-charge']
        if self.poke_one_type == 'reckless':
            if self.move in self.reckless:
                self.power = self.power * float(1.2)

        # =================================
        # ========== DANO BASE ==========
        # =================================
        self.dano_base = int(
            (2 * int(self.poke_one_lv) + 10) / 250 * ((120 - int(self.poke_one_lv)) / 150) * self.power)

        # TRAIT BLAZE
        if self.poke_one_trait == 'blaze' and self.move_type == 10:
            self.atk = self.atk * 1.5

        # TRAIT TORRENT
        if self.poke_one_trait == 'torrent' and self.move_type == 11:
            self.atk = self.atk * 1.5

        # TRAIT SWARM
        if self.poke_one_trait == 'swarm' and self.move_type == 7:
            self.atk = self.atk * 1.5

        # TRAIT OVERGROW
        if self.poke_one_trait == 'overgrow' and self.move_type == 12:
            self.atk = self.atk * 1.5

        # TRAIT FLASH FIRE
        if self.poke_one_trait == 'flash-fire':
            self.atk = self.atk * 1.5

        # TRAIT DEFEATIST
        if self.poke_one_trait == 'defeatist':
            self.atk = self.atk * 0.5
        # TRAIT GUTS
        if self.poke_one_trait == 'guts' and self.classe_dano == 2:
            self.atk = self.atk * 1.5

        # TRAIT HUGE POWER
        if self.poke_one_trait == 'huge-power' and self.classe_dano == 2:
            self.atk = self.atk * 2
        # TRAIT PURE POWER
        if self.poke_one_trait == 'pure-power' and self.classe_dano == 2:
            self.atk = self.atk * 2

        # TRAIT HUSTLE // FALTA PRECISÃO
        if self.poke_one_trait == 'hustle' and self.classe_dano == 2:
            self.atk = self.atk * 1.5

        # =================================
        # ========== BONUS DE STATS==========
        # =================================
        if self.atk > self.defe:
            self.bonus_stat = float(self.atk / self.defe / 3.3)
            self.dano = int((self.dano_base * self.bonus_stat) + self.dano_base)
        elif self.defe > self.atk:
            self.bonus_stat = float(self.defe / self.atk / 3.3)
            self.dano = int(self.dano_base - (self.dano_base * self.bonus_stat))
        else:
            self.bonus_stat = 1
            self.dano = self.dano_base * self.bonus_stat

        self.dano = self.dano * self.weaknes_final

        # =================================
        # ========== BONUS DE STAGES==========
        # =================================

        self.stages = {'1': float(1.2), '2': float(1.4), '3': float(1.6), '4': float(1.8), '5': float(2),
                       '6': float(2.2),
                       '7': float(2.4), '8': float(2.6), '9': float(2.8), '10': float(3), '11': float(3.2),
                       '12': float(3.4),
                       '-1': float(0.83), '-2': float(0.74), '-3': float(0.625), '-4': float(0.55), '-5': float(0.5),
                       '-6': float(0.45),
                       '-7': float(0.416), '-8': float(0.384), '-9': float(0.357), '-10': float(0.333),
                       '-11': float(0.312), '-12': float(0.294)}

        if int(self.stage_valor >= 1) or int(self.stage_valor) < 0:
            self.dano = self.dano * self.stages[str(self.stage_valor)]

        # =================================
        # ========== BONUS CRITICO  ==========
        # =================================

        self.chance_critico = {'0': 6.25, '1': 12.5, '2': 50, '3': 100}
        self.stage_critico = '0'
        self.critico_num_random = random.randrange(1, 101)
        if self.chance_critico[self.stage_critico] >= self.critico_num_random:
            if self.poke_one_trait == 'sniper':
                self.dano = self.dano * 2.25
            else:
                self.dano = self.dano * 1.5
            print('CRITICO!')

        # TRAIT FILTER
        if self.poke_two_trait == 'filter' and self.weaknes_final >= 1.5:
            self.dano = self.dano - (self.dano * 0.25)

        # TRAIT PARENTAL BOND
        if self.poke_one_trait == 'parental-bond':
            self.dano = self.dano = self.dano * 1.25

        # TRAIT TINTED LENS
        if self.poke_one_trait == 'tinted-lens' and self.weaknes_final <= 0.75:
            self.dano = self.dano * 2

        # =================================
        # ========== BURN ==========
        # =================================
        self.status_burn = False
        if self.status_burn == True:
            self.dano = self.dano / 2

        if self.weaknes_final == 0.5625:
            self.texto_efetividade = ("O {}  resistiu duplamente ao golpe!").format(self.poke_two[0])
        elif self.weaknes_final == 0.75:
            self.texto_efetividade = ("O {} alvo resistiu  ao golpe!").format(self.poke_two[0])
        elif self.weaknes_final == 1:
            self.texto_efetividade = ("O {} recebeu dano normal").format(self.poke_two[0])
        elif self.weaknes_final == 0:
            self.texto_efetividade = ("O {} não é afetado por este tipo de golpe!").format(self.poke_two[0])
        elif self.weaknes_final == 1.5:
            self.texto_efetividade = ("O {} recebeu um golpe efetivo!").format(self.poke_two[0])
        elif self.weaknes_final == 2.25:
            self.texto_efetividade = ("O {} recebeu um golpe duplamente efetivo!").format(self.poke_two[0])

        if self.dano <0:
            self.dano = 0
        self.resultado = ('O  {} atacou  o  {} com o movimento {}, causando {} de dano. {}\n'.format(self.poke_one[0], self.poke_two[0],
                                                                                       self.move, int(self.dano),
                                                                                       self.texto_efetividade))

        #print('{}: {} Power // STAB: {}'.format(self.move, self.power, self.stab))
        #print('{}: Atk/Sp.Atk: {}'.format(self.poke_one, self.atk))
        #print('{}: Def/Sp.Def: {}'.format(self.poke_two, self.defe))
        #print('Stages Atk: {}, Stages Spatk {}, Stages DEF: {}, Stages SPDEF: {}'.format(self.stages_atk,
                                                                                         #self.stages_spatk,
                                                                                         #self.stages_def,
                                                                                         #self.stages_spdef))



        return self.resultado