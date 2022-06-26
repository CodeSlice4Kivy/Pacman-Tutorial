from kivy.uix.widget import Widget
from player import passages

food = []

# here now we will type the code of were we want the food to appear
# We want the food to appear between the passages hence we import passages

for a0, a1, b0, b1 in passages:
    if a0==b0:
        for j in range(int(a1)+20, int(b1)-20,20):
            # We are now placing the food points in the vertical passages
            food.append([a0 + 38.5, j + 38.5])
            # we have now centered the points

    else:
        for j in range(int(a0),int(b0),20):
            # We are basically placing them horizontally now
            food.append([j + 38.5, a1 + 38.5])

food = food[:191]

class Points(Widget):
    print('this is food')
