from PIL import Image, ImageFilter
img = Image.open('chuhuan.jpg')
img1 = img.filter(ImageFilter.EMBOSS)
img2 = img1.filter(ImageFilter.SMOOTH)
img2.save('chuhuankhacnoi2.jpg')
img2.show()