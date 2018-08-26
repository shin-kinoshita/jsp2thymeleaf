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

    def attr_operation(self):
        if isinstance(self.attr_val, list):
            for val in self.attr_val:
                if (re.match(r"(.*)\${(.*)}(.*)", val) or re.match(r"(.*)@{(.*)}(.*)", val)) and \
                        not self.attr_key.startswith("th:"):
                    self.execute()
                    break
        else:
            if (re.match(r"(.*)\${(.*)}(.*)", self.attr_val) or re.match(r"(.*)@{(.*)}(.*)", self.attr_val)) and \
                    not self.attr_key.startswith("th:"):
                self.execute()

    def execute(self):
        comment_object = CommentObject(title=self.__class__.__name__, default_level=self.comment_level)
        comment_object.set_old_tag(self.tag)

        self.replace_attr_key("th:" + self.attr_key, comment_object)
