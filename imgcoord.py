import glob


class ImgCoord:
    '''all own functions required to get the coords'''
    def __init__(self, path):
        self.path = path


    def get_paths(self):
        """get a list of files (with path) within a directory and return them in a list"""
        return glob.glob(self.path)


    def alter_coords(self, original_coord):
        """alters form of coords to output list [[box1 top right col, top right row, bottom left col,
        bottom left row],  [box2 top right... and so on]"""
        # number of boxes with naughty images
        num_naughtys = len(original_coord)
        new_coord = []
        for box in original_coord:
            new_coord.append(box["box"])
        return new_coord




