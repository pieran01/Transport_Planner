
##import xml.etree.ElementTree as ET
import xml.etree.ElementTree

##tree = ET.parse('data_file_xml.xml')
##root = tree.getroot()
##print("root = " + str(root))

##for child in root:
##    print(child.tag, child.attrib)
##    for a in child:
##        print(a.tag, a.attrib)

##for country in root.findall('country'):
##    rank = country.find('rank').text
##    rank_up = country.find('rank').get('updated')
##    name = country.get('name')
##    print(name, rank, rank_up)



##for country in root.findall('country'):
##    rank = country.find('rank')
##    rank_up = rank.get('updated')
##    rank_num = rank.text
##    name = country.get('name')
##    print(name, rank_num, rank_up)


def event_tile(tile):
    name = tile.find('name').text
    job = tile.find('job_no').text
    print(name, job)

    #now find rooms for the event:
    for room in tile.findall('room'):
        print(room.get('name'))
    
    return

##tree = ET.parse('data_file_xml3.xml')
tree = xml.etree.ElementTree.parse('data_file_xml3.xml')
root = tree.getroot()
print(root)

for tile in root.findall('tile'):
    t_type = tile.get('type')
    print("Tile type: ", t_type)
    if t_type == 'event':
        print("an event tile has been found")
        event_tile(tile)
##        name = tile.find('name').text
##        job = tile.find('job_no').text
##        print(name, job)
    elif t_type == 'info':
        print("an info tile has been found")
    elif t_type == 'subhire':
        print("a subhire tile has been found")
    else:
        print("unknown tile found")
