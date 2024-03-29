from PIL import Image
import os 
from os import path,mkdir,walk

 
# 先将input  image 填充为正方形
def fill_image(image):
    width, height = image.size
    #选取原图片长、宽中较大值作为新图片的九宫格半径
    new_image_length = width if width > height else height
    #生产新图片【白底】
    new_image = Image.new(image.mode,(new_image_length, new_image_length), color='white')
    #将原图粘贴在新图上，位置为居中
    if width > height:
        new_image.paste(image,(0, int((new_image_length-height) / 2)))
    else:
        new_image.paste(image,(int((new_image_length-width) / 2), 0))
    return new_image
 
# 将图片切割成九宫格
def cut_image(image):
    width, height = image.size
    #一行放3张图
    item_width = int(width / 3)
    box_list = []
    for i in range(0,3):
        for j in range(0,3):
            box = (j*item_width,i*item_width,(j+1)*item_width,(i+1)*item_width)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    return image_list
#保存图片
def save_images(image_list,image_name):
    index = 1
    for image in image_list:
        image.save(f'image\\{image_name}_{str(index)}.png', 'PNG')
        index += 1
   
def open_images():
    root_dir = path.dirname(path.abspath(__file__)) 

    image_list = []
    for root,_,dirs in walk(root_dir,topdown=False):
        if root != root_dir:
            continue
        image_list = [item for item in dirs if item.endswith(".jpg") or item.endswith(".png") or item.endswith(".jpeg")]
    
    if image_list:
        image_dir = f'{root_dir}\\image'
        if not path.exists(image_dir):
            mkdir(image_dir)
    
        for image in image_list:
            try:
                image_name = image.strip().split('.')[0]
            except:
                print('index out of range')
                image_name = 'default'
            image = Image.open(f'{root_dir}\\{image}' )
            image = fill_image(image)
            image_list = cut_image(image)
            save_images(image_list,image_name)

if __name__ == '__main__':
    open_images()

