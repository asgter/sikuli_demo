## 项目结构
+ core
    + initialize_jvm: 启动jvm，以便使用java对象
+ imgs: 静态资源
+ lib: sikuliapi的jar包
+ screenshot_tools: 多种方式的截图工具
+ scripts: sikuliapi的各类测试脚本
+ utils: 工具包

## Python调用sikuliapi流程

1. 导入依赖
   ```shell
   pip install -r requirements.txt
   ```
2. 下载sikuliapi的jar包
   
   + api下载官网：http://www.sikuli.org/download.html
   + 找到sikulixapi-2.0.0.jar，并下载

3. 编写脚本
   test_sikuli_runnable.py
   ```python
   from jpype import *
   
   startJVM(getDefaultJVMPath(),"-ea", "-Djava.class.path=.\sikulixapi.jar")  # 这里填入jar包的位置
   
   java.lang.System.out.println("helloworld")
   
   Screen = JClass("org.sikuli.script.Screen")
   
   screen = Screen()
   
   screen.click("D:/pic/news.png")  # 这里需要先截图并保存到本地
   
   shutdownJVM()
   ```
