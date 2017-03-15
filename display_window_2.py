# Display window
# - Create main display window
# - moving tiles into their own class
# - create time/date bar?
# - add scroll bars if not full screen
# - get data from file to set up many tiles
    

import tkinter
from tiles import tile
from tiles import event_tile


# Display Window
class Disp_Dialog:



    def __init__(self, parent):
        print("init dialog class")
        self.parent = parent
        self.parent.geometry("800x200")
        #self.parent.attributes('-fullscreen', True)

        self.set_escapes()   # function to set up safe exit commands
        

        self.no_of_tiles = 10   # Number of tiles

        # Display tiles:
        print("creating tile object")
        self.tile = event_tile(self.parent, self.no_of_tiles)    





    #safety button to exit fullscreen display
    def set_escapes(self):
        self.b = tkinter.Button(self.parent, text="Button", command=self.b)
        self.b.place(width=50, height=20,
                     x=self.parent.winfo_screenwidth()-50,
                     y=self.parent.winfo_screenheight()-20)
        #Bind keyboard for safe exit:
        self.parent.bind("<Control-backslash>", self.get_exit)
        return

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
