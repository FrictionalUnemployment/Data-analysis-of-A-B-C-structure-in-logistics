import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import importexcel as exc

#Create array for 100 location
w, h = 18, 52
locations_picked_100 = [[0 for x in range(h)] for y in range(w)]
locations_layout = [[0 for x in range(h)] for y in range(w)] #The A,B,C summarization array with A,B,C for each X,Y location


#Create array for 200 location
w1, h1 = 18, 27
locations_picked_200 = [[0 for x in range(h1)] for y in range(w1)]
locations_layout2 = [[0 for x in range(h1)] for y in range(w1)]

#The Z-axis array for each aisle
location_z_coordinate_100 = [[0 for x in range(h)] for y in range(w)]
location_z_coordinate_200 = [[0 for x in range(h1)] for y in range(w1)]


#Filling the Z-axis arrays with dictionaries with the data that is relevant for each location
def create_z_dictionar():
    for i in location_z_coordinate_100: #Iterate the 100-aisle for the Z-axis.
        for j in range(0,52):
            i[j] = list(range(0,12)) 
            for k in range(0,12):
                
                i[j][k] = dict()
                i[j][k]['Zone'] = '?' #Add a Zone key for each location in this aisle.
            
    for i in location_z_coordinate_200: #Same as 100-aisle just changed range (width height for the aisle)
        for j in range(0,27):
            i[j] = list(range(0,12))
            for k in range(0,12):
                
                i[j][k] = dict()
                i[j][k]['Zone'] = '?'

def store_zone(excel_data): #Iterate through the panda dataframe and fill the z coordinate with relevant data
    for ind in excel_data.index:
        if(excel_data['MHA    '][ind] == 'NBUFF' or excel_data['MHA    '][ind] == 'NHVY'): #Filter the panda dataframe 
           
            w = int(excel_data['Rack    '][ind]) % 100 #Mod 100 of the rack to get the aisle number in the form of 1-18
            h = int(excel_data['X-Coor    '][ind]) 
            z = int(excel_data['Y-Coor    '][ind])

            picked_aisle = int(excel_data['Rack    '][ind]) - w #Get the rack number (The aisle) either 100 or 200

            if(picked_aisle == 100):
                location_z_coordinate_100[w-1][h-1][z-1]['Zone'] = excel_data['Zone    '][ind] #Fill the z-coordinate with the A,B,C classification for 100-aisle

            else:
                location_z_coordinate_200[w-1][h-1][z-1]['Zone'] = excel_data['Zone    '][ind] #Fill the z-coordinate with the A,B,C classification for 200-aisle

def sum_define_zones(loc_100, loc_200): #Find the summarizied classifaction from the Z-axis array and append them to the X,Y-axis.
    
    row = 0
    for i in loc_100: #Iterate the array
        column = 0
        for j in i:
            
            a = 0
            b = 0
            c = 0
            for k in j:
                if(k['Zone'] == 'A'): #Add amount of A-zones to the variables
                    a += 1
                if(k['Zone'] == 'B'):
                    b += 1
                if(k['Zone'] == 'C'):
                    c += 1
            max_txt = 'A'
            max = a
            if a < b: #Find the variable that is the biggest.
                max_txt = 'B'
                max = b
            if b < c:
                if c > a:
                    max_txt = 'C'
                    max = c
            
            locations_layout[row][column] = max #append the no of reoccuring A,B,C for that location
            locations_picked_100[row][column] = max_txt #Append the A,B,C for that location
            column += 1
        row += 1
    row = 0
    for i in loc_200: #Iterate the array
        column = 0
        for j in i:
            
            a = 0
            b = 0
            c = 0
            for k in j:
                if(k['Zone'] == 'A'): #Add amount of A-zones to the variables
                    a += 1
                if(k['Zone'] == 'B'):
                    b += 1
                if(k['Zone'] == 'C'):
                    c += 1
            max_txt = 'A'
            max = a
            if a < b: #Find the variable that is the biggest.
                max_txt = 'B'
                max = b
            if b < c:
                if c > a:
                    max_txt = 'C'
                    max = c
            
            locations_layout2[row][column] = max #append the no of reoccuring A,B,C for that location
            locations_picked_200[row][column] = max_txt #Append the A,B,C for that location
            column += 1
        row += 1
    
                

if __name__ == "__main__":
    p1 = exc.ExcelClass() #Import production object
    p1.getExcel() 
    create_z_dictionar() #Create the Z array with the necessary data

    store_zone(p1.data) #Add the dataframe data to the arrays

    sum_define_zones(location_z_coordinate_100, location_z_coordinate_200) #Create the A,B,C classifications and fill the arrays with data

    #Create the plots for 100 and 200-aisles.
    fig, ax = plt.subplots()
  
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

    plt.title("A,B,C Layout for each X,Y Coordinate summarized, 100-aisle.")
    
    heatplot1 = sns.heatmap(locations_layout, annot=locations_picked_100, fmt="",
                xticklabels=range(1,53), yticklabels=range(1,19), robust = True,
                            )
    heatplot1.invert_yaxis()
    heatplot1.invert_xaxis()

    plt.figure()

    plt.title("A,B,C Layout for each X,Y Coordinate summarized, 200-aisle.")
    
    heatplot1 = sns.heatmap(locations_layout2, annot=locations_picked_200, fmt="",
                xticklabels=range(1,28), yticklabels=range(1,19), robust = True,
                            )
    heatplot1.invert_yaxis()
    heatplot1.invert_xaxis()
    

    plt.show()
