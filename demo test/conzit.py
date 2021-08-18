from PIL import Image, ImageFilter
img = Image.open('con_zit_zang.jpg')
img2 = img.filter(ImageFilter.SHARPEN)
img2.save('con_zit_net.jpg')
img2.show()