
# Problem: Given three integers x,y and z representing the dimensions of a
#   cuboid along with integer n, print all possible coordinates given by
#   (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.
#   Must use list comprehensions.

x = int(input("Enter X: "))
y = int(input("Enter Y: "))
z = int(input("Enter Z: "))
n = int(input("Enter N: "))

for x in range(0,x+1):
    for y in range(0,y+1):
        for z in range(0,z+1):
            if x+y+z != n:
                print(x,y,z)

mycoordinates = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k!=n]
print(mycoordinates)
