import glob


class ImgCoord:
    '''all own functions required to get the coords'''
    def __init__(self, path):
        self.path = path


    def get_paths(self):
        """get a list of files (with path) within a directory and return them in a list"""
        return glob.glob(self.path)


    def alter_coords(self, original_coord, nono_parts):
        """alters form of coords to output list [[box1 top right col, top right row, bottom left col,
        bottom left row],  [box2 top right... and so on]"""
        # number of boxes with naughty images
        new_coord = []
        nono_coord = self.choose_nonos(original_coord, nono_parts)
        for box in nono_coord:
            new_coord.append(box)
        return new_coord

    def choose_nonos(self, original_coord, nono_parts):
        """only selects boxes for the categories of nonos that we choose"""
        return [i["box"] for i in original_coord if i["label"] in nono_parts]


