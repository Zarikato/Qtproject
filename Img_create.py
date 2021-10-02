from PIL import Image, ImageDraw


def create_dr(x, stp):
    im = Image.new("RGB", (x, x), (255, 255, 255))
    drawer = ImageDraw.Draw(im)
    for i in range(0, x // 2 + stp, stp):
        
        drawer.line((x // 2, i, x // 2 + i, x // 2), fill=(0, 0, 0), width=1) # I
        drawer.line((x // 2, i, x // 2 - i, x // 2), fill=(0, 0, 0), width=1) # II
        drawer.line((x // 2, x - i, x // 2 + i, x // 2), fill=(0, 0, 0), width=1) # III
        drawer.line((x // 2, x - i, x // 2 - i, x // 2), fill=(0, 0, 0), width=1) # IV
        drawer.line((0, x // 2, x, x // 2), fill=(0, 0, 0), width=1) # X0
        drawer.line((x // 2, 0, x // 2, x), fill=(0, 0, 0), width=1) # Y0
    im.save('image.jpg')


