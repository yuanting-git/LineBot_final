# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 01:48:52 2021

@author: restr
"""

from PIL import Image
import datetime

#儀錶板：處理相片合成之func()
#儀錶板：處理相片合成之func()
def resize_image_Square(image,size):
    new_image = image.resize((size,size))
    return new_image

def take_image(image,size,x,y,toImage):
    fromImge = Image.open(image)
    new_image = resize_image_Square(fromImge, size)
    loc = (x,y)  
    toImage.paste(new_image,loc)
    
    
def merge_3(image_1,image_2,image_3,size):
    
    toImage = Image.new('RGBA',(size,size))
    
    half_size = int(size/2)
    
    fromImge = Image.open(image_1)
    new_image = fromImge.resize((size,half_size))
    loc = (0,0)  
    toImage.paste(new_image,loc)
    
    fromImge = Image.open(image_2)
    new_image = resize_image_Square(fromImge, half_size)
    loc = (0,half_size)  
    toImage.paste(new_image,loc)
    
    fromImge = Image.open(image_3)
    new_image = resize_image_Square(fromImge, half_size)
    loc = (half_size,half_size)  
    toImage.paste(new_image,loc)
    
    #合圖檔名
    name = 'three_merged_'+datetime.datetime.today().strftime("%Y-%m-%d")+'.png'
    toImage.save(name) 

def merge_4(image_1,image_2,image_3,image_4,size):
    save_path = './image_map_pic/'
    toImage = Image.new('RGBA',(size,size))
    
    half_size = int(size/2)
    
    take_image(image_1, half_size, 0, 0, toImage)
    take_image(image_2, half_size, half_size, 0, toImage)
    take_image(image_3, half_size, 0, half_size, toImage)
    take_image(image_4, half_size, half_size, half_size, toImage)
    
    #合圖檔名
    name = 'four_merged_'+datetime.datetime.today().strftime("%Y-%m-%d")+'.png'
    toImage.save(save_path+name) 