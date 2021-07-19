import os

import jpype

from settings import PROJECT_PATH
from utils.config_parser import load_config_value
from utils.wrappers import singleton, check_file_and_screen_are_the_same_resolution, \
    check_file_and_screen_are_the_same_scale


class EnvInitializer:
    def __init__(self):
        self.__load_sikuliapi_path()
        self.__load_static_path()

    def __load_sikuliapi_path(self):
        sikuliapi_relative_path = load_config_value("sikuliapi_path")
        self.__sikuliapi_path = os.path.join(PROJECT_PATH, sikuliapi_relative_path)

    def __load_static_path(self):
        static_relative_path = load_config_value("static_path")
        self.__static_path = os.path.join(PROJECT_PATH, static_relative_path)

    def __enter__(self):
        if not jpype.isJVMStarted():
            print("starting JVM: {}".format(jpype.getDefaultJVMPath()))
            # print(type(self.__sikuliapi_path), self.__sikuliapi_path)
            jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", r"-Djava.class.path={}".format(self.__sikuliapi_path))
        return self

    def __exit__(self, type, value, trace):
        if not jpype.isJVMStarted():
            print("exiting JVM")
            jpype.shutdownJVM()

    @check_file_and_screen_are_the_same_resolution
    @check_file_and_screen_are_the_same_scale
    def get_static_file(self, filename):
        full_file_path = os.path.join(self.__static_path, filename)
        if os.path.exists(full_file_path):
            return full_file_path
        else:
            raise FileNotFoundError("文件不存在：{}".format(full_file_path))


if __name__ == "__main__":
    with EnvInitializer():
        pass
