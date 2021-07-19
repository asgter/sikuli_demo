from jpype import *

def test_can_load_sikuliapi_of_pattrn():
    sikuliapi_abs_path = r"D:\projects\sikuli_demo\lib\sikulixapi-2.0.0.jar"
    startJVM(getDefaultJVMPath(), "-ea", r"-Djava.class.path={}".format(sikuliapi_abs_path))
    Pattern = JClass("org.sikuli.script.Pattern")
    shutdownJVM()

if __name__ == "__main__":
    test_can_load_sikuliapi_of_pattrn()