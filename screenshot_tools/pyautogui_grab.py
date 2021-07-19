import pyautogui

from utils.wrappers import time_consuming


@time_consuming
def screenshot_by_pyauto(region):
    img = pyautogui.screenshot(region=region)
    img.show()

if __name__ == "__main__":
    region = [0,0,100,100]
    def test_screenshot_by_pyauto(region):
        screenshot_by_pyauto(region)

    test_screenshot_by_pyauto(region)