# Display window
# - Create main display window
# - moving tiles into their own class
# - create time/date bar?
# - room class
# - get data from file to set up many tiles
    

import tkinter
import sys
import xml.etree.ElementTree
from tiles import tile
from tiles import event_tile


# Display Window
class Disp_Dialog:

    def __init__(self, parent):
        print("init dialog class")
        self.parent = parent

        #DEBUG/FULLSCREEN MODE:
        self.fullscreen = False
        
        if self.fullscreen:
            self.parent.attributes('-fullscreen', True)
        else:
            self.parent.geometry("1200x800")
            
        self.set_escapes()   # function to set up safe exit commands
        
        # get datafile
        ##self.datafile = self.get_datafile()
        
        self.no_of_tiles = 10   # Number of tiles

        self.load_tiles()

        # Display tiles:
        ##print("creating tile object")
        ##self.tile = event_tile(self.parent, self.no_of_tiles, self.datafile)    

    # End of Class initialisation
    
#   ----- Class methods ---------------

    def load_tiles(self):
        # Parse in Datafile:
        
        
        #until end of datafile:
        # find tile symbol
        # determin tile type
        # create tile object of that type (pass datafile)
        #  in the tile class it will extract the rest of the data
        # check for end of file
        # loop for next tile type
        #tiles loaded
        pass

    def get_datafile(self):
        try:
            datafile = open('data_file.txt', 'r')
        except:
            print("Datafile not present")
            self.datafile = False               # Give self.datafile a vlaue to test on safe_exit()
            self.safe_exit()                    # Exit the program - no file to load

        return datafile


    #safety button to exit fullscreen display
    def set_escapes(self):
        self.b = tkinter.Button(self.parent, text="Button", command=self.safe_exit)
        self.b.place(width=50, height=20, x=0,y=0)
        #Bind keyboard for safe exit:
        self.parent.bind("<Control-backslash>", self.get_exit) # bind keyboard to detect exit command
        return

    # Safe method to exit program:
    def safe_exit(self):
        print("Exiting")
        if self.datafile:               # Check if datafile is used
            self.datafile.close()       # Close the file
        self.parent.destroy()           # Destroy the GUI
        sys.exit()                      # Terminate the program
        


    # Exit the program on Keypress
    def get_exit(self, event):
        print("keypress exit")
        self.safe_exit()
        


root = tkinter.Tk()
main = Disp_Dialog(root)
root.mainloop()
