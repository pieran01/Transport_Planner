# Display window
# - Create main display window
# - begin designing tiles
    

import tkinter
#from tkinter import font


# Display Window
class Disp_Dialog:



    def __init__(self, parent):

        self.parent = parent
        self.parent.geometry("800x200")
        #self.parent.attributes('-fullscreen', True)

        self.no_of_tiles = 10   # Number of tiles

        # Tiles (move to own class later)
        self.scr_w = self.parent.winfo_screenwidth()
        self.scr_h = self.parent.winfo_screenheight()
        
        self.frame_width = self.scr_w/(self.no_of_tiles/2)
        self.frame_height = self.scr_h/2

        self.tile = tkinter.Frame(self.parent, bg="white")
        self.tile.place(width=self.frame_width, heigh=self.frame_height, x=20, y=20)

        self.event_title = tkinter.StringVar()
        self.event_title.set("TEST")
        self.font_title = tkinter.font.Font(size=18)
        self.l_event_title = tkinter.Label(self.tile, textvariable=self.event_title,
                                           bg="white", font=self.font_title)
        self.l_event_title.place(x=self.frame_width/2, y=0, anchor="n")

        self.event_colour="#0ff000fff"
        self.l_event_colour = tkinter.Label(self.tile, bg=self.event_colour)
        self.l_event_colour.place(anchor="n", x=self.frame_width/2, y=50,
                                  width=self.frame_width-50, height=50)
        



        #Safety button to exit fullscreen
        self.b = tkinter.Button(self.parent, text="Button", command=self.b)
        self.b.place(width=50, height=20,
                     x=self.parent.winfo_screenwidth()-50,
                     y=self.parent.winfo_screenheight()-20)

        #detect key press for exit
        self.parent.bind("<Control-backslash>", self.get_exit)

    #safety button to exit fullscreen display
    def b(self):
        print("Exiting")
        self.parent.destroy()


    # Exit the program
    def get_exit(self, event):
        print("keypress exit")
        self.parent.destroy()
        


root = tkinter.Tk()
main = Disp_Dialog(root)
root.mainloop()
