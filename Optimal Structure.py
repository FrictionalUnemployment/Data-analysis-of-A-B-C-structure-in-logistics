import matplotlib.pyplot as plt
import seaborn as sns
import random as random

#Create X,Y arrays for 100 and 200-aisle
w, h = 18, 52
locations_picked_100 = [[0 for x in range(h)] for y in range(w)]

w1, h1 = 18, 27
locations_picked_200 = [[0 for x in range(h1)] for y in range(w1)]

#max_A = 7179
#max_B = 4054
#max_C = 5564

#Counter for how many A,B,C locations we have created.
current_A = 0

current_B = 0

current_C = 0

#max_placed_pallets = 41038, Counter for amount of pallets we have placed in the locations
max_pallets = 0


loc_x = 0
for i in locations_picked_100: #Iterate the 100-aisle add the necessary data with the random generator in each x,y location depending on parameters.
    
    curr_loc_y = 0
    for j in i:
    
        distribution_A = random.randint(8,15)
        distribution_B = random.randint(3,9)
        distribution_C = random.randint(1,4)
      
        if curr_loc_y > 0 and loc_x < 10 and (loc_x + 1) % 2 == 0: #If the location is not the first location in Y and the location is less than 10 (close to the pack station) and we're at an even aisle.
          
            locations_picked_100[loc_x][curr_loc_y] = distribution_A * 5
            max_pallets += distribution_A * 5
            current_A += 1
        if curr_loc_y > 0 and loc_x < 10 and (loc_x + 1) % 2 != 0: #Same as before, but uneven aisle.
            locations_picked_100[loc_x][curr_loc_y] = distribution_B * 5
            max_pallets += distribution_B * 5
            current_B += 1
        if curr_loc_y > 0 and loc_x >= 10 and (loc_x + 1) % 2 != 0: #The location is over or equals to 10 (Far away from the pack station) and its an uneven aisle.
            locations_picked_100[loc_x][curr_loc_y] = distribution_C * 3
            max_pallets += distribution_C * 3
            current_C += 1

        if curr_loc_y > 0 and loc_x >= 10 and (loc_x +1) % 2 == 0: #Location is over or equals to 10 and its an even aisle. 
            locations_picked_100[loc_x][curr_loc_y] = distribution_B * 5
            max_pallets += distribution_B * 5
            current_B += 1

        if curr_loc_y == 0: #If its the first location in the aisle in (Y).
            locations_picked_100[loc_x][curr_loc_y] = distribution_C * 2
            max_pallets += distribution_C * 2
            current_C += 1
        curr_loc_y += 1
            
        
    loc_x += 1

loc_x = 0
for i in locations_picked_200: #Same logic applied as 100-aisle. Just with less distribution.
    curr_loc_y = 0
    for j in i:
    
        distribution_A = random.randint(4,12)
        distribution_B = random.randint(3,6)
        distribution_C = random.randint(1,5)
      
        if curr_loc_y > 0 and loc_x < 10 and (loc_x + 1) % 2 == 0:
          
            locations_picked_200[loc_x][curr_loc_y] = distribution_A * 5
            max_pallets += distribution_A * 5
            current_A += 1
        if curr_loc_y > 0 and loc_x < 10 and (loc_x + 1) % 2 != 0:
            locations_picked_200[loc_x][curr_loc_y] = distribution_B * 5
            max_pallets += distribution_B * 5
            current_B += 1
        if curr_loc_y > 0 and loc_x >= 10 and (loc_x + 1) % 2 != 0:
            locations_picked_200[loc_x][curr_loc_y] = distribution_C * 2
            max_pallets += distribution_C * 2
            current_C += 1

        if curr_loc_y > 0 and loc_x >= 10 and (loc_x +1) % 2 == 0:
            locations_picked_200[loc_x][curr_loc_y] = distribution_B * 5
            max_pallets += distribution_B * 5
            current_B += 1

        if curr_loc_y == 0:
            locations_picked_200[loc_x][curr_loc_y] = distribution_C * 2
            max_pallets += distribution_C * 2
            current_C += 1
        curr_loc_y += 1
            
        
    loc_x += 1
        

print(current_A, current_B, current_C, max_pallets)

#Create each respective heatmap plot.
fig, ax = plt.subplots()

plt.title("Picked/Stored in 100-aisle (Y-axis) and location in aisle (X-axis)")
heatplot1 = sns.heatmap(locations_picked_100, annot=True, fmt="d",
            xticklabels=range(1,53), yticklabels=range(1,19), robust = True,
                            )
heatplot1.invert_yaxis()
heatplot1.invert_xaxis()

plt.figure()

plt.title("Picked/Stored in 200-aisle (Y-axis) and location in aisle (X-axis)")
heatplot1 = sns.heatmap(locations_picked_200, annot=True, fmt="d",
            xticklabels=range(1,28), yticklabels=range(1,19), robust = True,
                            )
heatplot1.invert_yaxis()
heatplot1.invert_xaxis()

plt.show()
