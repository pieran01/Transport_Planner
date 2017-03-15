#v1 basic tile creation
#   tile class and event tile class
#v2 tile to get information from xml datafile
#    - 'datafile' variable has been changed to 'tile_node'
#       a 'tile_node' is all the xml data for a single tile
#    - event 'title' has been change to 'name'

import tkinter
import time
import datetime
import xml.etree.ElementTree
from transport_states import State
from rooms import room


class tile:

    def __init__(self, parent, no_of_tiles, tile_node):
        print("tile: init tile object")
        self.parent = parent
        self.no_of_tiles = no_of_tiles
        self.scr_w = self.parent.winfo_screenwidth()
        self.scr_h = self.parent.winfo_screenheight()
        self.tile_width = self.scr_w/(self.no_of_tiles/2)
        self.tile_height = self.scr_h/2
        self.tile_node = tile_node
        self.tile_size = 1 # by default

        # move state into zone/room class
        self.state = State.UNCONFIRMED

        # Create the tkinter frame for the tile:
        self.Tile = tkinter.Frame(self.parent, bg="white")
        self.Tile.configure(width=self.tile_width, height=self.tile_height)
        
##        # Set the position for this frame
##        self.x_pos, self.y_pos = self.set_position()
##        
##        self.Tile.place(width=self.tile_width, height=self.tile_height,
##                        x=self.x_pos, y=self.y_pos)
##      
##                        
##    # Function to handle the position of tiles on the screen
##    def set_position(self):
##
##        #-figure out what tile this is and where it should be placed
##        #-auto position based on date
##        #-store 10 place holders. when loading data, determine where
##        #  this tile should be placed
##
##
##        #tmp:
##        x_pos = 20
##        y_pos = 20
##        return x_pos, y_pos

class event_tile(tile):

    def __init__(self, parent, no_of_tiles, tile_node):
        tile.__init__(self, parent, no_of_tiles, tile_node)
        self.name = tkinter.StringVar()
        self.job_no = tkinter.IntVar()
        self.colour = "#fffffffff"
        self.l_time = tkinter.StringVar()
        self.r_time = tkinter.StringVar()
        self.rooms = [] # list to hold room objects for the tile

        self.get_data()

        #self.draw_border()
        self.draw_name()
        #self.draw_job_no()

        self.place_rooms()
              
    # End of initialisation -------
        

        
    def get_data(self):

        #get event name and job number:
        self.name.set(self.tile_node.find('name').text)

        print(self.name.get())
        self.job_no.set(self.tile_node.find('job_no').text)

        # Find every room in this event tile:
        for rm in self.tile_node.findall('room'):
            # create a room object, pass it the room node of data
            self.rooms.append(room(rm, self.Tile))

        
        # if more than 4 rooms you will need to increase
        #   the size of the tile
        
        return


    def draw_name(self):
        #title position:
        x_pos = self.tile_width/2
        y_pos = 0

        #title font:
        font_name = tkinter.font.Font(size=20)

        #title widget:

        l_name = tkinter.Label(self.Tile, textvariable=self.name, bg="white",
                                font=font_name)
        l_name.place(x=x_pos, y=y_pos, anchor='n')
        return

    def place_rooms(self):
        #for loop for each room:
        # maybe create a function that passes position data
        # to the room object and have the room object place
        # itself when this function is called???

        #First room tile will have this position
        #(relative to the event tile):
        x_pos = 0
        y_pos = self.tile_height/3  # a third of the way down the event tile

        #all room tiles will be this size:
        r_width = self.tile_width/2
        r_height = self.tile_height/3
        
        #self.rooms[0].room_frame.place(x=x_pos, y=y_pos, width=r_width, height=r_height)
        #self.rooms[1].room_frame.place(x=x_pos, y=y_pos*2, width=r_width, height=r_height)

        for rm in self.rooms:
            # If more than 4 rooms throw an error - deal with this later.
            r = self.rooms.index(rm)
            if(r>3):
                print("TOO MANY ROOMS")
                raise

            # Set horizontal position for room:
            if((r)%2==0):
                x_pos = 0
                y_pos = y_pos + ((r/2)*y_pos)
            else:
                x_pos = self.tile_width/2

            # Set vertical position for room:
            #if(r/2
            #y_pos = y_pos + ((r/2)*y_pos)

            # Place the room:
            self.rooms[r].room_frame.place(
                x=x_pos, y=y_pos,
                width=r_width, height=r_height)


            
        return

    def draw_border(self):
##        c = tkinter.Canvas(self.Tile, width=self.tile_width,
##                           height=self.tile_height)
##        l1 = c.create_line(0, 0, self.tile_width, 0,
##                           self.tile_width, self.tile_height,
##                           0, self.tile_height, 0, 0, fill="red")

        c1= tkinter.Canvas(self.Tile, width=5, height=50)
        l1 = c1.create_line(0,0,0,50, fill='red', width=10)
        c1.place(x=0, y=0)
        return


