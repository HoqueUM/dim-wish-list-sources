import os
import glob
import json

def parse_file_for_dimwishlist(file_path):
    """Parse a single file and extract lines starting with 'dimwishlist:'."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.startswith('dimwishlist:')]

def parse_directory_for_dimwishlist(directory_path):
    """Parse all .txt files in a directory for lines starting with 'dimwishlist:'."""
    all_dimwishlist_lines = []
    for file_path in glob.glob(os.path.join(directory_path, '*.txt')):
        dimwishlist_lines = parse_file_for_dimwishlist(file_path)
        all_dimwishlist_lines.extend(dimwishlist_lines)
    return all_dimwishlist_lines

directory_path = 'PandaPaxxy'
all_dimwishlist_lines = parse_directory_for_dimwishlist(directory_path)
with open('All.txt', 'w') as output_file:
    for line in all_dimwishlist_lines:
        output_file.write(line + '\n') 

lines = []
with open('All.txt', 'r') as file:
    lines = file.readlines()

recs = []

for line in lines:
    line = line.split('=')
    weapon = line[1].split('&')[0]
    perks = line[2].split(',')
    perks[len(perks)-1] = perks[len(perks)-1].replace('\n', '')
    rec = {
        "weapon": weapon,
        "perks": perks
    }
    recs.append(rec)
with open('All.json', 'w') as output_file:
    json.dump(recs, output_file, indent=4)
