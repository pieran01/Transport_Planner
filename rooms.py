#Class for rooms
#At least one room for each event tile
#The room holds all the timing data

import datetime
import xml.etree.ElementTree
import tkinter
import room_colours

class room:

    def __init__(self, room_node, parent):
        self.room_node = room_node
        self.parent = parent
        
        # Room data:
        self.name = tkinter.StringVar()     # room name

        self.get_room_data()
        
        self.draw_frame()
        
 

        

        #build widgets (tile will .place them)

    # End of initialisation --------

    def get_data(self, data_item):
        try:
            data = self.room_node.find(data_item).text
        except AttributeError:
            data = "n/a"

        return data

    # Function to get all the room related data
    def get_room_data(self):
        self.name.set(self.room_node.get('name'))
        print("room name: ", self.name.get())

        self.colour = self.get_data('colour')
        # will require something to interpret 'colour' 
        print(self.colour)

        self.time_load = self.get_data('time_load')
        print(self.time_load)
        


        #room name, load time, colour, state, return time, load date, return
        #date

    # Function to create a frame of room data for the tile
    #  class to display appropriately
    def draw_frame(self):

        # Fram to hold all room widgets (tile class will 'place' frame)
        self.room_frame = tkinter.Frame(self.parent, bg='#f00f00f00')
        #self.room_frame.config(width=200, height=200)

        # Room name widget:
        w_name = tkinter.Label(self.room_frame, textvariable=self.name, bg='white')
        w_name.place(x=100, y=0, anchor='n')

        # Room colour widget:
        col = room_colours.Colours()
        colour = col.convert(self.colour)
        w_colour = tkinter.Label(self.room_frame, bg=colour)
        w_colour.place(x=100, y=50, anchor='n', width=100, height=50)

                       
