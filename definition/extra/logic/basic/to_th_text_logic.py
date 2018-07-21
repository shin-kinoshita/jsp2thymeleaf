import re

from bs4 import Tag

from definition.extra.logic.abs_logic import AbsLogic


class ToThTextLogic(AbsLogic):
    def __init__(self):
        super(ToThTextLogic, self).__init__(enable_attr=False, enable_string=True)

    def string_operation(self, parser, tag, string):
        self.execute(parser, tag, string)

    def execute(self, parser, tag, string):
        if not re.match("\$\{.*\}", string):
            return
        new_tag = Tag(parser, name="div", attrs=[("th:text", string)])
        string.replace_with(new_tag)
