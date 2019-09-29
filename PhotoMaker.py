from PIL import Image
import easygui	as egui

#filename = egui.enterbox("What is the image name?")

	

filename  = egui.fileopenbox("Please choose an image file", " ", '*.png') 

try:
	img = Image.open(filename)
except	IOError:
	print("NOT FOUND")

width, height = img.size

#egui.msgbox(str(width)+" "+str(height))
#img = img.transpose(Image.ROTATE_180)
#img.save("rotated.png")

pass_size = 413, 413
a4_size = 2480, 3508

img.thumbnail(pass_size, Image.ANTIALIAS)

#img.save("passport.png")

img = img.transpose(Image.ROTATE_90)

images_per_row = 6
number_of_rows = 8
	
padding = 2

new_im = Image.new("RGB", a4_size)

i,j=0,0

rw=0
for k in range(8):
	for j in range(32):
        	y_cord = (j//images_per_row)*413+rw
        	new_im.paste(img, (i, y_cord))
        	i=(i+413)+padding
	rw+=413

new_im.save("out.jpg", "JPEG", quality= 80, optimize = True, progressive = True)


