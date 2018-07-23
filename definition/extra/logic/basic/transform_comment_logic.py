import re

from definition.extra.logic.abs_logic import AbsLogic


class TransformCommentLogic(AbsLogic):
    def __init__(self):
        super(TransformCommentLogic, self).__init__(enable_attr=False, enable_string=True)

    def string_operation(self, parser, tag, string):
        string.replace_with(self.transform_comment(string))

    def transform_comment(self, text):
        return re.sub(r"(.*)<%--(.*)--%>(.*)", r"\1<!--\2-->\3", text)
