from PIL import Image

image = Image.new('RGB',(32,1),(255,255,255))

for i in range(1,32):
    image.putpixel((i-1,0),(i*8-1,i*8-1,i*8-1))

image.save('Palette.png')