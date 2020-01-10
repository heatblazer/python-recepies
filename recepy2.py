
class Screen(object):

    def __init__(self, w, h):

        def private_fillScreen(data, w, h):
            size = w * h
            for i in range (0, size):
                data.append('X')

        self.screen = list()
        # use private method
        private_fillScreen(self.screen, w, h)

    
    def blit(self):
        print (self.screen)


if __name__ == "__main__":
    scr = Screen(10, 10)
    scr.blit()