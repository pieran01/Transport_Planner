#Client Frames
# A class for frames that will be used in the client GUI
# Base class will be list box and frame design
# tile_frame and room_frame will inherrit client_frames
# and then take on their own attributes

import tkinter
from log_setup import l


#Basic Frame:
def basic_frame(parent_frame, title):
    frame_title = tkinter.Label(parent_frame, text=title)
    frame_subtitle = tkinter.Label(parent_frame, text="Attributes:")
    list_box = tkinter.Listbox(parent_frame)

    frame_title.grid(row=0)
    frame_subtitle.grid(row=0, column=1)
    list_box.grid(row=1)
    return list_box


def tile_frame(parent_frame, datafile):
    lb = basic_frame(parent_frame, "Tile/Jobs")
    l.debug("loading tile list box")
    # Load list of jobs into listbox:
    for tile in datafile.findall('tile'):
        tile_type = tile.get('type')
        l.debug("Tile type: " + tile_type)
        if(tile_type == "event"):
            l.debug(tile.find('name').text)
            lb.insert("end", tile.find('name').text)

    e_name = tkinter.Entry(parent_frame)
    e_job_no = tkinter.Entry(parent_frame)
    l_name = tkinter.Label(parent_frame, text="Job Name: ")
    l_job_no = tkinter.Label(parent_frame, text="Job Number: ")

    l_name.grid(row=1, column=1)
    e_name.grid(row=1, column=2)
    l_job_no.grid(row=2, column=1)
    e_job_no.grid(row=2, column=2)

    lb.bind('<<ListboxSelect>>', lambda event: list_selection(event, lb))
    return

def room_frame(parent_frame, datafile):
    lb = basic_frame(parent_frame, "Room")
    
    return


#Mouse binding for listbox selections:
def list_selection(event, lb):
    l.debug("List box select event")
    index = lb.curselection()[0]
    selected_item = lb.get(index)
    l.debug("Selected: " + selected_item)
