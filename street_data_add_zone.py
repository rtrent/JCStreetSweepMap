import json
import glob
import os
import codecs

#get a list of all geojson files in the folder "data/partialFiles"
filenames = glob.glob('data/partialFiles/*.geojson', recursive = True)

#create a loop to go through all the files
for filename in filenames:

    #print(filename)
#load a single street data file
    data = json.load(codecs.open(filename, 'r', 'utf-8-sig'))


    #print(data)

    #Loop over GeoJSON features and add the new properties
    for feat in data['features']:
        feat["properties"]["parking_zone"] = "TBU"

    with open(filename, 'w') as f:
        json.dump(data, f, indent = 2)

    f.close()
