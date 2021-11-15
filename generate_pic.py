from PIL import Image, ImageDraw


def generate_pictures():
    colors = open('settings.txt', mode='r')

    im1 = Image.new('RGBA', (50, 50))
    draw = ImageDraw.Draw(im1)
    draw.ellipse((0, 0, 45, 45), fill=tuple([int(i) for i in colors.readline().rstrip().split()]))
    im1.save('media/wf.png')
    im2 = Image.new('RGBA', (50, 50))
    draw = ImageDraw.Draw(im2)
    draw.ellipse((0, 0, 45, 45), fill=tuple([int(i) for i in colors.readline().rstrip().split()]))
    im2.save('media/bf.png')
