import re

from bs4 import NavigableString

from .abs_logic import AbsLogic


class ToInlineLogic(AbsLogic):
    def __init__(self):
        super(ToInlineLogic, self).__init__(enable_attr=False, enable_string=True)

    def string_operation(self, parser, tag, string):
        if re.match(r"(.*)\$\{(.*)\}(.*)", string, flags=re.DOTALL):
            self.execute(string)

    def execute(self, string):
        new_string = re.sub(r"(.*)\$\{(.*)\}(.*)", r"\1[[${\2}]]\3", string, flags=re.DOTALL)
        string.replace_with(NavigableString(new_string))
