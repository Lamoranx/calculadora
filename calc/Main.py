from tkinter import *
from tkinter import ttk
from  Gerador import *
from GeradorPokemon import *
from Dano import *
from misc import *
from autocomplete import  *
from tkinter.scrolledtext import *
import sys







class CalculadoraDano:



    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.grid()
        self.lado_right()





    def lado_right(self):
        self.cliques = 0
        self.lista_alvo = ['Slot1', 'Slot2', 'Slot3', 'Slot4', 'Slot5', 'Slot6',]

        pokes_dados = {}
        def iniciar_batalha():
            print(self.cliques)





            lista_slots = {'Slot1': [self.SeletorPokémom.get()], 'Slot2': [self.SeletorPokémomR1.get()],
                           'Slot3': [self.SeletorPokémomR2.get()],
                           'Slot4': [self.SeletorPokémomL1.get()], 'Slot5': [self.SeletorPokémomL2.get()],
                           'Slot6': [self.SeletorPokémomL3.get()]}


            dados = {"Slot1": [self.SeletorPokémom.get(), self.SpinLv.get(), self.ComboTrait.get(),
                               self.ComboMoves.get(), self.EntryBonusAtk.get(), self.EntryBonusDef.get(),
                               self.EntryBonusSpa.get(), self.EntryBonusSpd.get(), self.EntryBonusSpe.get(),
                               self.SpinAtk.get(), self.SpinDef.get(), self.SpinSpa.get(), self.SpinSpd.get(),
                               self.SpinSpe.get(), self.poke_alvo.get(),],
                     "Slot2": [self.SeletorPokémomR1.get(), self.SpinLvR1.get(), self.ComboTraitR1.get(),
                               self.ComboMovesR1.get(), self.EntryBonusAtkR1.get(), self.EntryBonusDefR1.get(),
                               self.EntryBonusSpaR1.get(), self.EntryBonusSpdR1.get(),
                               self.EntryBonusSpeR1.get(),
                               self.SpinAtkR1.get(), self.SpinDefR1.get(), self.SpinSpaR1.get(),
                               self.SpinSpdR1.get(),
                               self.SpinSpeR1.get(), self.poke_alvoR1.get()],
                     "Slot3": [self.SeletorPokémomR2.get(), self.SpinLvR2.get(), self.ComboTraitR2.get(),
                               self.ComboMovesR2.get(), self.EntryBonusAtkR2.get(),
                               self.EntryBonusDefR2.get(),
                               self.EntryBonusSpaR2.get(), self.EntryBonusSpdR2.get(),
                               self.EntryBonusSpeR2.get(),
                               self.SpinAtkR2.get(), self.SpinDefR2.get(), self.SpinSpaR2.get(),
                               self.SpinSpdR2.get(),
                               self.SpinSpeR2.get(), self.poke_alvoR2.get()],
                     "Slot4": [self.SeletorPokémomL1.get(), self.SpinLvL1.get(), self.ComboTraitL1.get(),
                               self.ComboMovesL1.get(), self.EntryBonusAtkL1.get(),
                               self.EntryBonusDefL1.get(),
                               self.EntryBonusSpaL1.get(), self.EntryBonusSpdL1.get(),
                               self.EntryBonusSpeL1.get(),
                               self.SpinAtkL1.get(), self.SpinDefL1.get(), self.SpinSpaL1.get(),
                               self.SpinSpdL1.get(),
                               self.SpinSpeL1.get(), self.poke_alvoL1.get()],
                     "Slot5": [self.SeletorPokémomL2.get(), self.SpinLvL2.get(), self.ComboTraitL2.get(),
                               self.ComboMovesL2.get(), self.EntryBonusAtkL2.get(),
                               self.EntryBonusDefL2.get(),
                               self.EntryBonusSpaL2.get(), self.EntryBonusSpdL2.get(),
                               self.EntryBonusSpeL2.get(),
                               self.SpinAtkL2.get(), self.SpinDefL2.get(), self.SpinSpaL2.get(),
                               self.SpinSpdL2.get(),
                               self.SpinSpeL2.get(), self.poke_alvoL2.get()],
                     "Slot6": [self.SeletorPokémomL3.get(), self.SpinLvL3.get(), self.ComboTraitL3.get(),
                               self.ComboMovesL3.get(), self.EntryBonusAtkL3.get(),
                               self.EntryBonusDefL3.get(),
                               self.EntryBonusSpaL3.get(), self.EntryBonusSpdL3.get(),
                               self.EntryBonusSpeL3.get(),
                               self.SpinAtkL3.get(), self.SpinDefL3.get(), self.SpinSpaL3.get(),
                               self.SpinSpdL3.get(),
                               self.SpinSpeL3.get(), self.poke_alvoL3.get()]}

            for k, v in lista_slots.items():
                if v != ['']:
                    pokes_dados[k] = dados[k]


            ordem = OrdemPoke(pokes_dados)
            ordem.ordem_ataque()
            ordem.hp()

            if self.cliques ==0:
                self.cliques += 1
                self.resultado_texto.insert('1.0', 'INICIANDO BATALHA!\n')
                for c in ordem.lista_speed_ordenado:
                    self.resultado_texto.insert('end-1c','\nPokémon: {} // Lv: {}// HP: {}/{}'.format(ordem.poke_dados[c][0], ordem.poke_dados[c][1], ordem.poke_dados[c][15], ordem.poke_dados[c][15]))




            return


        def prox_turno():
            #GERANDO ORDEM DE ATAQUE DOS POKÉMON
            ordem = OrdemPoke(pokes_dados)
            ordem.ordem_ataque()
            #VERIFICANDO MUDANÇA NO MOVIMENTO SELECIONADO
            for c in ordem.lista_speed_ordenado:


                dados = {"Slot1": [self.ComboMoves.get()],
                         "Slot2": [self.ComboMovesR1.get()],
                         "Slot3": [self.ComboMovesR2.get()],
                         "Slot4": [self.ComboMovesL1.get()],
                         "Slot5": [self.ComboMovesL2.get()],
                         "Slot6": [self.ComboMovesL3.get()]}
                pokes_dados[c][3] = dados[c][0]
                self.resultado_texto.insert('end-1c',
                                            '\nPokémon: {} // Lv: {}// HP: {}/{}'.format(ordem.poke_dados[c][0],
                                                                                         ordem.poke_dados[c][1],
                                                                                         ordem.poke_dados[c][15],
                                                                                         ordem.poke_dados[c][15]))


                #VERIFICANDO SE O POKÉMON E O ALVO TEM HP
                if ordem.poke_dados[c][16] == True and dados_moves(pokes_dados[c][3])[5] == '10':
                    # VERIFICANDO SE O POKÉMON ALVO ESTÁ DESMAIADO
                    if ordem.poke_dados[ordem.poke_dados[c][14]][16] == False:

                        all_enemys = {'Slot1': ['Slot4', 'Slot5', 'Slot6'],
                                      'Slot2': ['Slot4', 'Slot5', 'Slot6'],
                                      'Slot3': ['Slot4', 'Slot5', 'Slot6'],
                                      'Slot4': ['Slot1', 'Slot2', 'Slot3'],
                                      'Slot5': ['Slot1', 'Slot2', 'Slot3'],
                                      'Slot6': ['Slot1', 'Slot2', 'Slot3']}
                        all_enemys[c].remove(ordem.poke_dados[c][14])
                        # TROCANDO O POKÉMON ALVO
                        for slots in all_enemys[c]:
                            if slots in ordem.lista_speed_ordenado:
                                ordem.poke_dados[c][14] = slots

                    if dados_moves(pokes_dados[c][3])[5] == '10':
                        ordem.sorteio_acc(c)

                        ordem.calculo_dano(c, ordem.poke_dados[c][14])
                        ordem.poke_dados[ordem.poke_dados[c][14]][15] = int(
                            ordem.poke_dados[ordem.poke_dados[c][14]][15]) - int(ordem.dano)
                        self.resultado_texto.insert('end-1c', '\n {}'.format(ordem.resultado))
                        if ordem.poke_dados[ordem.poke_dados[c][14]][15] <=0:
                            ordem.poke_dados[ordem.poke_dados[c][14]][16] = False
                            print(ordem.poke_dados[ordem.poke_dados[c][14]])
                            self.resultado_texto.insert('end-1c', '{} desmaiou!'.format(ordem.poke_dados[ordem.poke_dados[c][14]][0]))



                if dados_moves(pokes_dados[c][3])[5] == '9':
                    all_adjacent = {'Slot1': ['Slot2', 'Slot4', 'Slot5'],
                                    'Slot2': ['Slot1', 'Slot3', 'Slot4', 'Slot5', 'Slot6'],
                                    'Slot3': ['Slot2', 'Slot5', 'Slot6'],
                                    'Slot4': ['Slot5', 'Slot1', 'Slot2'],
                                    'Slot5': ['Slot6', 'Slot4', 'Slot1', 'Slot2', 'Slot3'],
                                    'Slot6': ['Slot5', 'Slot2', 'Slot3']}

                    for slots in all_adjacent[c]:
                        if slots in ordem.lista_speed_ordenado:
                            if ordem.poke_dados[slots][16] == True:

                                ordem.sorteio_acc2(c, slots)
                                ordem.calculo_dano(c, slots)
                                ordem.poke_dados[slots][15] = ordem.poke_dados[slots][15] - int(ordem.dano)
                                print(ordem.poke_dados[slots][15])
                                self.resultado_texto.insert('end-1c', '\n {}'.format(ordem.resultado))
                                if ordem.poke_dados[slots][15] <=0:
                                    ordem.poke_dados[slots][16] = False
                                    self.resultado_texto.insert('end-1c', '{} desmaiou!'.format( ordem.poke_dados[slots][0]))


            return

        def limpar_frame():
            self.resultado_texto.delete('1.0', END)
            self.SeletorPokémom.set("")
            self.EntryHp.delete(0, END)
            self.EntryAtk.delete(0, END)
            self.EntryDef.delete(0, END)
            self.EntrySpa.delete(0, END)
            self.EntrySpd.delete(0, END)
            self.EntrySpe.delete(0, END)
            self.ComboType.set('')
            self.ComboTrait.set('')


        def return_entry(get):
            Player = self.SeletorPokémom.get()






            self.EntryHp.delete(0, END)
            self.EntryAtk.delete(0, END)
            self.EntryDef.delete(0, END)
            self.EntrySpa.delete(0, END)
            self.EntrySpd.delete(0, END)
            self.EntrySpe.delete(0, END)
            self.ComboType.set('')
            self.ComboTrait.set('')
            self.EntryHp.insert(0, info(Player)[0][0])
            self.EntryAtk.insert(0, info(Player)[0][1])
            self.EntryDef.insert(0, info(Player)[0][2])
            self.EntrySpa.insert(0, info(Player)[0][3])
            self.EntrySpd.insert(0, info(Player)[0][4])
            self.EntrySpe.insert(0, info(Player)[0][5])
            self.ComboType['values'] = info(Player)[2]
            self.ComboType.set(info(Player)[2][0])
            self.ComboTrait['values'] = info(Player)[1]
            #self.ComboTrait.set(info(Player)[1][0])


            return

        def return_entry_dois(get):
            Player = self.SeletorPokémomR1.get()






            self.EntryHpR1.delete(0, END)
            self.EntryAtkR1.delete(0, END)
            self.EntryDefR1.delete(0, END)
            self.EntrySpaR1.delete(0, END)
            self.EntrySpdR1.delete(0, END)
            self.EntrySpeR1.delete(0, END)
            self.ComboTypeR1.set('')
            self.ComboTraitR1.set('')
            self.EntryHpR1.insert(0, info(Player)[0][0])
            self.EntryAtkR1.insert(0, info(Player)[0][1])
            self.EntryDefR1.insert(0, info(Player)[0][2])
            self.EntrySpaR1.insert(0, info(Player)[0][3])
            self.EntrySpdR1.insert(0, info(Player)[0][4])
            self.EntrySpeR1.insert(0, info(Player)[0][5])
            self.ComboTypeR1['values'] = info(Player)[2]
            self.ComboTypeR1.set(info(Player)[2][0])
            self.ComboTraitR1['values'] = info(Player)[1]
            #self.ComboTrait.set(info(Player)[1][0])


            return

        def return_entry_tres(get):
            Player = self.SeletorPokémomR2.get()






            self.EntryHpR2.delete(0, END)
            self.EntryAtkR2.delete(0, END)
            self.EntryDefR2.delete(0, END)
            self.EntrySpaR2.delete(0, END)
            self.EntrySpdR2.delete(0, END)
            self.EntrySpeR2.delete(0, END)
            self.ComboTypeR2.set('')
            self.ComboTraitR2.set('')
            self.EntryHpR2.insert(0, info(Player)[0][0])
            self.EntryAtkR2.insert(0, info(Player)[0][1])
            self.EntryDefR2.insert(0, info(Player)[0][2])
            self.EntrySpaR2.insert(0, info(Player)[0][3])
            self.EntrySpdR2.insert(0, info(Player)[0][4])
            self.EntrySpeR2.insert(0, info(Player)[0][5])
            self.ComboTypeR2['values'] = info(Player)[2]
            self.ComboTypeR2.set(info(Player)[2][0])
            self.ComboTraitR2['values'] = info(Player)[1]
            #self.ComboTrait.set(info(Player)[1][0])


            return


        def retorno_dois(get):
            Player = self.SeletorPokémomL2.get()






            self.EntryHpL2.delete(0, END)
            self.EntryAtkL2.delete(0, END)
            self.EntryDefL2.delete(0, END)
            self.EntrySpaL2.delete(0, END)
            self.EntrySpdL2.delete(0, END)
            self.EntrySpeL2.delete(0, END)
            self.ComboTypeL2.set('')
            self.ComboTraitL2.set('')
            self.EntryHpL2.insert(0, info(Player)[0][0])
            self.EntryAtkL2.insert(0, info(Player)[0][1])
            self.EntryDefL2.insert(0, info(Player)[0][2])
            self.EntrySpaL2.insert(0, info(Player)[0][3])
            self.EntrySpdL2.insert(0, info(Player)[0][4])
            self.EntrySpeL2.insert(0, info(Player)[0][5])
            self.ComboTypeL2['values'] = info(Player)[2]
            self.ComboTypeL2.set(info(Player)[2][0])
            self.ComboTraitL2['values'] = info(Player)[1]
            #self.ComboTrait.set(info(Player)[1][0])


            return






        def retorno_tres(get):
            Player = self.SeletorPokémomL3.get()






            self.EntryHpL3.delete(0, END)
            self.EntryAtkL3.delete(0, END)
            self.EntryDefL3.delete(0, END)
            self.EntrySpaL3.delete(0, END)
            self.EntrySpdL3.delete(0, END)
            self.EntrySpeL3.delete(0, END)
            self.ComboTypeL3.set('')
            self.ComboTraitL3.set('')
            self.EntryHpL3.insert(0, info(Player)[0][0])
            self.EntryAtkL3.insert(0, info(Player)[0][1])
            self.EntryDefL3.insert(0, info(Player)[0][2])
            self.EntrySpaL3.insert(0, info(Player)[0][3])
            self.EntrySpdL3.insert(0, info(Player)[0][4])
            self.EntrySpeL3.insert(0, info(Player)[0][5])
            self.ComboTypeL3['values'] = info(Player)[2]
            self.ComboTypeL3.set(info(Player)[2][0])
            self.ComboTraitL3['values'] = info(Player)[1]
            #self.ComboTrait.set(info(Player)[1][0])


            return













        def retorno(get):
            PlayerTwo = self.SeletorPokémomL1.get()


            self.EntryHpL1.delete(0, END)
            self.EntryAtkL1.delete(0, END)
            self.EntryDefL1.delete(0, END)
            self.EntrySpaL1.delete(0, END)
            self.EntrySpdL1.delete(0, END)
            self.EntrySpeL1.delete(0, END)
            self.ComboTypeL1.set('')
            self.ComboTraitL1.set('')
            self.EntryHpL1.insert(0, info(PlayerTwo)[0][0])
            self.EntryAtkL1.insert(0, info(PlayerTwo)[0][1])
            self.EntryDefL1.insert(0, info(PlayerTwo)[0][2])
            self.EntrySpaL1.insert(0, info(PlayerTwo)[0][3])
            self.EntrySpdL1.insert(0, info(PlayerTwo)[0][4])
            self.EntrySpeL1.insert(0, info(PlayerTwo)[0][5])
            self.ComboTypeL1['values'] = info(PlayerTwo)[2]
            self.ComboTypeL1.set(info(PlayerTwo)[2][0])
            self.ComboTraitL1['values'] = info(PlayerTwo)[1]
            self.ComboTraitL1.set(info(PlayerTwo)[1][0])
            return

        self.FrameRight = LabelFrame(self.frame, text="JOGADOR 1")
        self.FrameLeft = LabelFrame(self.frame, text="JOGADOR 2")
        self.FrameRight.grid(row=0, column=0, pady=10, padx=10)
        self.Field = LabelFrame(self.frame, text="Field")
        self.resultado = LabelFrame(self.frame, text="RESULTADO")
        self.branco = LabelFrame(self.frame)

        self.note = ttk.Notebook(self.FrameRight)
        self.tab1 = ttk.Frame(self.note)
        self.tab2 = ttk.Frame(self.note)
        self.tab3 = ttk.Frame(self.note)
        self.note.add(self.tab1, text="Pokémon 1", compound=TOP)
        self.note.add(self.tab2, text="Pokémon 2")
        self.note.add(self.tab3, text="Pokémon 3")
        self.note.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW', pady=20, padx=20)
        self.FrameDados = LabelFrame(self.tab1, text="DADOS")
        self.FrameStats = LabelFrame(self.tab1, text="STATS")
        self.FrameOutros = LabelFrame(self.tab1, text="Outros")
        self.FrameDados.grid(pady = 20, ipadx = 60, padx = 10)



        self.PokémonLabel = ttk.Label(self.FrameDados, text="Pokémon")
        self.SeletorPokémom = AutocompleteCombobox( self.FrameDados, width=16)
        self.SeletorPokémom.set_completion_list(ListaNomes)

        self.SeletorPokémom.bind('<<ComboboxSelected>>', return_entry)
        self.LabelType = Label(self.FrameDados, text="Type")
        self.ComboType = ttk.Combobox(self.FrameDados, width=15)
        self.LabelGender = Label(self.FrameDados, text="Gender")
        self.ComboGender = ttk.Combobox(self.FrameDados, width=15, values=['Male', 'Female'])
        self.ComboGender.set('Male')
        self.LabelTrait = Label(self.FrameDados, text="Ability")
        self.ComboTrait = ttk.Combobox(self.FrameDados, width=15)
        self.LabelLv = Label(self.FrameDados, text="Level")
        self.SpinLv = Spinbox(self.FrameDados, from_=50, to=100, width=3)

        self.PokémonLabel.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.SeletorPokémom.grid(row=0, column=1, padx=1, pady=1)
        self.LabelType.grid(row=1, column=0, padx=1, pady=1, sticky='w')
        self.ComboType.grid(row=1, column=1, padx=1, pady=1, sticky='w')
        self.LabelGender.grid(row=3, column=0, padx=1, pady=1, sticky='w')
        self.ComboGender.grid(row=3, column=1, padx=1, pady=1, sticky='w')
        self.LabelTrait.grid(row=4, column=0, padx=1, pady=1, sticky='w')
        self.ComboTrait.grid(row=4, column=1, padx=1, pady=1, sticky='w')
        self.LabelLv.grid(row=5, column=0, padx=1, pady=1, sticky='w')
        self.SpinLv.grid(row=5, column=1, padx=1, pady=1, sticky='w')

        self.FrameStats.grid(sticky='w', ipadx=65, padx=20)
        self.LabelBase = Label(self.FrameStats, text="Base")
        self.LabelBranco = Label(self.FrameStats, text="", width=5)
        self.LabelBonus = Label(self.FrameStats, text="Bônus")
        self.LabelStages = Label(self.FrameStats, text="Stages")

        self.LabelBranco.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.LabelBase.grid(row=0, column=1, padx=1, pady=1, sticky='w')
        self.LabelBonus.grid(row=0, column=2, padx=1, pady=1, sticky='w')
        self.LabelStages.grid(row=0, column=3, padx=1, pady=1, sticky='w')

        status = ['HP', 'Attack', 'Defense', 'Sp.Atk', 'Sp.Def', 'Speed']

        rl = 1
        for c in status:
            Label(self.FrameStats, text=c).grid(row=rl, column=0, padx=1, pady=1, sticky='w')
            rl = rl + 1

        self.EntryHp = Entry(self.FrameStats, width=4)
        self.EntryAtk = Entry(self.FrameStats, width=4)
        self.EntryDef = Entry(self.FrameStats, width=4)
        self.EntrySpa = Entry(self.FrameStats, width=4)
        self.EntrySpd = Entry(self.FrameStats, width=4)
        self.EntrySpe = Entry(self.FrameStats, width=4)

        self.EntryHp.grid(row=1, column=1, pady=1, sticky='w')
        self.EntryAtk.grid(row=2, column=1, pady=1, sticky='w')
        self.EntryDef.grid(row=3, column=1, pady=1, sticky='w')
        self.EntrySpa.grid(row=4, column=1, pady=1, sticky='w')
        self.EntrySpd.grid(row=5, column=1, pady=1, sticky='w')
        self.EntrySpe.grid(row=6, column=1, pady=1, sticky='w')
        self.teste = 0
        self.EntryBonusAtk = Entry(self.FrameStats, width=4)
        self.EntryBonusAtk.delete(0, END)
        self.EntryBonusAtk.insert(0, '0')
        self.EntryBonusDef = Entry(self.FrameStats, width=4)
        self.EntryBonusDef.delete(0, END)
        self.EntryBonusDef.insert(0, '0')
        self. EntryBonusSpa = Entry(self.FrameStats, width=4)
        self.EntryBonusSpa.delete(0, END)
        self.EntryBonusSpa.insert(0, '0')
        self.EntryBonusSpd = Entry(self.FrameStats, width=4)
        self.EntryBonusSpd.delete(0, END)
        self.EntryBonusSpd.insert(0, '0')
        self.EntryBonusSpe = Entry(self.FrameStats, width=4)
        self.EntryBonusSpe.delete(0, END)
        self.EntryBonusSpe.insert(0, '0')

        self.EntryBonusAtk.grid(row=2, column=2, pady=1, sticky='w')
        self.EntryBonusDef.grid(row=3, column=2, pady=1, sticky='w')
        self.EntryBonusSpa.grid(row=4, column=2, pady=1, sticky='w')
        self.EntryBonusSpd.grid(row=5, column=2, pady=1, sticky='w')
        self.EntryBonusSpe.grid(row=6, column=2, pady=1, sticky='w')

        self.SpinAtk = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinDef = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpa = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpd = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpe = Spinbox(self.FrameStats, from_=0, to=6, width=2)

        self.SpinAtk.grid(row=2, column=3, pady=1, sticky='w')
        self.SpinDef.grid(row=3, column=3, pady=1, sticky='w')
        self.SpinSpa.grid(row=4, column=3, pady=1, sticky='w')
        self.SpinSpd.grid(row=5, column=3, pady=1, sticky='w')
        self.SpinSpe.grid(row=6, column=3, pady=1, sticky='w')
        self.FrameOutros.grid(sticky='w', ipadx=38, padx= 18)
        self.LabelMoves = Label(self.FrameOutros, text="Ataque")
        self.ComboMoves =  AutocompleteCombobox(self.FrameOutros, width=16)
        self.ComboMoves.set_completion_list(MovesLista)
        self.LabelMoves.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.ComboMoves.grid(row=0, column=1, padx=1, pady=1)
        self.label_alvo = Label(self.FrameOutros, text="Alvo")
        self.poke_alvo = AutocompleteCombobox(self.FrameOutros, width=16)
        self.poke_alvo.set_completion_list(self.lista_alvo )
        self.label_alvo.grid(row=1, column=0, padx=1, pady=1, sticky='w')
        self.poke_alvo.grid(row=1, column=1, padx=1, pady=1)


        #POKÉMON DOIS
        self.FrameDados = LabelFrame(self.tab2, text="DADOS")
        self.FrameStats = LabelFrame(self.tab2, text="STATS")
        self.FrameOutros = LabelFrame(self.tab2, text="Outros")
        self.FrameDados.grid(pady=20, ipadx=60, padx=10)

        self.PokémonLabelR1 = ttk.Label(self.FrameDados, text="Pokémon")
        self.SeletorPokémomR1 = AutocompleteCombobox(self.FrameDados, width=16)
        self.SeletorPokémomR1.set_completion_list(ListaNomes)

        self.SeletorPokémomR1.bind('<<ComboboxSelected>>', return_entry_dois)
        self.LabelTypeR1 = Label(self.FrameDados, text="Type")
        self.ComboTypeR1 = ttk.Combobox(self.FrameDados, width=15)
        self.LabelGenderR1 = Label(self.FrameDados, text="Gender")
        self.ComboGenderR1 = ttk.Combobox(self.FrameDados, width=15, values=['Male', 'Female'])
        self.ComboGenderR1.set('Male')
        self.LabelTraitR1 = Label(self.FrameDados, text="Ability")
        self.ComboTraitR1 = ttk.Combobox(self.FrameDados, width=15)
        self.LabelLvR1 = Label(self.FrameDados, text="Level")
        self.SpinLvR1 = Spinbox(self.FrameDados, from_=50, to=100, width=3)

        self.PokémonLabelR1.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.SeletorPokémomR1.grid(row=0, column=1, padx=1, pady=1)
        self.LabelTypeR1.grid(row=1, column=0, padx=1, pady=1, sticky='w')
        self.ComboTypeR1.grid(row=1, column=1, padx=1, pady=1, sticky='w')
        self.LabelGenderR1.grid(row=3, column=0, padx=1, pady=1, sticky='w')
        self.ComboGenderR1.grid(row=3, column=1, padx=1, pady=1, sticky='w')
        self.LabelTraitR1.grid(row=4, column=0, padx=1, pady=1, sticky='w')
        self.ComboTraitR1.grid(row=4, column=1, padx=1, pady=1, sticky='w')
        self.LabelLvR1.grid(row=5, column=0, padx=1, pady=1, sticky='w')
        self.SpinLvR1.grid(row=5, column=1, padx=1, pady=1, sticky='w')

        self.FrameStats.grid(sticky='w', ipadx=65, padx=20)
        self.LabelBaseR1 = Label(self.FrameStats, text="Base")
        self.LabelBrancoR1 = Label(self.FrameStats, text="", width=5)
        self.LabelBonusR1 = Label(self.FrameStats, text="Bônus")
        self.LabelStagesR1 = Label(self.FrameStats, text="Stages")

        self.LabelBrancoR1.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.LabelBaseR1.grid(row=0, column=1, padx=1, pady=1, sticky='w')
        self.LabelBonusR1.grid(row=0, column=2, padx=1, pady=1, sticky='w')
        self.LabelStagesR1.grid(row=0, column=3, padx=1, pady=1, sticky='w')

        status = ['HP', 'Attack', 'Defense', 'Sp.Atk', 'Sp.Def', 'Speed']

        rl = 1
        for c in status:
            Label(self.FrameStats, text=c).grid(row=rl, column=0, padx=1, pady=1, sticky='w')
            rl = rl + 1

        self.EntryHpR1 = Entry(self.FrameStats, width=4)
        self.EntryAtkR1 = Entry(self.FrameStats, width=4)
        self.EntryDefR1 = Entry(self.FrameStats, width=4)
        self.EntrySpaR1 = Entry(self.FrameStats, width=4)
        self.EntrySpdR1 = Entry(self.FrameStats, width=4)
        self.EntrySpeR1 = Entry(self.FrameStats, width=4)

        self.EntryHpR1.grid(row=1, column=1, pady=1, sticky='w')
        self.EntryAtkR1.grid(row=2, column=1, pady=1, sticky='w')
        self.EntryDefR1.grid(row=3, column=1, pady=1, sticky='w')
        self.EntrySpaR1.grid(row=4, column=1, pady=1, sticky='w')
        self.EntrySpdR1.grid(row=5, column=1, pady=1, sticky='w')
        self.EntrySpeR1.grid(row=6, column=1, pady=1, sticky='w')
        self.teste = 0
        self.EntryBonusAtkR1 = Entry(self.FrameStats, width=4)
        self.EntryBonusAtkR1.delete(0, END)
        self.EntryBonusAtkR1.insert(0, '0')
        self.EntryBonusDefR1 = Entry(self.FrameStats, width=4)
        self.EntryBonusDefR1.delete(0, END)
        self.EntryBonusDefR1.insert(0, '0')
        self.EntryBonusSpaR1 = Entry(self.FrameStats, width=4)
        self.EntryBonusSpaR1.delete(0, END)
        self.EntryBonusSpaR1.insert(0, '0')
        self.EntryBonusSpdR1 = Entry(self.FrameStats, width=4)
        self.EntryBonusSpdR1.delete(0, END)
        self.EntryBonusSpdR1.insert(0, '0')
        self.EntryBonusSpeR1 = Entry(self.FrameStats, width=4)
        self.EntryBonusSpeR1.delete(0, END)
        self.EntryBonusSpeR1.insert(0, '0')

        self.EntryBonusAtkR1.grid(row=2, column=2, pady=1, sticky='w')
        self.EntryBonusDefR1.grid(row=3, column=2, pady=1, sticky='w')
        self.EntryBonusSpaR1.grid(row=4, column=2, pady=1, sticky='w')
        self.EntryBonusSpdR1.grid(row=5, column=2, pady=1, sticky='w')
        self.EntryBonusSpeR1.grid(row=6, column=2, pady=1, sticky='w')

        self.SpinAtkR1 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinDefR1 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpaR1 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpdR1 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpeR1 = Spinbox(self.FrameStats, from_=0, to=6, width=2)

        self.SpinAtkR1.grid(row=2, column=3, pady=1, sticky='w')
        self.SpinDefR1.grid(row=3, column=3, pady=1, sticky='w')
        self.SpinSpaR1.grid(row=4, column=3, pady=1, sticky='w')
        self.SpinSpdR1.grid(row=5, column=3, pady=1, sticky='w')
        self.SpinSpeR1.grid(row=6, column=3, pady=1, sticky='w')
        self.FrameOutros.grid(sticky='w', ipadx=38, padx=18)
        self.LabelMovesR1 = Label(self.FrameOutros, text="Ataque")

        self.ComboMovesR1 = AutocompleteCombobox(self.FrameOutros, width=16)
        self.ComboMovesR1.set_completion_list(MovesLista)
        self.LabelMovesR1.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.ComboMovesR1.grid(row=0, column=1, padx=1, pady=1)
        self.label_alvoR1 = Label(self.FrameOutros, text="Alvo")
        self.poke_alvoR1 = AutocompleteCombobox(self.FrameOutros, width=16)
        self.poke_alvoR1.set_completion_list(self.lista_alvo)
        self.label_alvoR1.grid(row=1, column=0, padx=1, pady=1, sticky='w')
        self.poke_alvoR1.grid(row=1, column=1, padx=1, pady=1)

        #POKÉMON TRÊS
        self.FrameDados = LabelFrame(self.tab3, text="DADOS")

        self.FrameStats = LabelFrame(self.tab3, text="STATS")
        self.FrameOutros = LabelFrame(self.tab3, text="Outros")
        self.FrameDados.grid(pady=20, ipadx=60, padx=10)

        self.PokémonLabelR2 = ttk.Label(self.FrameDados, text="Pokémon")
        self.SeletorPokémomR2 = AutocompleteCombobox(self.FrameDados, width=16)
        self.SeletorPokémomR2.set_completion_list(ListaNomes)

        self.SeletorPokémomR2.bind('<<ComboboxSelected>>', return_entry_tres)
        self.LabelTypeR2 = Label(self.FrameDados, text="Type")
        self.ComboTypeR2 = ttk.Combobox(self.FrameDados, width=15)
        self.LabelGenderR2 = Label(self.FrameDados, text="Gender")
        self.ComboGenderR2 = ttk.Combobox(self.FrameDados, width=15, values=['Male', 'Female'])
        self.ComboGenderR2.set('Male')
        self.LabelTraitR2 = Label(self.FrameDados, text="Ability")
        self.ComboTraitR2 = ttk.Combobox(self.FrameDados, width=15)
        self.LabelLvR2 = Label(self.FrameDados, text="Level")
        self.SpinLvR2 = Spinbox(self.FrameDados, from_=50, to=100, width=3)

        self.PokémonLabelR2.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.SeletorPokémomR2.grid(row=0, column=1, padx=1, pady=1)
        self.LabelTypeR2.grid(row=1, column=0, padx=1, pady=1, sticky='w')
        self.ComboTypeR2.grid(row=1, column=1, padx=1, pady=1, sticky='w')
        self.LabelGenderR2.grid(row=3, column=0, padx=1, pady=1, sticky='w')
        self.ComboGenderR2.grid(row=3, column=1, padx=1, pady=1, sticky='w')
        self.LabelTraitR2.grid(row=4, column=0, padx=1, pady=1, sticky='w')
        self.ComboTraitR2.grid(row=4, column=1, padx=1, pady=1, sticky='w')
        self.LabelLvR2.grid(row=5, column=0, padx=1, pady=1, sticky='w')
        self.SpinLvR2.grid(row=5, column=1, padx=1, pady=1, sticky='w')

        self.FrameStats.grid(sticky='w', ipadx=65, padx=20)
        self.LabelBaseR2 = Label(self.FrameStats, text="Base")
        self.LabelBrancoR2 = Label(self.FrameStats, text="", width=5)
        self.LabelBonusR2 = Label(self.FrameStats, text="Bônus")
        self.LabelStagesR2 = Label(self.FrameStats, text="Stages")

        self.LabelBrancoR2.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.LabelBaseR2.grid(row=0, column=1, padx=1, pady=1, sticky='w')
        self.LabelBonusR2.grid(row=0, column=2, padx=1, pady=1, sticky='w')
        self.LabelStagesR2.grid(row=0, column=3, padx=1, pady=1, sticky='w')

        status = ['HP', 'Attack', 'Defense', 'Sp.Atk', 'Sp.Def', 'Speed']

        rl = 1
        for c in status:
            Label(self.FrameStats, text=c).grid(row=rl, column=0, padx=1, pady=1, sticky='w')
            rl = rl + 1

        self.EntryHpR2 = Entry(self.FrameStats, width=4)
        self.EntryAtkR2 = Entry(self.FrameStats, width=4)
        self.EntryDefR2 = Entry(self.FrameStats, width=4)
        self.EntrySpaR2 = Entry(self.FrameStats, width=4)
        self.EntrySpdR2 = Entry(self.FrameStats, width=4)
        self.EntrySpeR2 = Entry(self.FrameStats, width=4)

        self.EntryHpR2.grid(row=1, column=1, pady=1, sticky='w')
        self.EntryAtkR2.grid(row=2, column=1, pady=1, sticky='w')
        self.EntryDefR2.grid(row=3, column=1, pady=1, sticky='w')
        self.EntrySpaR2.grid(row=4, column=1, pady=1, sticky='w')
        self.EntrySpdR2.grid(row=5, column=1, pady=1, sticky='w')
        self.EntrySpeR2.grid(row=6, column=1, pady=1, sticky='w')
        self.teste = 0
        self.EntryBonusAtkR2 = Entry(self.FrameStats, width=4)
        self.EntryBonusAtkR2.delete(0, END)
        self.EntryBonusAtkR2.insert(0, '0')
        self.EntryBonusDefR2 = Entry(self.FrameStats, width=4)
        self.EntryBonusDefR2.delete(0, END)
        self.EntryBonusDefR2.insert(0, '0')
        self.EntryBonusSpaR2 = Entry(self.FrameStats, width=4)
        self.EntryBonusSpaR2.delete(0, END)
        self.EntryBonusSpaR2.insert(0, '0')
        self.EntryBonusSpdR2 = Entry(self.FrameStats, width=4)
        self.EntryBonusSpdR2.delete(0, END)
        self.EntryBonusSpdR2.insert(0, '0')
        self.EntryBonusSpeR2 = Entry(self.FrameStats, width=4)
        self.EntryBonusSpeR2.delete(0, END)
        self.EntryBonusSpeR2.insert(0, '0')

        self.EntryBonusAtkR2.grid(row=2, column=2, pady=1, sticky='w')
        self.EntryBonusDefR2.grid(row=3, column=2, pady=1, sticky='w')
        self.EntryBonusSpaR2.grid(row=4, column=2, pady=1, sticky='w')
        self.EntryBonusSpdR2.grid(row=5, column=2, pady=1, sticky='w')
        self.EntryBonusSpeR2.grid(row=6, column=2, pady=1, sticky='w')

        self.SpinAtkR2 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinDefR2 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpaR2 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpdR2 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpeR2 = Spinbox(self.FrameStats, from_=0, to=6, width=2)

        self.SpinAtkR2.grid(row=2, column=3, pady=1, sticky='w')
        self.SpinDefR2.grid(row=3, column=3, pady=1, sticky='w')
        self.SpinSpaR2.grid(row=4, column=3, pady=1, sticky='w')
        self.SpinSpdR2.grid(row=5, column=3, pady=1, sticky='w')
        self.SpinSpeR2.grid(row=6, column=3, pady=1, sticky='w')
        self.FrameOutros.grid(sticky='w', ipadx=38, padx=18)
        self.LabelMovesR2 = Label(self.FrameOutros, text="Ataque")

        self.ComboMovesR2 = AutocompleteCombobox(self.FrameOutros, width=16)
        self.ComboMovesR2.set_completion_list(MovesLista)
        self.LabelMovesR2.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.ComboMovesR2.grid(row=0, column=1, padx=1, pady=1)
        self.label_alvoR2 = Label(self.FrameOutros, text="Alvo")
        self.poke_alvoR2 = AutocompleteCombobox(self.FrameOutros, width=16)
        self.poke_alvoR2.set_completion_list(self.lista_alvo)
        self.label_alvoR2.grid(row=1, column=0, padx=1, pady=1, sticky='w')
        self.poke_alvoR2.grid(row=1, column=1, padx=1, pady=1)


    #INICIO FIELD
        self.Field.grid(row=0, column=1, ipadx=100, ipady=210)

        #INICIO JOGADOR DOIS
        self.note = ttk.Notebook(self.FrameLeft)
        self.tab1 = ttk.Frame(self.note)
        self.tab2 = ttk.Frame(self.note)
        self.tab3 = ttk.Frame(self.note)
        self.note.add(self.tab1, text="Pokémon 1", compound=TOP)
        self.note.add(self.tab2, text="Pokémon 2")
        self.note.add(self.tab3, text="Pokémon 3")
        self.FrameLeft.grid(row=0, column=3, pady=10, padx=10)
        self.note.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW', pady=20, padx=20)
        self.FrameDados = LabelFrame(self.tab1, text="DADOS")
        self.FrameStats = LabelFrame(self.tab1, text="STATS")
        self.FrameOutros = LabelFrame(self.tab1, text="Outros")
        self.FrameDados.grid(pady=10, ipadx=20, padx=10)
        self.PokémonLabelL1 = ttk.Label(self.FrameDados, text="Pokémon")


        self.SeletorPokémomL1 = AutocompleteCombobox(self.FrameDados, width=16)
        self.SeletorPokémomL1.set_completion_list(ListaNomes)
        self.SeletorPokémomL1.bind('<<ComboboxSelected>>', retorno)
        self.LabelTypeL1 = Label(self.FrameDados, text="Type")
        self.ComboTypeL1 = ttk.Combobox(self.FrameDados, width=15)
        self.LabelGenderL1 = Label(self.FrameDados, text="Gender")
        self.ComboGenderL1 = ttk.Combobox(self.FrameDados, width=15, values=['Male', 'Female'])
        self.ComboGenderL1.set('Male')
        self.LabelTraitL1 = Label(self.FrameDados, text="Ability")
        self.ComboTraitL1 = ttk.Combobox(self.FrameDados, width=15)
        self.LabelLvL1 = Label(self.FrameDados, text="Level")
        self.SpinLvL1 = Spinbox(self.FrameDados, from_=1, to=100, width=3)

        self.PokémonLabelL1.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.SeletorPokémomL1.grid(row=0, column=1, padx=1, pady=1)
        self.LabelTypeL1.grid(row=1, column=0, padx=1, pady=1, sticky='w')
        self.ComboTypeL1.grid(row=1, column=1, padx=1, pady=1, sticky='w')
        self.LabelGenderL1.grid(row=3, column=0, padx=1, pady=1, sticky='w')
        self.ComboGenderL1.grid(row=3, column=1, padx=1, pady=1, sticky='w')
        self.LabelTraitL1.grid(row=4, column=0, padx=1, pady=1, sticky='w')
        self.ComboTraitL1.grid(row=4, column=1, padx=1, pady=1, sticky='w')
        self.LabelLvL1.grid(row=5, column=0, padx=1, pady=1, sticky='w')
        self.SpinLvL1.grid(row=5, column=1, padx=1, pady=1, sticky='w')

        self.FrameStats.grid(sticky='w', ipadx=24, padx=20)
        self.LabelBaseL1 = Label(self.FrameStats, text="Base")
        self.LabelBrancoL1 = Label(self.FrameStats, text="", width=5)
        self.LabelBonusL1 = Label(self.FrameStats, text="Bônus")
        self.LabelStagesL1 = Label(self.FrameStats, text="Stages")

        self.LabelBrancoL1.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.LabelBaseL1.grid(row=0, column=1, padx=1, pady=1, sticky='w')
        self.LabelBonusL1.grid(row=0, column=2, padx=1, pady=1, sticky='w')
        self.LabelStagesL1.grid(row=0, column=3, padx=1, pady=1, sticky='w')

        status = ['HP', 'Attack', 'Defense', 'Sp.Atk', 'Sp.Def', 'Speed']

        rl = 1
        for c in status:
            Label(self.FrameStats, text=c).grid(row=rl, column=0, padx=1, pady=1, sticky='w')
            rl = rl + 1

        self.EntryHpL1 = Entry(self.FrameStats, width=4)
        self.EntryAtkL1 = Entry(self.FrameStats, width=4)
        self.EntryDefL1 = Entry(self.FrameStats, width=4)
        self.EntrySpaL1 = Entry(self.FrameStats, width=4)
        self.EntrySpdL1 = Entry(self.FrameStats, width=4)
        self.EntrySpeL1 = Entry(self.FrameStats, width=4)

        self.EntryHpL1.grid(row=1, column=1, pady=1, sticky='w')
        self.EntryAtkL1.grid(row=2, column=1, pady=1, sticky='w')
        self.EntryDefL1.grid(row=3, column=1, pady=1, sticky='w')
        self.EntrySpaL1.grid(row=4, column=1, pady=1, sticky='w')
        self.EntrySpdL1.grid(row=5, column=1, pady=1, sticky='w')
        self.EntrySpeL1.grid(row=6, column=1, pady=1, sticky='w')

        self.EntryBonusAtkL1 = Entry(self.FrameStats, width=4)
        self.EntryBonusAtkL1.delete(0, END)
        self.EntryBonusAtkL1.insert(0, '0')
        self.EntryBonusDefL1 = Entry(self.FrameStats, width=4)
        self.EntryBonusDefL1.delete(0, END)
        self.EntryBonusDefL1.insert(0, '0')
        self.EntryBonusSpaL1 = Entry(self.FrameStats, width=4)
        self.EntryBonusSpaL1.delete(0, END)
        self.EntryBonusSpaL1.insert(0, '0')
        self.EntryBonusSpdL1 = Entry(self.FrameStats, width=4)
        self.EntryBonusSpdL1.delete(0, END)
        self.EntryBonusSpdL1.insert(0, '0')
        self.EntryBonusSpeL1 = Entry(self.FrameStats, width=4)
        self.EntryBonusSpeL1.delete(0, END)
        self.EntryBonusSpeL1.insert(0, '0')

        self.EntryBonusAtkL1.grid(row=2, column=2, pady=1, sticky='w')
        self.EntryBonusDefL1.grid(row=3, column=2, pady=1, sticky='w')
        self.EntryBonusSpaL1.grid(row=4, column=2, pady=1, sticky='w')
        self.EntryBonusSpdL1.grid(row=5, column=2, pady=1, sticky='w')
        self.EntryBonusSpeL1.grid(row=6, column=2, pady=1, sticky='w')

        self.SpinAtkL1 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinDefL1 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpaL1 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpdL1 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpeL1 = Spinbox(self.FrameStats, from_=0, to=6, width=2)

        self.SpinAtkL1.grid(row=2, column=3, pady=1, sticky='w')
        self.SpinDefL1.grid(row=3, column=3, pady=1, sticky='w')
        self.SpinSpaL1.grid(row=4, column=3, pady=1, sticky='w')
        self.SpinSpdL1.grid(row=5, column=3, pady=1, sticky='w')
        self.SpinSpeL1.grid(row=6, column=3, pady=1, sticky='w')

        self.FrameOutros.grid(sticky='w', ipadx=38, padx=18)
        self.LabelMovesL1 = Label(self.FrameOutros, text="Ataque")
        self.ComboMovesL1 = AutocompleteCombobox(self.FrameOutros, width=16)
        self.ComboMovesL1.set_completion_list(MovesLista)
        self.LabelMovesL1.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.ComboMovesL1.grid(row=0, column=1, padx=1, pady=1)
        self.label_alvoL1 = Label(self.FrameOutros, text="Alvo")
        self.poke_alvoL1 = AutocompleteCombobox(self.FrameOutros, width=16)
        self.poke_alvoL1.set_completion_list(self.lista_alvo)
        self.label_alvoL1.grid(row=1, column=0, padx=1, pady=1, sticky='w')
        self.poke_alvoL1.grid(row=1, column=1, padx=1, pady=1)


        self.FrameDados = LabelFrame(self.tab2, text="DADOS")

        self.FrameStats = LabelFrame(self.tab2, text="STATS")
        self.FrameOutros = LabelFrame(self.tab2, text="Outros")
        self.FrameDados.grid(pady=10, ipadx=20, padx=10)
        self.PokémonLabelL2 = ttk.Label(self.FrameDados, text="Pokémon")

        self.SeletorPokémomL2 = AutocompleteCombobox(self.FrameDados, width=16)
        self.SeletorPokémomL2.set_completion_list(ListaNomes)
        self.SeletorPokémomL2.bind('<<ComboboxSelected>>', retorno_dois)
        self.LabelTypeL2 = Label(self.FrameDados, text="Type")
        self.ComboTypeL2 = ttk.Combobox(self.FrameDados, width=15)
        self.LabelGenderL2 = Label(self.FrameDados, text="Gender")
        self.ComboGenderL2 = ttk.Combobox(self.FrameDados, width=15, values=['Male', 'Female'])
        self.ComboGenderL2.set('Male')
        self.LabelTraitL2 = Label(self.FrameDados, text="Ability")
        self.ComboTraitL2 = ttk.Combobox(self.FrameDados, width=15)
        self.LabelLvL2 = Label(self.FrameDados, text="Level")
        self.SpinLvL2 = Spinbox(self.FrameDados, from_=1, to=100, width=3)

        self.PokémonLabelL2.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.SeletorPokémomL2.grid(row=0, column=1, padx=1, pady=1)
        self.LabelTypeL2.grid(row=1, column=0, padx=1, pady=1, sticky='w')
        self.ComboTypeL2.grid(row=1, column=1, padx=1, pady=1, sticky='w')
        self.LabelGenderL2.grid(row=3, column=0, padx=1, pady=1, sticky='w')
        self.ComboGenderL2.grid(row=3, column=1, padx=1, pady=1, sticky='w')
        self.LabelTraitL2.grid(row=4, column=0, padx=1, pady=1, sticky='w')
        self.ComboTraitL2.grid(row=4, column=1, padx=1, pady=1, sticky='w')
        self.LabelLvL2.grid(row=5, column=0, padx=1, pady=1, sticky='w')
        self.SpinLvL2.grid(row=5, column=1, padx=1, pady=1, sticky='w')

        self.FrameStats.grid(sticky='w', ipadx=24, padx=20)
        self.LabelBaseL2 = Label(self.FrameStats, text="Base")
        self.LabelBrancoL2 = Label(self.FrameStats, text="", width=5)
        self.LabelBonusL2 = Label(self.FrameStats, text="Bônus")
        self.LabelStagesL2 = Label(self.FrameStats, text="Stages")

        self.LabelBrancoL2.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.LabelBaseL2.grid(row=0, column=1, padx=1, pady=1, sticky='w')
        self.LabelBonusL2.grid(row=0, column=2, padx=1, pady=1, sticky='w')
        self.LabelStagesL2.grid(row=0, column=3, padx=1, pady=1, sticky='w')

        status = ['HP', 'Attack', 'Defense', 'Sp.Atk', 'Sp.Def', 'Speed']

        rl = 1
        for c in status:
            Label(self.FrameStats, text=c).grid(row=rl, column=0, padx=1, pady=1, sticky='w')
            rl = rl + 1

        self.EntryHpL2 = Entry(self.FrameStats, width=4)
        self.EntryAtkL2 = Entry(self.FrameStats, width=4)
        self.EntryDefL2 = Entry(self.FrameStats, width=4)
        self.EntrySpaL2 = Entry(self.FrameStats, width=4)
        self.EntrySpdL2 = Entry(self.FrameStats, width=4)
        self.EntrySpeL2 = Entry(self.FrameStats, width=4)

        self.EntryHpL2.grid(row=1, column=1, pady=1, sticky='w')
        self.EntryAtkL2.grid(row=2, column=1, pady=1, sticky='w')
        self.EntryDefL2.grid(row=3, column=1, pady=1, sticky='w')
        self.EntrySpaL2.grid(row=4, column=1, pady=1, sticky='w')
        self.EntrySpdL2.grid(row=5, column=1, pady=1, sticky='w')
        self.EntrySpeL2.grid(row=6, column=1, pady=1, sticky='w')

        self.EntryBonusAtkL2 = Entry(self.FrameStats, width=4)
        self.EntryBonusAtkL2.delete(0, END)
        self.EntryBonusAtkL2.insert(0, '0')
        self.EntryBonusDefL2 = Entry(self.FrameStats, width=4)
        self.EntryBonusDefL2.delete(0, END)
        self.EntryBonusDefL2.insert(0, '0')
        self.EntryBonusSpaL2 = Entry(self.FrameStats, width=4)
        self.EntryBonusSpaL2.delete(0, END)
        self.EntryBonusSpaL2.insert(0, '0')
        self.EntryBonusSpdL2 = Entry(self.FrameStats, width=4)
        self.EntryBonusSpdL2.delete(0, END)
        self.EntryBonusSpdL2.insert(0, '0')
        self.EntryBonusSpeL2 = Entry(self.FrameStats, width=4)
        self.EntryBonusSpeL2.delete(0, END)
        self.EntryBonusSpeL2.insert(0, '0')

        self.EntryBonusAtkL2.grid(row=2, column=2, pady=1, sticky='w')
        self.EntryBonusDefL2.grid(row=3, column=2, pady=1, sticky='w')
        self.EntryBonusSpaL2.grid(row=4, column=2, pady=1, sticky='w')
        self.EntryBonusSpdL2.grid(row=5, column=2, pady=1, sticky='w')
        self.EntryBonusSpeL2.grid(row=6, column=2, pady=1, sticky='w')

        self.SpinAtkL2 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinDefL2 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpaL2 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpdL2 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpeL2 = Spinbox(self.FrameStats, from_=0, to=6, width=2)

        self.SpinAtkL2.grid(row=2, column=3, pady=1, sticky='w')
        self.SpinDefL2.grid(row=3, column=3, pady=1, sticky='w')
        self.SpinSpaL2.grid(row=4, column=3, pady=1, sticky='w')
        self.SpinSpdL2.grid(row=5, column=3, pady=1, sticky='w')
        self.SpinSpeL2.grid(row=6, column=3, pady=1, sticky='w')

        self.FrameOutros.grid(sticky='w', ipadx=38, padx=18)
        self.LabelMovesL2 = Label(self.FrameOutros, text="Ataque")
        self.ComboMovesL2 = AutocompleteCombobox(self.FrameOutros, width=16)
        self.ComboMovesL2.set_completion_list(MovesLista)
        self.LabelMovesL2.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.ComboMovesL2.grid(row=0, column=1, padx=1, pady=1)
        self.label_alvoL2 = Label(self.FrameOutros, text="Alvo")
        self.poke_alvoL2 = AutocompleteCombobox(self.FrameOutros, width=16)
        self.poke_alvoL2.set_completion_list(self.lista_alvo)
        self.label_alvoL2.grid(row=1, column=0, padx=1, pady=1, sticky='w')
        self.poke_alvoL2.grid(row=1, column=1, padx=1, pady=1)


        #POKEMON TRÊS
        self.FrameDados = LabelFrame(self.tab3, text="DADOS")
        self.FrameStats = LabelFrame(self.tab3, text="STATS")
        self.FrameOutros = LabelFrame(self.tab3, text="Outros")
        self.FrameDados.grid(pady=10, ipadx=20, padx=10)
        self.PokémonLabelL3 = ttk.Label(self.FrameDados, text="Pokémon")

        self.SeletorPokémomL3 = AutocompleteCombobox(self.FrameDados, width=16)
        self.SeletorPokémomL3.set_completion_list(ListaNomes)
        self.SeletorPokémomL3.bind('<<ComboboxSelected>>', retorno_tres)
        self.LabelTypeL3 = Label(self.FrameDados, text="Type")
        self.ComboTypeL3 = ttk.Combobox(self.FrameDados, width=15)
        self.LabelGenderL3 = Label(self.FrameDados, text="Gender")
        self.ComboGenderL3 = ttk.Combobox(self.FrameDados, width=15, values=['Male', 'Female'])
        self.ComboGenderL3.set('Male')
        self.LabelTraitL3 = Label(self.FrameDados, text="Ability")
        self.ComboTraitL3 = ttk.Combobox(self.FrameDados, width=15)
        self.LabelLvL3 = Label(self.FrameDados, text="Level")
        self.SpinLvL3 = Spinbox(self.FrameDados, from_=1, to=100, width=3)

        self.PokémonLabelL3.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.SeletorPokémomL3.grid(row=0, column=1, padx=1, pady=1)
        self.LabelTypeL3.grid(row=1, column=0, padx=1, pady=1, sticky='w')
        self.ComboTypeL3.grid(row=1, column=1, padx=1, pady=1, sticky='w')
        self.LabelGenderL3.grid(row=3, column=0, padx=1, pady=1, sticky='w')
        self.ComboGenderL3.grid(row=3, column=1, padx=1, pady=1, sticky='w')
        self.LabelTraitL3.grid(row=4, column=0, padx=1, pady=1, sticky='w')
        self.ComboTraitL3.grid(row=4, column=1, padx=1, pady=1, sticky='w')
        self.LabelLvL3.grid(row=5, column=0, padx=1, pady=1, sticky='w')
        self.SpinLvL3.grid(row=5, column=1, padx=1, pady=1, sticky='w')

        self.FrameStats.grid(sticky='w', ipadx=24, padx=20)
        self.LabelBaseL3 = Label(self.FrameStats, text="Base")
        self.LabelBrancoL3 = Label(self.FrameStats, text="", width=5)
        self.LabelBonusL3 = Label(self.FrameStats, text="Bônus")
        self.LabelStagesL3 = Label(self.FrameStats, text="Stages")

        self.LabelBrancoL3.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.LabelBaseL3.grid(row=0, column=1, padx=1, pady=1, sticky='w')
        self.LabelBonusL3.grid(row=0, column=2, padx=1, pady=1, sticky='w')
        self.LabelStagesL3.grid(row=0, column=3, padx=1, pady=1, sticky='w')

        status = ['HP', 'Attack', 'Defense', 'Sp.Atk', 'Sp.Def', 'Speed']

        rl = 1
        for c in status:
            Label(self.FrameStats, text=c).grid(row=rl, column=0, padx=1, pady=1, sticky='w')
            rl = rl + 1

        self.EntryHpL3 = Entry(self.FrameStats, width=4)
        self.EntryAtkL3 = Entry(self.FrameStats, width=4)
        self.EntryDefL3 = Entry(self.FrameStats, width=4)
        self.EntrySpaL3 = Entry(self.FrameStats, width=4)
        self.EntrySpdL3 = Entry(self.FrameStats, width=4)
        self.EntrySpeL3 = Entry(self.FrameStats, width=4)

        self.EntryHpL3.grid(row=1, column=1, pady=1, sticky='w')
        self.EntryAtkL3.grid(row=2, column=1, pady=1, sticky='w')
        self.EntryDefL3.grid(row=3, column=1, pady=1, sticky='w')
        self.EntrySpaL3.grid(row=4, column=1, pady=1, sticky='w')
        self.EntrySpdL3.grid(row=5, column=1, pady=1, sticky='w')
        self.EntrySpeL3.grid(row=6, column=1, pady=1, sticky='w')

        self.EntryBonusAtkL3 = Entry(self.FrameStats, width=4)
        self.EntryBonusAtkL3.delete(0, END)
        self.EntryBonusAtkL3.insert(0, '0')
        self.EntryBonusDefL3 = Entry(self.FrameStats, width=4)
        self.EntryBonusDefL3.delete(0, END)
        self.EntryBonusDefL3.insert(0, '0')
        self.EntryBonusSpaL3 = Entry(self.FrameStats, width=4)
        self.EntryBonusSpaL3.delete(0, END)
        self.EntryBonusSpaL3.insert(0, '0')
        self.EntryBonusSpdL3 = Entry(self.FrameStats, width=4)
        self.EntryBonusSpdL3.delete(0, END)
        self.EntryBonusSpdL3.insert(0, '0')
        self.EntryBonusSpeL3 = Entry(self.FrameStats, width=4)
        self.EntryBonusSpeL3.delete(0, END)
        self.EntryBonusSpeL3.insert(0, '0')

        self.EntryBonusAtkL3.grid(row=2, column=2, pady=1, sticky='w')
        self.EntryBonusDefL3.grid(row=3, column=2, pady=1, sticky='w')
        self.EntryBonusSpaL3.grid(row=4, column=2, pady=1, sticky='w')
        self.EntryBonusSpdL3.grid(row=5, column=2, pady=1, sticky='w')
        self.EntryBonusSpeL3.grid(row=6, column=2, pady=1, sticky='w')

        self.SpinAtkL3 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinDefL3 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpaL3 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpdL3 = Spinbox(self.FrameStats, from_=0, to=6, width=2)
        self.SpinSpeL3 = Spinbox(self.FrameStats, from_=0, to=6, width=2)

        self.SpinAtkL3.grid(row=2, column=3, pady=1, sticky='w')
        self.SpinDefL3.grid(row=3, column=3, pady=1, sticky='w')
        self.SpinSpaL3.grid(row=4, column=3, pady=1, sticky='w')
        self.SpinSpdL3.grid(row=5, column=3, pady=1, sticky='w')
        self.SpinSpeL3.grid(row=6, column=3, pady=1, sticky='w')

        self.FrameOutros.grid(sticky='w', ipadx=38, padx=18)
        self.LabelMovesL3 = Label(self.FrameOutros, text="Ataque")
        self.ComboMovesL3 = AutocompleteCombobox(self.FrameOutros, width=16)
        self.ComboMovesL3.set_completion_list(MovesLista)
        self.LabelMovesL3.grid(row=0, column=0, padx=1, pady=1, sticky='w')
        self.ComboMovesL3.grid(row=0, column=1, padx=1, pady=1)
        self.label_alvoL3 = Label(self.FrameOutros, text="Alvo")
        self.poke_alvoL3 = AutocompleteCombobox(self.FrameOutros, width=16)
        self.poke_alvoL3.set_completion_list(self.lista_alvo)
        self.label_alvoL3.grid(row=1, column=0, padx=1, pady=1, sticky='w')
        self.poke_alvoL3.grid(row=1, column=1, padx=1, pady=1)


        self.resultado.grid(row=1, column=0, ipadx=20, ipady=10, padx = 20, pady= 20, columnspan =4, sticky= SW)
        self.Calcular = Button(self.resultado, text="Iniciar Batalha", command=iniciar_batalha)
        self.Calcular.grid(row=0, column=0, padx=1, pady=1)
        self.turno = Button(self.resultado, text="Prox Turno", command = prox_turno)
        self.turno.grid(row=1, column=0, padx=1, pady=1)
        self.resultado_texto = ScrolledText(self.resultado, width=110, height=10 )

        self.resultado_texto.grid(row=2, column=0, padx=1, pady=1, ipadx = 5)

root = Tk()
b = CalculadoraDano(root)
root.mainloop()