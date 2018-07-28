import re

from bs4 import NavigableString

from .abs_logic import AbsLogic


class EditLinkingLiteralLogic(AbsLogic):
    def __init__(self):
        super(EditLinkingLiteralLogic, self).__init__(enable_attr=True, enable_string=False)

    def attr_operation(self, parser, tag, attr_key):
        attr_val = tag[attr_key]
        if isinstance(attr_val, list):
            new_attr_val = list()
            for val in attr_val:
                if re.match(r"(.*)\|(.*)\|(.*)", val, flags=re.DOTALL):
                    new_attr_val.append(val)
                elif re.match(r"(.*)\${(.*)}(.*)", val, flags=re.DOTALL):
                    new_val = self.transform_string(val)
                    new_attr_val.append(new_val)
                else:
                    new_attr_val.append(val)
            tag[attr_key] = new_attr_val
        else:
            if re.match(r"(.*)\|(.*)\|(.*)", attr_val, flags=re.DOTALL):
                return
            if re.match(r"(.*)\${(.*)}(.*)", attr_val, flags=re.DOTALL):
                new_attr_val = self.transform_string(attr_val)
                tag[attr_key] = new_attr_val

    def transform_string(self, string):
        string_list = re.sub(r"(.*)\${(.*)}(.*)", r"\1,${\2},\3", string, flags=re.DOTALL).split(",")
        string_list = list(filter(lambda s: s != "", string_list))
        new_string = " + ".join(string_list)
        return new_string