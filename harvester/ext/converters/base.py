import abc


class ConverterPluginBase(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, url, conf=None):
        self.url = url
        self.conf = conf or {}

    @abc.abstractmethod
    def convert(self, storage_in, storage_out):
        pass
