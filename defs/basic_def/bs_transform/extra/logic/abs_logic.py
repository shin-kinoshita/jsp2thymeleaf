from abc import ABCMeta

from common.comment.comment_level import CommentLevel


class AbsLogic(metaclass=ABCMeta):
    def __init__(self, enable_attr=False, enable_string=False, comment_level=None):
        self.enable_attr = enable_attr
        self.enable_string = enable_string
        self.comment_level = comment_level
        if self.comment_level is None:
            self.comment_level = CommentLevel.NORMAL

        self.parser = None
        self.tag = None
        self.attr_key = None
        self.attr_val = None
        self.string = None

    def call_attr_operation(self, parser, tag, attr_key):
        self.parser = parser
        self.tag = tag
        self.attr_key = attr_key
        self.attr_val = tag[attr_key]

        self.attr_operation()

    def call_string_operation(self, parser, tag, string):
        self.parser = parser
        self.tag = tag
        self.string = string

        self.string_operation()

    def attr_operation(self):
        raise NotImplementedError

    def string_operation(self):
        raise NotImplementedError

    def replace_attr_key(self, new_attr_key, comment_object):
        self.tag[new_attr_key] = self.tag.attrs.pop(self.attr_key)
        if comment_object is not None:
            for comment in comment_object:
                self.tag.insert_before(comment)

    def replace_attr_val(self, new_attr_val, comment_object):
        self.tag[self.attr_key] = new_attr_val
        if comment_object is not None:
            for comment in comment_object:
                self.tag.insert_before(comment)

    def replace_string(self, new_string, comment_object):
        self.string.replace_with(new_string)
        if comment_object is not None:
            for comment in comment_object:
                new_string.insert_before(comment)
