from mcpi.minecraft import Minecraft

mc = Minecraft.create()
def fill(b):
    b = list(b)
    for i in range(0, len(b)):
        if b[i] == '#' and b[i+1] == '#':
            pass
        elif b[i] == '#' and '#' in b[i+1:]:
            indexOf = b[i+1:].index('#') + i+1
            for g in range(i+1, indexOf):
                b[g] = '#'
    return b
class ellipse:
    def __init__(self, r, y = None, x = None, z = None):
        if x == None:
            self.x = mc.player.getPos().x
        else:
            self.x = x
        if y == None:
            self.y = mc.player.getPos().y
        else:
            self.y = y
        if z == None:
            self.z = mc.player.getPos().z
        else:
            self.z = z
        self.r = r

    def build_ellipse(self):
        width, height = (self.r*4)+1, (self.r*4)+1
        a, b = self.r+10, self.r+10
        EPSILON = self.r/3.14
        map_ = [['.' for x in range(width)] for y in range(height)]
        for y in range(height):
            for x in range(width):
                if abs((x-a)**2 + (y-b)**2 - self.r**2) < EPSILON**2:
                    map_[y][x] = '#'
        result = []
        for line in map_:
            result.append(''.join(line))
        for i in range(0, (self.r*4)+1):
            result[i] = fill(result[i])
        for i in range(0, width):
            for g in range(0, height):
                if result[i][g] == '#':
                    mc.setBlock(self.x+g, self.y-1, self.z+i, 46)


def grib(r, h):
    x = mc.player.getPos().x
    y = mc.player.getPos().y
    z = mc.player.getPos().z
    for i in range(0, h):
        stvol = ellipse(r,y+i)
        stvol.build_ellipse()
    chlyapa = ellipse(r*2, y+h, x - r, z - r)
    chlyapa.build_ellipse()

grib(20, 40)