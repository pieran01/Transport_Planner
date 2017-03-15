# conversion of named colours into RGB values
import tkinter
class Colours():

    def __init__(self):
        self.c = {}
        self.c['red'] = "#fff000000"
        self.c['green'] = "#000fff000"
        self.c['blue'] = "#000000fff"


    def convert(self, colour):
        out = self.c[colour]
        return out


    def test(self, colour):
        top = tkinter.Tk()
        top.configure(background = self.convert(colour))
        top.mainloop()

