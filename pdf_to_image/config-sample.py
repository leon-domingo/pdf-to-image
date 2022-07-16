import logging
import os


class BaseConfig(object):
    @classmethod
    def get(cls, attr_name, default=None):
        return getattr(cls, attr_name, default)

    BASE_PATH = os.path.dirname(__file__)
    DEBUG = os.environ.get("PTI__TEST", "1") == "1"

    LOG_LEVEL = logging.DEBUG
    LOG_FORMAT = "{0} %(asctime)s,%(msecs)03d %(levelname)-5.5s [%(name)s] %(message)s".format(os.environ.get("PTI__WORKER_NAME") or "*")


class ConfigStd(BaseConfig):
    pass


class ConfigTest(BaseConfig):
    pass


Config = ConfigStd
if os.environ.get("PTI__CONFIG") == "TEST":
    Config = ConfigTest
