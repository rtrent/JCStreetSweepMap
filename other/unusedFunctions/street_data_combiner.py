import json
import glob
import os

#create a master file which will be the geojson
masterfile = []


#the first three lines need to be as follows
#line 1 {
#line 2  "type": "FeatureCollection",
#line 3  "features": [

masterfile.append('{\n')
masterfile.append('  "type": "FeatureCollection",\n')
masterfile.append('    "features": [\n')

#get a list of all geojson files in the folder
#"data/partialFiles"


filenames = glob.glob('data/partialFiles/*.geojson', recursive = True)

#files must be saved as formatted json for this to work
#with new lines for each line of json
#if they are saved as a single string it will break
#geojson.io saves files as a sinlge line
#need to copy and paste the formatted json

#perhaps I should count the number of lines and if there is a single line
#do one approach
#and if there are more than one I know I can use this method

# filenames = [
#    "data/partialFiles/Hamilton_6th.geojson",
#    "data/partialFiles/Hamilton_7th.geojson",
#    "data/partialFiles/VanVorst_Wayne.geojson",
#    "data/partialFiles/VanVorst_York.geojson"
# ] 


print(filenames)


#create a loop to go through all the files
for filename in filenames:

#load a single street data file
#this works for one file  #filename = "data/partialFiles/Hamilton_6th.geojson"
    
    file = open(filename, "r")

#read all the lines except the first three and last three
    jsonfile = file.readlines()[3:-3]


#append all these lines into the new full file
#need to loop through lines and append each one
    for line in jsonfile:
        masterfile.append(line)


#close that one file
    file.close()

#add a "}," as a line after what I just loaded
    masterfile.append('    },\n')

#repeat for the next file until finished

#DO NOT ADD a comma to the very last file instead it should end with "}" no comma

#since the loop adds a "}," as a new line at the end of every loaded file
#I need to delete the very last row in the master file
#it is curently "}," but should be "}"
del masterfile[-1]
masterfile.append('    }\n')


#once all the files are loaded add the final two lines
masterfile.append('  ]\n')
masterfile.append('}')
#second to last line ]
#last line }

#check my work
for line in masterfile:
    print(line)

#save to new file
with open("data/streetdata.geojson", "w+") as f:
    for line in masterfile:
        f.write(line)
    f.close()


#IT WORKS :)
