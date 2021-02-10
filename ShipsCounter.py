ships = [
            [ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, ],
            [ 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, ],
            [ 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, ],
            [ 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, ],
            [ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [ 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [ 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, ],
            [ 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, ]
            ]

neigh = ((1,0), (-1, 0), (0, -1), (0, 1))
my_ships = []
zeroes = []

#Checking cell in list
def in_arr(i, j):
    
    if 0 <= i < len(ships) and 0<= j < len(ships[0]):    
        return True

#Checking that cell wasn't checked before
def valid(i, j):
    if not in_arr(i, j):
        return False
    return ships[i][j] and not (i,j) in my_ships

#Checking neighbours cells
def neighbours(i, j):
    
    for n in neigh:
        x = i + n[0]
        y = j + n[1]
        
        if valid(x, y):

                my_ships.append((x, y))
                neighbours(x, y)

count = 0
#Main loop
for index_x, row in enumerate(ships):
    for index_y, element in enumerate(row):
        
        if valid(index_x, index_y):
            count += 1
            my_ships.append((index_x, index_y))
            neighbours(index_x, index_y)
    

print(count)
