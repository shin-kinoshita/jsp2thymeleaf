import re

from common.comment.comment_object import CommentObject
from .abs_logic import AbsLogic


class ToThLogic(AbsLogic):
    def __init__(self, comment_level=None):
        super(ToThLogic, self).__init__(
            enable_attr=True,
            enable_string=False,
            comment_level=comment_level
        )

    def attr_operation(self, parser, tag, attr_key):
        attr_val = tag[attr_key]
        if isinstance(attr_val, list):
            for val in attr_val:
                if (re.match(r"(.*)\${(.*)}(.*)", val) or re.match(r"(.*)@{(.*)}(.*)", val)) and not attr_key.startswith("th:"):
                    self.execute(tag, attr_key)
                    break
        else:
            if (re.match(r"(.*)\${(.*)}(.*)", attr_val) or re.match(r"(.*)@{(.*)}(.*)", attr_val)) and not attr_key.startswith("th:"):
                self.execute(tag, attr_key)

    def execute(self, tag, attr_key):
        comment_object = CommentObject(title=self.__class__.__name__, default_level=self.comment_level)
        comment_object.set_old_tag(tag)

        self.replace_attr_key(tag, attr_key, "th:" + attr_key, comment_object)
