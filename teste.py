from kivy.uix.screenmanager import Screen
from kivy.clock import Clock


class Teste(Screen):
    textos = []

    def __init__(self, **kw):
        super().__init__(**kw)
        self.texto = ''
        self.start = False
    
    def UpdateTime(self, *args):
        self.ids.timer.text = str(int(self.ids.timer.text)-1)

    def Type(self):
        if self.start == False:
            Clock.schedule_interval(self.UpdateTime, 1)
            self.start = True
        print(self.ids.usertexto.text[-1])