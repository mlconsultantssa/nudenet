# Import module
# from NudeNet.nudenet import NudeClassifier

# # initialize classifier (downloads the checkpoint file automatically the first time)
# classifier = NudeClassifier()

# # Classify single image
# print(classifier.classify(r"C:\Users\user\Desktop\01-MACHINE_LEARNING\04-MLC\nudenet\Nude_1.PNG"))
# # Returns {'path_to_image_1': {'safe': PROBABILITY, 'unsafe': PROBABILITY}}
# # Classify multiple images (batch prediction)
# # batch_size is optional; defaults to 4
# #classifier.classify(['path_to_image_1', 'path_to_image_2'], batch_size=BATCH_SIZE)
# # Returns {'path_to_image_1': {'safe': PROBABILITY, 'unsafe': PROBABILITY},
# #          'path_to_image_2': {'safe': PROBABILITY, 'unsafe': PROBABILITY}}

# # Classify video
# # batch_size is optional; defaults to 4
# #classifier.classify_video('path_to_video', batch_size=BATCH_SIZE)
# # Returns {"metadata": {"fps": FPS, "video_length": TOTAL_N_FRAMES, "video_path": 'path_to_video'},
# #          "preds": {frame_i: {'safe': PROBABILITY, 'unsafe': PROBABILITY}, ....}}

###

# Import module
from NudeNet.nudenet import NudeDetector
#import numpy as np
#import matplotlib.pyplot as plt
from imgcoord import ImgCoord
from imagehandle import ImgHandle
# path to the folder with images to use
path = r"C:\Users\user\Desktop\nudes\*.*"
save_path = r"C:\Users\user\Desktop\nudes_no_more"
nono_parts = ["EXPOSED_ANUS", "EXPOSED_BUTTOCKS", "EXPOSED_BREAST_F", "EXPOSED_GENITALIA_F", "EXPOSED_GENITALIA_M"] #options: EXPOSED_ANUS EXPOSED_ARMPITS COVERED_BELLY EXPOSED_BELLY COVERED_BUTTOCKS EXPOSED_BUTTOCKS FACE_F FACE_M COVERED_FEET EXPOSED_FEET COVERED_BREAST_F EXPOSED_BREAST_F COVERED_GENITALIA_F EXPOSED_GENITALIA_F EXPOSED_BREAST_M EXPOSED_GENITALIA_M

# initialize class to with functions to get image coords, passing 
img_coord = ImgCoord(path)
# initialize detector (downloads the checkpoint file automatically the first time)
detector = NudeDetector() # detector = NudeDetector('base') for the "base" version of detector.
# initialize class to with functions to alter image 
img_handle = ImgHandle()

# step through images in folder and get the coords of the naughty bits
path_list = img_coord.get_paths()



for image_path in path_list:
    # first we get the coords
    naughty_coords_original = detector.detect(image_path)# Detect single image
    if len(naughty_coords_original)> 0:
        coord_list = img_coord.alter_coords(naughty_coords_original, nono_parts)
        # now we alter the image
        img_handle.place_blocks(image_path,coord_list, save_path)


#print(naughty_coords)

# # Load an image
# original_img = plt.imread(images_paths[0])
# # Visualizing the image

# plt.imshow(original_img)



# fast mode is ~3x faster compared to default mode with slightly lower accuracy.
#detector.detect('path_to_image', mode='fast')
# Returns [{'box': LIST_OF_COORDINATES, 'score': PROBABILITY, 'label': LABEL}, ...]

# Detect video
# batch_size is optional; defaults to 2
# show_progress is optional; defaults to True
#detector.detect_video('path_to_video', batch_size=BATCH_SIZE, show_progress=BOOLEAN)
# fast mode is ~3x faster compared to default mode with slightly lower accuracy.
#detector.detect_video('path_to_video', batch_size=BATCH_SIZE, show_progress=BOOLEAN, mode='fast')
# Returns {"metadata": {"fps": FPS, "video_length": TOTAL_N_FRAMES, "video_path": 'path_to_video'},
#          "preds": {frame_i: {'box': LIST_OF_COORDINATES, 'score': PROBABILITY, 'label': LABEL}, ...], ....}}
