import re

from bs4 import NavigableString, Comment

from common.comment.comment_object import CommentObject
from .abs_logic import AbsLogic


class ToInlineLogic(AbsLogic):
    def __init__(self, comment_level=None):
        super(ToInlineLogic, self).__init__(
            enable_attr=False,
            enable_string=True,
            comment_level=comment_level
        )
        self.comment_level = comment_level

    def string_operation(self, parser, tag, string):
        if isinstance(string, Comment):
            return
        if re.match(r"(.*)\|(.*)\|(.*)", string, flags=re.DOTALL):
            return
        if re.match(r"(.*)\$\{(.*)\}(.*)", string, flags=re.DOTALL):
            self.execute(string)

    def execute(self, string):
        comment_object = CommentObject(title=self.__class__.__name__, default_level=self.comment_level)
        comment_object.set_old_string(string)

        new_string = NavigableString(re.sub(r"(.*)\$\{(.*)\}(.*)", r"\1[[${\2}]]\3", string, flags=re.DOTALL))
        self.replace_string(string, new_string, comment_object)
