# C sharp like getter/setter

class Screen(object):

    def __init__(self):
        pass

    def getter_setter_y(self, y, get=True):
        """get and set a true private variable"""
        if get is False:
            Screen.getter_setter_y.value = y
        else:
            return Screen.getter_setter_y.value


    def getter_setter_x(self, x, get=True):
        """get and set a true private variable"""
        if get is True:
            Screen.getter_setter_x.value = x
        else:
            return Screen.getter_setter_x.value

    def plot(self, x, y, color):
        pass
    
    def blit(self):
        pass
                

if __name__ == "__main__":
    scr = Screen()
    scr.getter_setter_x(100)
    value1 = scr.getter_setter_x(0, get=False)
    print (value1)
    scr.getter_setter_x(200)
    value2 =  scr.getter_setter_x(0, get=False)
    print (value2)
    scr.getter_setter_x(300)
    value3 =  scr.getter_setter_x(0, get=False)
    print (value3)
