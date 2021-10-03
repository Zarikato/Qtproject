from PIL import Image, ImageDraw

class StarDraw():
    def __init__(self, size, stp, color=(0, 0, 0)):
        self.x, self.y = size
        self.stp = stp
        self.color = color

    def set_x(self, xn=1000):
        if xn == '' or xn == 0:
            xn == 1000
        else:
            self.x = xn

    def set_y(self, yn=1000):
        if yn == '' or yn == 0:
            yn == 1000
        else:
            self.y = yn

    def set_stp(self, stpn):
        self.stp = stpn

    def set_color(self, colorn):
        self.color = colorn

    def create_dr(self):
        im = Image.new("RGB", (self.x, self.y), (255, 255, 255))
        drawer = ImageDraw.Draw(im)
        colore = self.color
        x = self.x
        y = self.y
        for i in range(0, self.y // 2 + self.stp, self.stp):
        
            drawer.line((x // 2, i, x // 2 + i, y // 2), fill=colore, width=1) # I
            drawer.line((x // 2, i, x // 2 - i, y // 2), fill=colore, width=1) # II
            drawer.line((x // 2, y - i, x // 2 + i, y // 2), fill=colore, width=1) # III
            drawer.line((x // 2, y - i, x // 2 - i, y // 2), fill=colore, width=1) # IV
        im.save('image.jpg')
