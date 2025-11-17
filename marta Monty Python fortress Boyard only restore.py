
from PIL import Image


file = "password_hidden_team2_UAI324.png"
im=Image.open(file)
pix=im.load()

im_new = Image.new( im.mode, im.size)
pix_new = im_new.load()

w=im.size[0]
h=im.size[1]

for i in range(w):
  for j in range(h):
    if pix[i,j][0]  != 255:
        pix_new[i,j]= (0,0,0)
    else:
        pix_new[i,j]= pix[i,j]

im.close()
im_new.save("password_recoveded_team2.jpg")
im_new.close()




