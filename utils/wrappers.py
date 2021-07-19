import re
import time

from utils.config_parser import load_config_value


def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner


def check_file_and_screen_are_the_same_resolution(func):
    screen_resolution = load_config_value("screen_resolution")

    # x, y = screen_resolution.split("/")
    def inner(filename):
        if filename.find(screen_resolution) != -1:
            return func(filename)
        else:
            img_resolution = re.search("\d{4}_\d{4}", filename).group()
            raise AssertionError("图片分辨率{}与屏幕分辨率{}不一致，无法完成图片匹配！".format(
                img_resolution, screen_resolution
            )
            )

    return inner


def check_file_and_screen_are_the_same_scale(func):
    screen_scale = load_config_value("screen_scale")

    def inner(filename):
        img_scale = re.search("\d{4}_\d{4}_(\d{3})", filename).group(1)
        if screen_scale != img_scale:
            return func(filename)
        else:

            raise AssertionError("图片缩放{}与屏幕缩放{}不一致，无法完成图片匹配！".format(
                img_scale, screen_scale
            )
            )

    return inner


def time_consuming(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        cost_time = end_time - start_time
        print("{}消耗时间为{}".format(func.__name__, cost_time))
        return cost_time

    return wrapper


if __name__ == "__main__":
    def test_resolution():
        screen_resolution = load_config_value("screen_resolution")
        x, y = map(int, screen_resolution.split("_"))
        print("screen_x: {}, screen_y: {}".format(x, y))
        filename = r"D:\projects\sikuli_demo\imgs\img_chrome_1920_1080_100.png"
        img_resolution = re.search("\d{4}_\d{4}", filename).group()
        print(f"screen_resolution: {screen_resolution}, img_resolution: {img_resolution}")


    def test_scale():
        screen_scale = load_config_value("screen_scale")
        filename = r"D:\projects\sikuli_demo\imgs\img_chrome_1920_1080_100.png"
        img_scale = re.search("\d{4}_\d{4}_(\d{3})", filename).group(1)
        print(f"screen_scale: {screen_scale}, img_resolution: {img_scale}")


    test_resolution()
    test_scale()
