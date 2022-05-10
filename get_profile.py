import instaloader
import os
from PIL import Image, ImageDraw, ImageFont
import random

from send_mail import send_mail


def get_posts(usr_name):
    """ Gets Profile Data of a User"""
    root=instaloader.Instaloader()
    
    root.download_profile(usr_name)
    return usr_name

def get_file_names(username):
    """ Returns all photo names of the user"""
    # os.chdir(username)
    # os.mkdir('images')
    files = os.listdir(os.path.join(os.getcwd(),username))
    photo_list :list = []
    for file in files:
        print(file, file[-3:])
        if file[-3:] == 'jpg':
            photo_list.append(file)
    
    return photo_list

def make_collage(photo_list, username):
    
    image1 = Image.open(username+'/'+random.choice(photo_list))
    image2 = Image.open(username+'/'+random.choice(photo_list))
    image3 = Image.open(username+'/'+random.choice(photo_list))
    image1 = image1.resize((300, 400))
    image2 = image2.resize((100, 500))
    image3 = image3.resize((200, 600))

    image1_size = image1.size
    image2_size = image2.size
    image3_size = image3.size 
    new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(image1_size[0],0))
    new_image.paste(image3,(image2_size[0],0))
    
    new_image.save(f"images/{username}_birthday.jpg","JPEG")
    # new_image.show()
    return f"images/{username}_birthday.jpg"
    # add text to image
def add_text(username, path):
    """ Adds Happy Birthday to the photos"""
    img = Image.open(path)
    I1 = ImageDraw.Draw(img)
    image_font = ImageFont.truetype('Heart Blues.ttf',45)
    I1.text((200, 320),f'Happy Birthday {username}',font=image_font, fill=(255,255,255))
    img.show()
    img.save(f'output/{username}_birthday_final.jpg')
    return f"output/{username}_birthday_final.jpg"



if __name__ == "__main__":
     usr_name=str(input("enter username :: "))
     get_posts(usr_name)

     photo_list = get_file_names(usr_name)
     path_name = make_collage(photo_list,usr_name)
     location  = add_text(usr_name, path_name)
     send_mail_addr = input("Enter birthday guy/woman's email address :")
     send_mail(send_mail_addr,location)