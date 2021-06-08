import matplotlib.pyplot as plt
import importexcel as exc
import seaborn as sns
import pandas as pd
from matplotlib.widgets import Button

#Array that holds the data for 100-aisle
w, h = 18, 52
locations_picked_100 = [[0 for x in range(h)] for y in range(w)]

#Array that holds the data for 200-aisle
w1, h1 = 18, 27
locations_picked_200 = [[0 for x in range(h1)] for y in range(w1)]


#Array that holds the data for Z-axis for 100 & 200-aisle

location_z_coordinate_100 = [[0 for x in range(h)] for y in range(w)]

location_z_coordinate_200 = [[0 for x in range(h1)] for y in range(w1)]


#Callback object that holds the onclick button object.
callback = None

#Variables to keep track of the amount of stored & picked.
picked = 0
stored = 0

def create_z_dictionar(): #Iterate through the z-axis arrays and add dictionaries to them
    for i in location_z_coordinate_100:
        for j in range(0,52):
            i[j] = list(range(0,12))
            for k in range(0,12):
                
                i[j][k] = dict()
                i[j][k]['No of picked'] = 0
                i[j][k]['No of stored'] = 0
                i[j][k]['Zone'] = '?'
                i[j][k]['Articles'] = dict()
            
    for i in location_z_coordinate_200:
        for j in range(0,27):
            i[j] = list(range(0,12))
            for k in range(0,12):
                
                i[j][k] = dict()
                i[j][k]['No of picked'] = 0
                i[j][k]['No of stored'] = 0
                i[j][k]['Zone'] = '?'
                i[j][k]['Articles'] = dict()
    
            
        

def store_picked(excel_data): #Add the data from the dataframe to the 100 & 200-aisle arrays.
    
     global picked, stored
     for ind in excel_data.index: #Iterate through the dataframe
        if (excel_data['Queue    '][ind] == 'NFPP' and excel_data['MHA    '][ind] == 'NBOP1'
            and type(excel_data['From-Rack    '][ind]) == str ): #Filter the dataframe to only include outwards goods
           
            w = int(excel_data['From-Rack    '][ind]) % 100 #Width variable with the mod 100 for only getting specific aisle 1-18
            h = int(excel_data['From-X    '][ind]) #The X-axis variable
            z = int(excel_data['From-Y    '][ind]) #Y-axis variable
            
            picked_aisle = int(excel_data['From-Rack    '][ind]) - w #Get the aisle number either 100 or 200.

            if(picked_aisle == 100): #Add relevant data to the 100-aisle arrays with the information from the dataframe.
                
                locations_picked_100[w-1][h-1] += 1
                picked += 1
                location_z_coordinate_100[w-1][h-1][z-1]['No of picked'] += 1
                
                
                location_z_coordinate_100[w-1][h-1][z-1]['Zone'] = excel_data['From-Zone'][ind]
                Article = excel_data['Article    '][ind-1]
                if Article not in location_z_coordinate_100[w-1][h-1][z-1]['Articles']:
                    
                    Zone = excel_data['Buff Zone'][ind-1]
                    location_z_coordinate_100[w-1][h-1][z-1]['Articles'][Article] = dict()
                    location_z_coordinate_100[w-1][h-1][z-1]['Articles'][Article]['Number of picked'] = 1
                    location_z_coordinate_100[w-1][h-1][z-1]['Articles'][Article]['Article Zone'] = Zone

                    
                    if 'Number of stored' not in location_z_coordinate_100[w-1][h-1][z-1]['Articles'][Article]:
                        location_z_coordinate_100[w-1][h-1][z-1]['Articles'][Article]['Number of stored'] = 0
                                                                       
                else:
                    
                    location_z_coordinate_100[w-1][h-1][z-1]['Articles'][Article]['Number of picked'] += 1
                    
                    
                    
                
            else: #Add the relevant data to the 200-aisle.
                
                locations_picked_200[w-1][h-1] += 1
                picked += 1

                location_z_coordinate_200[w-1][h-1][z-1]['No of picked'] += 1
                location_z_coordinate_200[w-1][h-1][z-1]['Zone'] = excel_data['From-Zone'][ind]

                Article = Article = excel_data['Article    '][ind-1]
                if Article not in location_z_coordinate_200[w-1][h-1][z-1]['Articles']:
                    
                    Zone = excel_data['Buff Zone'][ind-1]
                    location_z_coordinate_200[w-1][h-1][z-1]['Articles'][Article] = dict()
                    location_z_coordinate_200[w-1][h-1][z-1]['Articles'][Article]['Number of picked'] = 1
                    location_z_coordinate_200[w-1][h-1][z-1]['Articles'][Article]['Article Zone'] = Zone

                    if 'Number of stored' not in location_z_coordinate_200[w-1][h-1][z-1]['Articles'][Article]:
                        location_z_coordinate_200[w-1][h-1][z-1]['Articles'][Article]['Number of stored'] = 0
                                                                       
                else:
                    location_z_coordinate_200[w-1][h-1][z-1]['Articles'][Article]['Number of picked'] += 1
                

        if (excel_data['Queue    '][ind] == 'NINI' and type(excel_data['Rack    '][ind]) == str): #If its an inwards pallet then we add the relevant info to the arrays.
            w = int(excel_data['Rack    '][ind]) % 100
            h = int(excel_data['X-Coor    '][ind]) #X axis
            z = int(excel_data['Y-Coor    '][ind]) #Y-axis variable

            left_aisle = int(excel_data['Rack    '][ind]) - w
            
            if(left_aisle == 100):
                
                locations_picked_100[w-1][h-1] += 1
                stored += 1

                location_z_coordinate_100[w-1][h-1][z-1]['No of stored'] += 1
                
               
                location_z_coordinate_100[w-1][h-1][z-1]['Zone'] = excel_data['Buff Zone'][ind] #A,B,C Classificaiton for the Z-Axis location
                Article = Article = excel_data['Article    '][ind]
                if Article not in location_z_coordinate_100[w-1][h-1][z-1]['Articles']:
                    
                    Zone = excel_data['Buff Zone'][ind]
                    location_z_coordinate_100[w-1][h-1][z-1]['Articles'][Article] = dict()
                    location_z_coordinate_100[w-1][h-1][z-1]['Articles'][Article]['Number of stored'] = 1
                    location_z_coordinate_100[w-1][h-1][z-1]['Articles'][Article]['Article Zone'] = Zone

                    if 'Number of picked' not in location_z_coordinate_100[w-1][h-1][z-1]['Articles'][Article]:
                        location_z_coordinate_100[w-1][h-1][z-1]['Articles'][Article]['Number of picked'] = 0
                                                                       
                else:
                    location_z_coordinate_100[w-1][h-1][z-1]['Articles'][Article]['Number of stored'] += 1

                

                
            else:
                
                locations_picked_200[w-1][h-1] += 1
                stored += 1
                
                location_z_coordinate_200[w-1][h-1][z-1]['No of stored'] += 1
                location_z_coordinate_200[w-1][h-1][z-1]['Zone'] = excel_data['Buff Zone'][ind]
                Article = Article = excel_data['Article    '][ind]
                if Article not in location_z_coordinate_200[w-1][h-1][z-1]['Articles']:
                    
                    Zone = excel_data['Buff Zone'][ind]
                    location_z_coordinate_200[w-1][h-1][z-1]['Articles'][Article] = dict()
                    location_z_coordinate_200[w-1][h-1][z-1]['Articles'][Article]['Number of stored'] = 1
                    
                    location_z_coordinate_200[w-1][h-1][z-1]['Articles'][Article]['Article Zone'] = Zone
                    if 'Number of picked' not in location_z_coordinate_200[w-1][h-1][z-1]['Articles'][Article]:
                        location_z_coordinate_200[w-1][h-1][z-1]['Articles'][Article]['Number of picked'] = 0
                                                                       
                else:
                    location_z_coordinate_200[w-1][h-1][z-1]['Articles'][Article]['Number of stored'] += 1
                

def onclick(event): #When a click is registered from the heatmap.
    x = int(event.xdata) #Store X coordinates clicked on
    y = int(event.ydata) #Store Y coordinates clicked on
    
    if callback.ind == 0: #If callback the index is equals to 0 then we know that the person is in the 100-aisle
        
        data = location_z_coordinate_100[y][x]
        
        data_frame = pd.DataFrame(data) #Convert data to panda dataframe

        #Create our file name
        number_string = '10' if y < 10 else '1'
        string = 'Data for coordinate X,Y ' + number_string + str(y + 1) + ' ' + str(x + 1)

        #Save as excel
        datatoexcel = pd.ExcelWriter(string + '.xlsx')
        data_frame.to_excel(datatoexcel)
        datatoexcel.save()

    else:

        data = location_z_coordinate_200[y][x]
        data_frame = pd.DataFrame(data)
        number_string = '20' if y < 10 else '2'
        string = 'Data for coordinate X,Y ' + number_string + str(y + 1) + " " + str(x + 1)
        datatoexcel = pd.ExcelWriter(string + '.xlsx')
        data_frame.to_excel(datatoexcel)
        datatoexcel.save()
        
        
# Button handler object
class Index(object):
    def __init__(self, heatplot1, my_cbar):
        self.ind = 0
        self.heatplot = heatplot1
        self.bar = my_cbar
        

    # This function is called when bswitch is clicked
    def switch(self, event): #Creates heatmap for either 100-aisle or 200-aisle, by checking the ind variable.
        if self.ind == 0:
            self.heatplot.cla() #clear plot
            
            self.heatplot.set_title("Picked/Stored in 200-aisle (Y-axis) and location in aisle (X-axis)")
               
            sns.heatmap(locations_picked_200, annot=True, fmt="d",
                    xticklabels=range(1,28), yticklabels=range(1,19), ax = self.heatplot, cbar_ax = self.bar)
            heatplot1.invert_yaxis()
            heatplot1.invert_xaxis()
            self.ind = 1 #Change ind to 1 as to apply that we are in the 200-aisle now.
        else:
            self.heatplot.cla()
            self.heatplot.set_title("Picked/Stored in 100-aisle (Y-axis) and location in aisle (X-axis)")
               
            sns.heatmap(locations_picked_100, annot=True, fmt="d",
                    xticklabels=range(1,53), yticklabels=range(1,19), ax = self.heatplot, cbar_ax = self.bar)
            heatplot1.invert_yaxis()
            heatplot1.invert_xaxis()
            self.ind = 0
            
        plt.draw()

        
if __name__ == "__main__":
    p1 = exc.ExcelClass() 
    p1.getExcel()
    create_z_dictionar() #First we create the z-array dictionary with the info needed.
    
    fig, ax = plt.subplots()
  
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
    
    store_picked(p1.data) #We iterate the dataframe and add the data to the arrays that we have created beforehand.

    
    print(picked, stored)

    #We create the plots and everything that has to do with the plots.
    
    plt.title("Picked/Stored in 100-aisle (Y-axis) and location in aisle (X-axis)")
    
    heatplot1 = sns.heatmap(locations_picked_100, annot=True, fmt="d",
                xticklabels=range(1,53), yticklabels=range(1,19), robust = True,
                            )
    heatplot1.invert_yaxis()
    heatplot1.invert_xaxis()
    cbar_ax = fig.axes[-1]

    # Initialize Button handler object
    callback = Index(heatplot1, cbar_ax)

    # Connect to a "switch" Button, setting its left, top, width, and height
    axswitch = plt.axes([0.40, 0.01, 0.2, 0.05])
    bswitch = Button(axswitch, 'Switch graph')
    bswitch.on_clicked(callback.switch)


    cid = fig.canvas.mpl_connect('button_press_event', onclick) #Calls the onclick function if you click on coordinates in the plot, this is to create the excel files with data for the Z-axis
    
    
    plt.show()
