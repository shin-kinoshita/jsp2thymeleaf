from abc import ABCMeta, abstractmethod


class AbsLogic(metaclass=ABCMeta):
    def __init__(self, enable_attr=False, enable_string=False):
        self.enable_attr = enable_attr
        self.enable_string = enable_string

    def attr_operation(self, parser, tag, attr_key):
        raise NotImplementedError

    def string_operation(self, parser, tag, string):
        raise NotImplementedError
