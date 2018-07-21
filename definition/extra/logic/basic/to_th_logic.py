import re

from definition.extra.logic.abs_logic import AbsLogic


class ToThLogic(AbsLogic):
    def __init__(self):
        super(ToThLogic, self).__init__(enable_attr=True, enable_string=False)

    def attr_operation(self, parser, tag, attr_key):
        if not re.match("\$\{.*\}", tag[attr_key]) or attr_key.startswith("th:"):
            return
        self.execute(tag, attr_key)

    def execute(self, tag, attr_key):
        attr_val = tag.attrs.pop(attr_key)
        tag.attrs["th:" + attr_key] = attr_val
