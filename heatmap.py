import matplotlib.pyplot as plt
import importexcel as exc
import seaborn as sns
import pandas as pd
from matplotlib.widgets import Button

w, h = 18, 52
locations_picked_100 = [[0 for x in range(h)] for y in range(w)]


w1, h1 = 18, 27
locations_picked_200 = [[0 for x in range(h1)] for y in range(w1)]

location_z_coordinate_100 = [[0 for x in range(h)] for y in range(w)]

location_z_coordinate_200 = [[0 for x in range(h1)] for y in range(w1)]

callback = None


picked = 0
stored = 0

def create_z_dictionar():
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
    
            
        

def store_picked(excel_data):
     global picked, stored
     for ind in excel_data.index:
        if (excel_data['Queue    '][ind] == 'NFPP' and excel_data['MHA    '][ind] == 'NBOP1'
            and type(excel_data['From-Rack    '][ind]) == str ):
           
            w = int(excel_data['From-Rack    '][ind]) % 100
            h = int(excel_data['From-X    '][ind])
            z = int(excel_data['From-Y    '][ind])
            
            picked_aisle = int(excel_data['From-Rack    '][ind]) - w

            if(picked_aisle == 100):
                
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
                    
                    
                    
                
            else:
                
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
                

        if (excel_data['Queue    '][ind] == 'NINI' and type(excel_data['Rack    '][ind]) == str):
            w = int(excel_data['Rack    '][ind]) % 100
            h = int(excel_data['X-Coor    '][ind])

            left_aisle = int(excel_data['Rack    '][ind]) - w

            if(left_aisle == 100):
                
                locations_picked_100[w-1][h-1] += 1
                stored += 1

                location_z_coordinate_100[w-1][h-1][z-1]['No of stored'] += 1
                
               
                location_z_coordinate_100[w-1][h-1][z-1]['Zone'] = excel_data['Buff Zone'][ind]
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
                

def onclick(event):
    if callback.ind == 0: #if event.dblclick
        x = int(event.xdata)
        y = int(event.ydata)
        
        
        data = location_z_coordinate_100[y][x]
        data_frame = pd.DataFrame(data)
        
        number_string = '10' if y < 10 else '1'
        string = 'Data for coordinate X,Y ' + number_string + str(y) + ' ' + str(x)
        
        datatoexcel = pd.ExcelWriter(string + '.xlsx')
        data_frame.to_excel(datatoexcel)
        datatoexcel.save()

    else:
        x = int(event.xdata)
        y = int(event.ydata)

        data = location_z_coordinate_200[y][x]
        data_frame = pd.DataFrame(data)
        number_string = '20' if y < 10 else '2'
        string = 'Data for coordinate X,Y ' + str(y) + " " + str(x)
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
    def switch(self, event):
        if self.ind == 0:
            self.heatplot.cla()
            
            self.heatplot.set_title("Picked/Stored in 200-aisle (Y-axis) and location in aisle (X-axis)")
               
            sns.heatmap(locations_picked_200, annot=True, fmt="d",
                    xticklabels=range(1,28), yticklabels=range(1,19), ax = self.heatplot, cbar_ax = self.bar)
            heatplot1.invert_yaxis()
            heatplot1.invert_xaxis()
            self.ind = 1
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
    create_z_dictionar()
    
    fig, ax = plt.subplots()
  
    

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
    
    store_picked(p1.data)

    
    print(picked, stored)

    
    
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


    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    

    plt.show()
