import matplotlib.pyplot as plt
import seaborn as sns
import random as random

w, h = 18, 52
locations_picked_100 = [[0 for x in range(h)] for y in range(w)]

w1, h1 = 18, 27
locations_picked_200 = [[0 for x in range(h1)] for y in range(w1)]

max_A = 7179
max_B = 4054
max_C = 5564

current_A = 0

current_B = 0

current_C = 0

max_placed_pallets = 41038
max_pallets = 0


loc_x = 0
for i in locations_picked_100:
    
    curr_loc_y = 0
    for j in i:
    
        distribution_A = random.randint(8,15)
        distribution_B = random.randint(3,9)
        distribution_C = random.randint(1,4)
      
        if curr_loc_y > 0 and loc_x < 10 and (loc_x + 1) % 2 == 0:
          
            locations_picked_100[loc_x][curr_loc_y] = distribution_A * 5
            max_pallets += distribution_A * 5
            current_A += 1
        if curr_loc_y > 0 and loc_x < 10 and (loc_x + 1) % 2 != 0:
            locations_picked_100[loc_x][curr_loc_y] = distribution_B * 5
            max_pallets += distribution_B * 5
            current_B += 1
        if curr_loc_y > 0 and loc_x >= 10 and (loc_x + 1) % 2 != 0:
            locations_picked_100[loc_x][curr_loc_y] = distribution_C * 3
            max_pallets += distribution_C * 3
            current_C += 1

        if curr_loc_y > 0 and loc_x >= 10 and (loc_x +1) % 2 == 0:
            locations_picked_100[loc_x][curr_loc_y] = distribution_B * 5
            max_pallets += distribution_B * 5
            current_B += 1

        if curr_loc_y == 0:
            locations_picked_100[loc_x][curr_loc_y] = distribution_C * 2
            max_pallets += distribution_C * 2
            current_C += 1
        curr_loc_y += 1
            
        
    loc_x += 1

loc_x = 0
for i in locations_picked_200:
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
