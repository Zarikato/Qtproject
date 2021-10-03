from PIL import Image, ImageDraw

class StarDraw():
    def __init__(self, size, stp, color=(0, 0, 0)):
        self.x, self.y = size
        self.stp = stp
        self.color = color

    def set_x(self, xn):
        self.x = xn

    def set_y(self, yn):
        self.y = yn

    def set_stp(self, stpn):
        self.stp = stpn

    def set_color(self, colorn):
        self.color = colorn

    def create_dr(self):
        im = Image.new("RGB", (self.x, self.y), (255, 255, 255))
        drawer = ImageDraw.Draw(im)
        x = self.x
        y = self.y
        for i in range(0, self.y // 2 + self.stp, self.stp):
        
            drawer.line((x // 2, i, x // 2 + i, y // 2), fill=self.color, width=1) # I
            drawer.line((x // 2, i, x // 2 - i, y // 2), fill=self.color, width=1) # II
            drawer.line((x // 2, y - i, x // 2 + i, y // 2), fill=self.color, width=1) # III
            drawer.line((x // 2, y - i, x // 2 - i, y // 2), fill=self.color, width=1) # IV
        im.save('image.jpg')
