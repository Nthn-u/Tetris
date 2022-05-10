class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, notSelf): #operator overloading
        return Coordinates(self.x + notSelf.x, self.y + notSelf.y)

def formatMilliseconds(ms):
    return f"{int((ms/(1000*60)))}:{int((ms/1000)%60)}:{int(ms%1000)}"

