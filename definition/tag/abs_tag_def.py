import re

from abc import ABCMeta, abstractmethod


class AbsTagDef(metaclass=ABCMeta):
    def __init__(self):
        pass

    def get_search_name(self):
        if self.search_name(self) is None:
            return None
        return re.compile(self.search_name(self))

    def get_search_attrs(self):
        return self.search_attrs(self)

    def get_search_string(self):
        if self.search_string(self) is None:
            return None
        return re.compile(self.search_string(self))

    @abstractmethod
    def search_name(self):
        raise NotImplementedError

    @abstractmethod
    def search_attrs(self):
        raise NotImplementedError

    @abstractmethod
    def search_string(self):
        raise NotImplementedError

    @abstractmethod
    def operate(self, parser, old_tag):
        raise NotImplementedError
