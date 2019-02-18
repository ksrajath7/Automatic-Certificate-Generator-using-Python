import xlrd

from PIL import Image, ImageDraw, ImageFont

file_location="names.xlsx"

image= Image.open('1.jpg')
draw=ImageDraw.Draw(image)

font_type= ImageFont.truetype('arial.ttf',18)

workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)

for i in range(sheet.nrows):
    name=sheet.cell_value(i,0)
    draw.text(xy=(50,50),text=name,fill="#33ccff",font=font_type)
    image.show()
