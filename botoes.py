from logging import root
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty

class Input(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)