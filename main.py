from PIL import Image


#  open file and create list of lines 
f = open("pixels.csv")
lines = f.readlines()

height = len(lines)

for i in range(len(lines)):
  lines[i] = lines[i].replace("\n", "").split(",")

width = int(len(lines[0])/3)

# print (len(lines[0]))

# exit()

img = Image.new( "RGB" , (width, height))

# for i in range(0,30,3):
#   print (i)

# exit()

print (img.size)

for y in range(height):
  for x in range(0, len(lines[0]), 3):
    these_values = lines[y][x:x+3]
    
    # print (these_values)

    these_values = map(lambda x: int(x), these_values) 
    
    # print (tuple(these_values))

    # exit()

    # print (list(these_values))

    # exit()
    # for i in range(len(these_values)):
    #   these_values[i] = int(these_values[i])

    color = tuple(these_values)

    # print (color)

    # print ((x//3,y), tuple(these_values))

    img.putpixel((x//3,y), color)


img.save("pic.jpg")


























# from PIL import Image

# img = Image.open("chicago.jpg");

# w,h = img.size

# new = Image.new( "RGB", img.size)

# for y in range(h):

#   for x in range(w):  
    

#     if (x % 2 == 0):
#       r,g,b = img.getpixel( (x,y) )
#       g = int(g/2) + 80
#       if (b < 128):
#         b = int(b/2)
#       if (r % 2 == 0):
#         r = int(r/2)
#     else:
#       r,g,b = img.getpixel( (w-1-x,y) )

        
#     new.putpixel ((x,y), (b, r, g))

# new.save("scrambled.jpg")
