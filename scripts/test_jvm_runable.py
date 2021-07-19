from jpype import *

def test_jvm_runable():
    sikuliapi_abs_path = r"D:\projects\sikuli_demo\lib\sikulixapi-2.0.0.jar"
    startJVM(getDefaultJVMPath(), "-ea", r"-Djava.class.path={}".format(sikuliapi_abs_path))
    java.lang.System.out.println("hello sikuli")
    shutdownJVM()

if __name__ == "__main__":
    test_jvm_runable()