import csv

from PIL import Image, ImageDraw, ImageFont

width = 512
height = 512
font = ImageFont.truetype("arial.ttf", size=20)


with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    i = 0
    for [message] in reader:
        i += 1
        img = Image.new('RGB', (width, height), color='blue')

        imgDraw = ImageDraw.Draw(img)

        textWidth, textHeight = imgDraw.textsize(message, font=font)
        xText = (width - textWidth) / 2
        yText = (height - textHeight) / 2

        imgDraw.text((xText, yText), message, font=font, fill=(255, 255, 0))

        img.save(f'result{i}.png')
