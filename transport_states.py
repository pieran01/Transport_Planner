# States of the transport planner:
from enum import Enum

class State(Enum):
    UNCONFIRMED = 0     # Pick list not complete - do not pick
    CONFIRMED = 1       # Pick list confirmed - begin pick when ready
    PICKING = 2         # Job is currently being picked
    PICKED = 3          # Job is picked and ready for loading
    LOADING = 4         # Job is currently being loaded
    LOADED = 5          # Job has been loaded onto truck
    OUT = 6             # Job has left / Truck has departed from smyle
    RETURNED = 7        # Job has returned to be unloaded
    COMPLETE = 8        # Job is complete and can be removed from planner

