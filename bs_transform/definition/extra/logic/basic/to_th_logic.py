import re

from .abs_logic import AbsLogic


class ToThLogic(AbsLogic):
    def __init__(self):
        super(ToThLogic, self).__init__(enable_attr=True, enable_string=False)

    def attr_operation(self, parser, tag, attr_key):
        attr_val = tag[attr_key]
        if isinstance(attr_val, list):
            for val in attr_val:
                if re.match(".*\$\{.*\}.*", val) and not attr_key.startswith("th:"):
                    self.execute(tag, attr_key)
                    break
        else:
            if re.match(".*\$\{.*\}.*", attr_val) and not attr_key.startswith("th:"):
                self.execute(tag, attr_key)

    def execute(self, tag, attr_key):
        attr_val = tag.attrs.pop(attr_key)
        tag.attrs["th:" + attr_key] = attr_val
