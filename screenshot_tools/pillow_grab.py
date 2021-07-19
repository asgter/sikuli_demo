import time
import numpy as np
from PIL import ImageGrab

from utils.wrappers import time_consuming


@time_consuming
def screenshot_by_img_grab(bbox):
    img = ImageGrab.grab(bbox=bbox)
    # img.show()
    # img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)

if __name__ == "__main__":
    bbox = (100, 161, 1141, 610)
    screenshot_by_img_grab(bbox)
