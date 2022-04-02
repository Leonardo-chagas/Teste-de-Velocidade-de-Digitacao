from turtle import Screen
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from teste import Teste
from botoes import *


class Menu(Screen):
    pass

class Gerenciador(ScreenManager):
    pass

class Aplicativo(App):
    def build(self):
        #kv = Builder.load_file('aplicativo.kv')
        return Gerenciador()

Aplicativo().run()