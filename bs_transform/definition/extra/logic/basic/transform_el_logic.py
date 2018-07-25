import re

from .abs_logic import AbsLogic


class TransformElLogic(AbsLogic):
    def __init__(self):
        super(TransformElLogic, self).__init__(enable_attr=True, enable_string=True)

    def attr_operation(self, parser, tag, attr_key):
        attr_val = tag[attr_key]
        if isinstance(attr_val, list):
            for i, val in enumerate(attr_val):
                tag[attr_key][i] = self.transform_f_h(val)
        else:
            tag[attr_key] = self.transform_f_h(attr_val)

    def string_operation(self, parser, tag, string):
        if re.match(r"\$\{(.*)f:h\((.*)\)(.*)\}", string):
            string.replace_with(self.transform_f_h(string))

    def transform_f_h(self, text):
        return re.sub(r"\$\{(.*)f:h\((.*)\)(.*)\}", r"${\1\2\3}", text)

