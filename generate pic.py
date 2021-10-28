from PIL import Image, ImageDraw

# Пустой желтый фон.
im1 = Image.new('RGBA', (50, 50))
draw = ImageDraw.Draw(im1)
draw.ellipse((0, 0, 45, 45), fill='white')
im1.save('wf.png')
im2 = Image.new('RGBA', (50, 50))
draw = ImageDraw.Draw(im2)
draw.ellipse((0, 0, 45, 45), fill='black')
im2.save('bf.png')