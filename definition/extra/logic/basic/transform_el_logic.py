import re

from definition.extra.logic.abs_logic import AbsLogic


class TransformElLogic(AbsLogic):
    def __init__(self):
        super(TransformElLogic, self).__init__(enable_attr=True, enable_string=True)

    def attr_operation(self, parser, tag, attr_key):
        attr_val = tag[attr_key]
        tag[attr_key] = self.transform_f_h(attr_val)

    def string_operation(self, parser, tag, string):
        string.replace(string, self.transform_f_h(string))

    def transform_f_h(self, text):
        return re.sub(r"f:h\((.*)\)", r"\1", text)

