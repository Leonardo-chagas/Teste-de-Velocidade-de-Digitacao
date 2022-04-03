from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import Clock
import random


class Teste(Screen):
    textos = ['Esse texto existe somente para a realização do teste de velocidade de digitação, e nada mais.',
    'João Pedro estava andando pela rua, quando de repente, ele tropeçou em uma pedra e se machucou.',
    'A velocidade de digitação mais rápida foi definida por Stella Pajunas, em 1946 com 216 palavras por minuto.']

    def __init__(self, **kw):
        super().__init__(**kw)
        self.texto = ' '.join(random.sample(self.textos, 3))
        #print(self.texto)
        self.start = False
        self.index = 0
        self.palavras = self.texto.split(' ')
        #self.ids.texto.text = self.texto
    
    def UpdateTime(self, *args):
        self.ids.timer.text = str(int(self.ids.timer.text)-1)

    def CompareText(self):
        if self.palavras[self.index] == self.ids.usertexto.text:
            self.palavras[self.index] = '[color=#56b035]' + self.palavras[self.index] + '[/color]'
        else:
            self.palavras[self.index] = '[color=#b03535]' + self.palavras[self.index] + '[/color]'
        self.ids.usertexto.text = ''
        self.index += 1

    def Type(self):
        if self.start == False:
            Clock.schedule_interval(self.UpdateTime, 1)
            self.start = True
        if self.ids.usertexto.text.find(' ') != -1:
            self.CompareText()


""" class TextoTeste(TextInput, Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) """