import tkinter
import time
import datetime
from transport_states import State


class tile:

    def __init__(self, parent, no_of_tiles, datafile):
        print("tile: init tile object")
        self.parent = parent
        self.no_of_tiles = no_of_tiles
        self.scr_w = self.parent.winfo_screenwidth()
        self.scr_h = self.parent.winfo_screenheight()
        self.tile_width = self.scr_w/(self.no_of_tiles/2)
        self.tile_height = self.scr_h/2
        self.datafile = datafile

        # move state into zone/room class
        self.state = State.UNCONFIRMED

        # Create the tkinter frame for the tile:
        self.Tile = tkinter.Frame(self.parent, bg="white")
        
        # Set the position for this frame
        self.x_pos, self.y_pos = self.set_position()
        
        self.Tile.place(width=self.tile_width, height=self.tile_height,
                        x=self.x_pos, y=self.y_pos)
      
                        
    # Function to handle the position of tiles on the screen
    def set_position(self):

        #-figure out what tile this is and where it should be placed
        #-auto position based on date
        #-store 10 place holders. when loading data, determine where
        #  this tile should be placed


        #tmp:
        x_pos = 20
        y_pos = 20
        return x_pos, y_pos

class event_tile(tile):

    def __init__(self, parent, no_of_tiles, datafile):
        tile.__init__(self, parent, no_of_tiles, datafile)
        self.title = tkinter.StringVar()
        self.colour = "#fffffffff"
        self.l_time = tkinter.StringVar()
        self.r_time = tkinter.StringVar()

        self.get_data()

        self.draw_title()
        self.draw_colour()
        
        
    # End of initialisation -------
        

        
    def get_data(self):
##        self.title.set("Test")
##        self.colour = "#0ff000fff"
##        self.l_time = datetime.date(2017,1,17)
##        self.r_time = datetime.date(2017,1,20)

        #open data_file (continue where it was last opened?)
        #get event name
        #until end of rooms marker:
        # create room object (and pass datafile to it)
        #  in the room object init, it will extract the data it needs
        # check for end of rooms marker
        #check for end of tile marker
        
        return


    def draw_title(self):
        #title position:
        x_pos = self.tile_width/2
        y_pos = 0

        #title font:
        font_title = tkinter.font.Font(size=20)

        #title widget:
        l_title = tkinter.Label(self.Tile, textvariable=self.title, bg="white",
                                font=font_title)
        l_title.place(x=x_pos, y=y_pos, anchor='n')
        return

    def draw_colour(self):
        #colour position:
        x_pos = self.tile_width/2
        y_pos = 50

        #colour size:
        l_height = 50
        l_width = self.tile_width-50
    
        #colour widget:
        l_event_colour = tkinter.Label(self.Tile, bg=self.colour)
        l_event_colour.place(anchor="n", x=x_pos, y=y_pos, height=l_height,
                             width=l_width)
        return



