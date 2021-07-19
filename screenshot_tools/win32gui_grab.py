import win32gui

hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def find_hwnd(title):
    win32gui.EnumWindows(get_all_hwnd, 0)

    for hwnd, win_title in hwnd_title.items():
        if win_title.find(title) != -1:
            return hwnd
    else:
        raise NameError("要查找的窗口标题： {}不存在！".format(title))

if __name__ == "__main__":
    def test_find_hwnd_can_find_title():
        print(find_hwnd("照片"))

    def test_find_hwnd_can_raise_error():
        print(find_hwnd("照片1"))


    test_find_hwnd_can_find_title()
    test_find_hwnd_can_raise_error()