from enum import Enum

class WORK_STATE(Enum):
    IMAGES_LIST = 0,
    VIDEO = 1,
    WEBCAM = 2

class FOLDER_WRITE(Enum):
    TRAIN = 0,
    NEGATIVE = 1
    TEST = 2

class SelectorZone(Enum):
    NONE = 0
    MOVE_ZONE = 1
    RESIZE_TOP_LEFT_ZONE = 2
    RESIZE_TOP_RIGHT_ZONE = 3
    RESIZE_BOTTOM_LEFT_ZONE = 4
    RESIZE_BOTTOM_RIGHT_ZONE = 5