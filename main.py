from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Gerenciador():
    pass

class Aplicativo(App):
    def build(self):
        #kv = Builder.load_file('aplicativo.kv')
        return Gerenciador()

Aplicativo().run()