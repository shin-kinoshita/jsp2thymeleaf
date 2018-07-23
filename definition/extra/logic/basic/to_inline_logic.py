import re

from bs4 import Tag, NavigableString

from definition.extra.logic.abs_logic import AbsLogic


class ToInlineLogic(AbsLogic):
    def __init__(self):
        super(ToInlineLogic, self).__init__(enable_attr=False, enable_string=True)

    def string_operation(self, parser, tag, string):
        if not re.match(".*\$\{.*\}.*", string):
            return
        self.execute(string)

    def execute(self, string):
        new_string = re.sub(r"\$\{(.*)\}", r"[[${\1}]]!", string)
        string.replace_with(NavigableString(new_string))
