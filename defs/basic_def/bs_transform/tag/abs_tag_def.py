import re

from abc import ABCMeta, abstractmethod


class AbsTagDef(metaclass=ABCMeta):
    def __init__(self):
        pass

    def get_search_name(self):
        if self.search_name() is None:
            return None
        return re.compile(self.search_name())

    def get_search_attrs(self):
        return self.search_attrs()

    def get_search_string(self):
        if self.search_string() is None:
            return None
        return re.compile(self.search_string())

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

    def replace(self, old_tag, new_tag, comment_object):
        old_tag.replace_with(new_tag)
        if comment_object is not None:
            for comment in comment_object:
                new_tag.insert_before(comment)
