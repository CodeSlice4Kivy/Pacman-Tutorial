from kivy.uix.widget import Widget
from kivy.properties import StringProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector

# boundary points
bpoint = {}
bpoint[1] = (89,40)
bpoint[2] = (1032,40)
bpoint[3] = (89,283)
bpoint[4] = (1032,283)

bpoint[5] = (255,40)
bpoint[6] = (255,283)

bpoint[7] = (510,40)
bpoint[8] = (510,283)

bpoint[9] = (688,40)
bpoint[10] = (688,283)

bpoint[11] = (866,40)
bpoint[12] = (866,283)

bpoint[13] = (178,121)
bpoint[14] = (255,121)
bpoint[15] = (178,202)
bpoint[16] = (255,202)

bpoint[17] = (510,121)
bpoint[18] = (599,121)
bpoint[19] = (599,202)
bpoint[20] = (688,202)

bpoint[21] = (955,121)
bpoint[22] = (1032,121)
bpoint[23] = (955,202)
bpoint[24] = (1032,202)

bpoint[25] = (777,40)
bpoint[26] = (777,121)

bpoint[27] = (0,159)
bpoint[28] = (89,159)
bpoint[29] = (1032,159)
bpoint[30] = (1109,159)

# Passage list
passages = []

# now that we have our if statement
# lets create passages by linking our point
passages = [bpoint[1] + bpoint[2], bpoint[2] + bpoint[4],bpoint[1] + bpoint[3],bpoint[3] + bpoint[4],\
            bpoint[5] + bpoint[6], bpoint[7] + bpoint[8],bpoint[9] + bpoint[10],bpoint[11] + bpoint[12],\
            bpoint[13] + bpoint[14], bpoint[15] + bpoint[16],bpoint[17] + bpoint[18],bpoint[19] + bpoint[20],\
            bpoint[21] + bpoint[22], bpoint[23] + bpoint[24],bpoint[25] + bpoint[26],bpoint[27] + bpoint[28],\
            bpoint[29] + bpoint[30]]


class Player(Widget):
    pac_img = StringProperty('images/pac_right.gif')

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
  
    def move(self):
        # now we will use if statements to create passages for our player to
        # move in using our boundary point.
        # we will connect two boundary points to form passages
        # We have 17 passages in total in our case

        #make sure passages list is created
        # now lets create our if statements for x and y restrictions

        for passage in passages:
            if (passage[0] <= self.velocity_x + self.pos[0]) and \
               (passage[2] >= self.velocity_x + self.pos[0]) and \
               (passage[1] <= self.velocity_y + self.pos[1]) and \
               (passage[3] >= self.velocity_y + self.pos[1]):
            
                # Besure to move the below into if statement

                self.pos = Vector(*self.velocity)+self.pos
                
                if self.velocity == [0, 1]:
                    self.pac_img = "images/pac_up.gif"
                elif self.velocity == [0, -1]:
                    self.pac_img = "images/pac_down.gif"
                elif self.velocity == [-1, 0]:
                    self.pac_img = "images/pac_left.gif"
                elif self.velocity == [1, 0]:
                    self.pac_img = "images/pac_right.gif"
        
    
