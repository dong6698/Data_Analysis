from PIL import Image
from PIL import ImageFilter

'''
打印图片大小 格式
'''
# img = Image.open('959.jpg')
# print(img.size)
# print(img.format)
# img.show()

'''
剪切图片指定大小
'''
# area = (150, 150, 1150, 800)
# cropped_img = img.crop(area)
# cropped_img.show()

'''
合成图片 复制图片1 到 图片2
'''
# cats_img = Image.open('cats.jpg')
# area = (100, 100, cats_img.width+100, cats_img.height+100)
# img.paste(cats_img, area)
# img.show()

'''
RGB分割图片
'''
# red, green, blue = img.split()
# red.show()
# green.show()
# blue.show()
# red, green, blue = img.split()
# new_img = Image.merge('RGB', (green, red, blue))
# new_img.show()

'''
重设图片大小 镜像 以及翻转
'''
# cats = Image.open('cats.jpg')
# square_cats = cats.resize((300, 300))
# flip_cats = cats.transpose(Image.FLIP_LEFT_RIGHT)
# rotate_cats = cats.transpose(Image.ROTATE_90)
# cats.show()
# square_cats.show()
# flip_cats.show()
# rotate_cats.show()

'''
L 代表黑白
'''
# cats = Image.open('cats.jpg')
# black_white = cats.convert('L')
# # black_white.show()

'''
使图片变得模糊
'''
# blur = cats.filter(ImageFilter.BLUR)
# blur.show()

'''
使图片变得更清楚?
'''
# detail = cats.filter(ImageFilter.DETAIL)
# detail.show()

'''
勾画黑白轮廓
'''
# edges = cats.filter(ImageFilter.FIND_EDGES)
# edges.show()
