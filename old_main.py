from PIL import Image

# img = Image.open("chicago.jpg");

# w,h = img.size

# pixels = []
# for y in range(h):
#   line = []
#   for x in range(w):  
#     r,g,b = img.getpixel( (x,y) )
#     line.append(str(r))
#     line.append(str(g))
#     line.append(str(b))
#   pixels.append(','.join(line) + "\n")

# f = open("pixels.csv","w")

# for i in range(len(pixels)):
#   f.write(pixels[i])

# f.close()


f = open("pixels.csv")

lines = f.readlines()

f.close()

h = len(lines)
line0 = lines[0].replace("\n","")
line0 = line0.split(',')

pixels_in_line0 = int(len(line0)/3)

img = Image.new( "RGB", (pixels_in_line0,len(lines)))

# print (img.size)
# exit()

for l in range(len(lines)):
  line = lines[l].replace("\n", "").split(',')
  # print (len(line),line)
  # exit()
  pixels = []
  for i in range(0,len(line),3):
    color = line[i:i+3]
    r = int(color[0])
    g = int(color[1])
    b = int(color[2])
    pixel = (r,g,b)
    pixels.append(pixel)
  # print (pixels)  
  # exit()
  
  # print(i,l)
  # exit()
  for p in range(len(pixels)):
    img.putpixel( (p,l), pixels[p])


img.save("new.jpg")








