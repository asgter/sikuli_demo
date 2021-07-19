from jpype import *
from core.initialize_jvm import EnvInitializer

def test_sikuli_able_to_click_exactly_in_100_scaling():
    with EnvInitializer() as env:
        print("start script!")
        Pattern = JClass("org.sikuli.script.Pattern")
        Screen = JClass("org.sikuli.script.Screen")
        pattern_0 = Pattern(env.get_static_file("img_chrome_1920_1080_100.png"))
        pattern_1 = Pattern(env.get_static_file("img_chrome_1920_1080_100_1.png"))
        screen = Screen()
        pattern_list = [pattern_0, pattern_1]
        # 找到匹配区域
        for pattern in pattern_list:
            try:
                pattern_finder = screen.find(pattern)
            except Exception as e:
                print("Pattern: {} 定位失败。".format(pattern.getFilename()))
            else:
                print("定位成功的pattern是：{}".format(pattern.getFilename()))
                break
        print(pattern_finder.x, pattern_finder.y)
        # 高亮匹配区域
        for i in range(2):
            pattern_finder.highlight(1)


def test_sikuli_able_to_click_exactly_in_150_scaling():
    with EnvInitializer():
        print("start script!")
        Pattern = JClass("org.sikuli.script.Pattern")
        Screen = JClass("org.sikuli.script.Screen")
        Location = JClass("org.sikuli.script.Location")
        # pattern = Pattern(env.get_static_file("img_chrome_1920_1080_100.png"))
        pattern = Pattern(env.get_static_file("img_chrome_1920_1080_150.png"))
        screen = Screen()
        # 找到匹配区域
        pattern_finder = screen.find(pattern)
        print(pattern_finder.x, pattern_finder.y)
        # 高亮匹配区域
        for i in range(2):
            pattern_finder.highlight(1)
        # 点击匹配区域
        double_click_res = screen.doubleClick(pattern)
        print(dir(double_click_res))
        # 自定义点击点， 并点击
        location = Location(int(pattern_finder.x / 1.5) + 20, int(pattern_finder.y / 1.5) + 20)
        # screen.click(location)
        screen.doubleClick(location)


if __name__ == "__main__":
    test_sikuli_able_to_click_exactly_in_100_scaling()
    # test_sikuli_able_to_click_exactly_in_150_scaling()
