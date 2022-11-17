import skimage.io as ski
#import numpy as np
# import matplotlib.pyplot as plt


class ImgHandle:
    '''all own functions required to handle and alter the image'''
    def __init__(self):
        pass



    def place_blocks(self, image_path, coord_list, save_path):
        """places blocks over the naughty bits in an image and saves"""
        img = ski.imread(image_path)
        for block in coord_list:
            if img.shape[2] == 4:
                img[block[1]:block[3], block[0]:block[2]] = (0,0,0,225)
            
            else:
                img[block[1]:block[3], block[0]:block[2]] = (0,0,0)

        save_path_alter = self.add_file_name(save_path, image_path)
        ski.imsave(save_path_alter, img)
        return 


    def add_file_name(self, save_path, image_path):
        """returns the save path with a filename and _sensor to it"""
        # get the original file name
        file_name = image_path.rsplit("\\", 1)[1]
        file_name = file_name.rsplit(".", 1)[0]

        # add file name to the save path
        save_path_alter = save_path + "\\" + file_name + "_sensor.PNG"

        return save_path_alter



#print(type(img))
# img[22:82, 84:134] = (0,0,0,255)

# ski.io.imshow(img)
# plt.show()

# img_shape = img.shape
# ski.io.imsave(r"C:\Users\user\Desktop\01-MACHINE_LEARNING\04-MLC\nudenet\nudes\Nude_1"+"new"+".PNG", img)
