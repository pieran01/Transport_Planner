# Client GUI

# A GUI that allows a user to update the contents of tiles on the
# display window. Initially, this will update the xml file where
# 'display window' gets it data from. It will then either 1) tell
# the 'display window' to check for a change to the xml file or 2)
# only update the file and leave the 'display window' to update its
# own contents. In the future the GUI should be on a client machine
# and connect to a server running the 'display window'. Server can
# then either update the xml accordingly or perform some other options
# to update the disply.

# File Notation:
# 'l' is the logging object
# Class names begin with Capitals
# Widget objects begin with type_name (e.g. a 'close' button: = b_close)

# 17/04/17 - v1:
# TO DO:
#   - create a series of frames with 'back' and 'next' options
#       to navigate through the xml tree
#   - locate the xml file and parse it in


import tkinter
import sys
import log_setup

l = log_setup.init_log()

# Main window:
class Client_Dialog:

    def __init__(self, parent):
        self.parent = parent
        self.parent.geometry("700x700")

        #Back, Next, Update, Close Buttons:
        self.draw_main_controls()

        self.frames = []    # This will hold the different windows/frames/views
                            # depending on which level of the xml you a editing
        self.frames.append(tkinter.Frame(self.parent, bg='black'))
        self.frames.append(tkinter.Frame(self.parent, bg='red'))

        self.current_frame = 0  # Hold the current frame being displayed

        self.display_frame(self.current_frame) 

    #End init--------

    def draw_main_controls(self):
        # Function creates the standard butons to appear all the time
        # These include Close, Update(save), Back, Next, Notes
        self.b_close = tkinter.Button(self.parent, text="Close", command=self.func_close)
        self.b_back = tkinter.Button(self.parent, text="Back", command=self.func_back)
        self.b_next = tkinter.Button(self.parent, text="Next", command=self.func_next)
        self.b_update = tkinter.Button(self.parent, text="Update", command=self.func_update)
        self.b_notes = tkinter.Button(self.parent, text="Note Tile", command=self.func_notes)

        b_height = 40
        b_width = 50
        b_ypos = 650

        self.b_close.place (x=600, y=b_ypos, height=b_height, width=b_width)
        self.b_back.place  (x=50,  y=b_ypos, height=b_height, width=b_width)
        self.b_next.place  (x=100, y=b_ypos, height=b_height, width=b_width)
        self.b_update.place(x=550, y=b_ypos, height=b_height, width=b_width)
        self.b_notes.place (x=300, y=b_ypos, height=b_height, width=100)

    def display_frame(self, frame):
        for f in self.frames:
            f.place_forget()

        self.frames[frame].place(x=50, y=50, height=100, width=100)
        #self.frames[frame].pack()

    def f_jobs(self):
        #self.frames[0].
        pass

    def func_close(self):
        l.debug("Closing")
        self.parent.destroy()   #Close window
        sys.exit()              #Exit Program

    def func_back(self):
        if(self.current_frame > 0):
            self.current_frame -= 1     # go back a frame
            l.debug("Current Frame = " + str(self.current_frame))
        self.display_frame(self.current_frame)

    def func_next(self):
        if(self.current_frame < len(self.frames)-1):
            self.current_frame += 1
            l.debug("Current Frame = " + str(self.current_frame))
        self.display_frame(self.current_frame)

    def func_update(self):
        pass

    def func_notes(self):
        #This should open a new text editor kind of window
        #for editing the notes tile
        pass

#------------------------------------------
# Main call to begin GUI:
root = tkinter.Tk()
main = Client_Dialog(root)

root.mainloop()
