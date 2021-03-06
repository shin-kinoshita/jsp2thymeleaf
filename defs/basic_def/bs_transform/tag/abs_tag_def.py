import re

from abc import ABCMeta, abstractmethod

from common.comment.comment_level import CommentLevel


class AbsTagDef(metaclass=ABCMeta):
    def __init__(self, comment_level=None):
        self.comment_level = comment_level

        if self.comment_level is None:
            self.comment_level = CommentLevel.NORMAL

    def get_search_name(self):
        if self.search_name() is None:
            return None
        return re.compile(self.search_name())

    @abstractmethod
    def search_name(self):
        raise NotImplementedError

    @abstractmethod
    def operate(self, parser, old_tag):
        raise NotImplementedError

    def replace_tag(self, old_tag, new_tag, comment_object):
        old_tag.replace_with(new_tag)
        if comment_object is not None:
            for comment in comment_object:
                new_tag.insert_before(comment)
