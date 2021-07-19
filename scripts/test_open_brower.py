import time

from jpype import *
from core.initialize_jvm import EnvInitializer


def test_ifly_site_can_open():
    with EnvInitializer() as env:
        Pattern = JClass("org.sikuli.script.Pattern")
        Screen = JClass("org.sikuli.script.Screen")
        pattern = Pattern(env.get_static_file("img_chrome_1920_1080_100_1.png"))
        screen = Screen()
        # 找到匹配区域
        pattern_finder = screen.find(pattern)
        print(pattern_finder)
        # 点击匹配区域
        screen.doubleClick(pattern)


def test_login_ifly_site():
    test_ifly_site_can_open()
    with EnvInitializer() as env:
        SikuliEvent = JClass("org.sikuli.script.SikuliEvent")
        Pattern = JClass("org.sikuli.script.Pattern")
        Screen = JClass("org.sikuli.script.Screen")
        Key = JClass("org.sikuli.script.Key")
        pattern = Pattern(env.get_static_file("login_button_in_portal_web.png"))
        screen = Screen()
        event = SikuliEvent()
        # 等待匹配区域
        for _ in range(5):
            if not screen.exists(pattern.exact()):
                time.sleep(0.5)
        # 点击匹配区域
        screen.click(pattern.targetOffset(20, 0))


def test_search_in_baidu():
    with EnvInitializer() as env:
        Pattern = JClass("org.sikuli.script.Pattern")
        Screen = JClass("org.sikuli.script.Screen")
        Key = JClass('org.sikuli.script.Key')
        screen = Screen()
        key = Key()
        # 打开chrome浏览器
        pattern_chrome = Pattern(env.get_static_file("img_chrome_ico_1920_1080_100.png"))
        if not screen.exists(r"D:\projects\sikuli_demo\imgs\img_chrome_ico_1920_1080_100.png", 2):
            print("未检测到chrome浏览器！")
        screen.doubleClick(pattern_chrome.similar(0.8))
        # 最大化浏览器
        pattern_maxmize = Pattern(env.get_static_file("img_chrome_maximize.png"))
        if not screen.exists(pattern_maxmize.exact(), 2):
            print("未检测到chrome最大化按钮！")
        screen.find(pattern_maxmize.similar(0.8))
        screen.doubleClick(pattern_maxmize.similar(0.8))
        # 打开bing搜索页面
        pattern_bing_search_button = Pattern(env.get_static_file("img_bing_search_button.png"))
        if not screen.exists(pattern_bing_search_button.exact(), 2):
            print("未检测到bing按钮！")
        screen.doubleClick(pattern_bing_search_button)
        # 输入搜索关键字
        pattern_bing_search_type = Pattern(env.get_static_file("img_bing_search_type.png"))
        if not screen.exists(pattern_bing_search_type.exact(), 2):
            print("未检测到bing输入框！")
        screen.doubleClick(pattern_bing_search_type.targetOffset(0, 10))
        screen.type("java")
        screen.type(key.ENTER)
        screen.type(key.ENTER)


if __name__ == "__main__":
    # test_brower_can_open()
    test_login_ifly_site()
    # test_search_in_baidu()
