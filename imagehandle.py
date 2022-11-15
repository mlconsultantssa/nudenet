import skimage as ski
import numpy as np
import matplotlib.pyplot as plt


class ImgHandle:
    '''all own functions required to handle and alter the image'''
    def __init__(self):
        pass



    def place_blocks(self, image_path, coord_list, save_path):
        """places blocks over the naughty bits in an image and saves"""
        img = ski.io.imread(image_path)
        for block in coord_list:
            img[block[1]:block[3], block[0]:block[2]] = (0,0,0,225)

        ski.io.imsave(save_path, img)
        return 




#print(type(img))
# img[22:82, 84:134] = (0,0,0,255)

# ski.io.imshow(img)
# plt.show()

# img_shape = img.shape
# ski.io.imsave(r"C:\Users\user\Desktop\01-MACHINE_LEARNING\04-MLC\nudenet\nudes\Nude_1"+"new"+".PNG", img)
