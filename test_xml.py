import sys


datafile = open('data_file.txt', 'r')

# Function to find an xml tag:
def find_tag(tag, datafile):
    found = False
    while not found:
        readln = datafile.readline()
        print(readln)
        if(readln.strip() == tag):
            found = True
        elif(readln == ""):
            print("eof found without tag")
            break
    return found


# Function to get a tag's data
def get_data(tag, datafile):
    # look for 'tag'
    # read data until end tag found

# Function to find start of file tag:
def sof_tag(dataile):
    found = find_tag('<sof>', datafile)
    return found

# Function to find tile tag:
def tile_tag(datafile):
    found = find_tag('<tile>', datafile)
    if found:
        data = get_data*=(tag, datafile)


##---------- MAIN -----------##

# To begin loading in the file we are expecting to find a
# 'Start of File' tag: <sof>
if not sof_tag(datafile):
    print('no sof - closing')
    #safe close
    datafile.close()
    sys.exit()

# If SOF is found, we will be creating a tile next. We need to find what
# type of tile object to make
tile_type = tile_tag(datafile)
if (tile_type == 'event'):
    #create an event tile
    print("event tile")
elif(tile_type == 'subhire'):
    #create a subhire tile
    print("subhire tile")
elif(tile_type == 'info'):
    #create an info tile
    print("info tile")
else:
    #unknown tile type
    print("unknown tile")

print("end")
