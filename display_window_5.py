# Display window

#v4 removes old 'datafile' and replaces it with xml file
#   datafile name is still used for the xml fiel
#   but txt file related datafile stuff has been removed

#v5 is making display_window place the tiles
#   In v4, the tiles class has been set up to place the tiles
#   tiles class will be amended so that .place is called by
#   display_window.
#
#   TO DO:
#       - Fix the spacing issue between tiles.
#       - Test number of tiles for range placing


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

        self.scr_w = self.parent.winfo_screenwidth()
        self.scr_h = self.parent.winfo_screenheight()

        self.parent.configure(bg='#000000300')
        
        self.set_escapes()   # function to set up safe exit commands
        
        # get datafile
        ##self.datafile = self.get_datafile()
        

        self.no_of_tiles = 10   # Number of tiles to diplay on screen
        self.tiles = []         # List to hold all the tile objects
        self.load_tiles()       # Load in the datafile and create tiles

        # Display tiles:
        self.place_tiles()    

    # End of Class initialisation
    
#   ----- Class methods ---------------

    def place_tiles(self):

        #Only draw the number of tiles available
        # up to a maximum of 6.
        if (len(self.tiles)<6):
            r = len(self.tiles)
        else:
            r = 6
        
        for i in range(0, r):
            # 'i' is the index of the tile - its tile number in the list

            # Set x position for tile:
            x_pos = 5+(5*i) + (self.scr_w/(self.no_of_tiles/2))*i

            # Set y position for tile:
            if(i > (self.no_of_tiles/2)):
                y_pos = 5+ self.scr_h/2
            else:
                y_pos = 5

            # Place the tile:
            self.tiles[i].Tile.place(x=x_pos, y=y_pos)
            
        return

    def load_tiles(self):
        # Parse in Datafile:
        datafile = xml.etree.ElementTree.parse('data_file_xml3.xml')

        
        for tile in datafile.findall('tile'):   # find every tile in the datafile
            tile_type = tile.get('type')        # get the tile's type
            if (tile_type == "event"):
                # create an event tile:
                self.tiles.append(event_tile(self.parent, self.no_of_tiles, tile))
                #break
            elif (tile_type == "subhire"):
                # create a subhire tile
                pass
            elif (tile_type == "info"):
                # create an info tile
                pass
            else:
                # unknown tile found
                print("Unknown tile found")
                safe_exit()
        return


##    def get_datafile(self):
##        try:
##            datafile = open('data_file.txt', 'r')
##        except:
##            print("Datafile not present")
##            self.datafile = False               # Give self.datafile a vlaue to test on safe_exit()
##            self.safe_exit()                    # Exit the program - no file to load
##
##        return datafile


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
##        if self.datafile:               # Check if datafile is used
##            self.datafile.close()       # Close the file
        self.parent.destroy()           # Destroy the GUI
        sys.exit()                      # Terminate the program
        


    # Exit the program on Keypress
    def get_exit(self, event):
        print("keypress exit")
        self.safe_exit()
        


root = tkinter.Tk()
main = Disp_Dialog(root)

root.mainloop()
