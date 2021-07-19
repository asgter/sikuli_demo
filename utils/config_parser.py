import configparser
import os

import settings

CONFIG_PATH = r"..\config.ini"
if not os.path.exists(CONFIG_PATH):
    raise FileNotFoundError("没有找到对应的配置文件，请检查配置文件地址是否正确：{}".format(CONFIG_PATH))

SECTION = "DEBUG" if settings.DEBUG else "PROD"

def load_config_value(name):
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH, encoding="utf-8")
    try:
        value = config[SECTION][name]
    except KeyError as e:
        return None
    print("config_name: {}, config_value: {}".format(name, value))
    return value
