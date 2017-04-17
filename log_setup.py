#Basic Logging setup
#Set up the required handlers/formats for the log in 'init_log'
#Import this file into your program
#Call init_log, which will reutrn a logging object to use

import logging
import logging.handlers

def init_log():
    #Set up a new logger:
    l = logging.getLogger("log_name")
    l.setLevel(logging.DEBUG)


    #Set up console handler:
    console_output = logging.StreamHandler()    # output to idle console window
    console_output.setLevel(logging.DEBUG)      # output debug logs
    console_format = logging.Formatter(fmt='%(asctime)s %(filename).8s %(funcName)s (%(levelname)s)\t- %(message)s',
                                  datefmt='%H:%M:%S')
    console_output.setFormatter(console_format)


    #Apply handlers to logger:
    l.addHandler(console_output)

    l.debug("Logging initialised")
    return l
