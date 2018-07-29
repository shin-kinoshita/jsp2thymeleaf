import re

from common.comment.comment_object import CommentObject
from .abs_logic import AbsLogic


class EditLinkingLiteralLogic(AbsLogic):
    def __init__(self):
        super(EditLinkingLiteralLogic, self).__init__(enable_attr=True, enable_string=False)

    def attr_operation(self, parser, tag, attr_key):
        if attr_key == "th:each":
            return

        attr_val = tag[attr_key]
        if isinstance(attr_val, list):
            is_replace = False
            new_attr_val = list()
            for val in attr_val:
                if re.match(r"(.*)\|(.*)\|(.*)", val, flags=re.DOTALL):
                    new_attr_val.append(val)
                elif re.match(r"\${(.*)}", val, flags=re.DOTALL):
                    new_attr_val.append(val)
                elif re.match(r"(.*)\${(.*)}(.*)", val, flags=re.DOTALL):
                    new_val = self.transform_string(val)
                    new_attr_val.append(new_val)
                    is_replace = True
                else:
                    new_attr_val.append(val)
            if is_replace:
                comment_object = CommentObject(title="Link literals properly")
                comment_object.set_old_tag(tag)
                self.replace_attr_val(tag, attr_key, new_attr_val, comment_object)
        else:
            if re.match(r"(.*)\|(.*)\|(.*)", attr_val, flags=re.DOTALL):
                return
            if re.match(r"\${(.*)}", attr_val, flags=re.DOTALL):
                return
            if re.match(r"(.*)\${(.*)}(.*)", attr_val, flags=re.DOTALL):
                new_attr_val = self.transform_string(attr_val)

                comment_object = CommentObject(title="Link literals properly")
                comment_object.set_old_tag(tag)
                self.replace_attr_val(tag, attr_key, new_attr_val, comment_object)

    def transform_string(self, string):
        string_list = re.sub(r"(.*)\${(.*)}(.*)", r"'\1',${\2},'\3'", string, flags=re.DOTALL).split(",")
        string_list = list(filter(lambda s: s != "''", string_list))
        new_string = " + ".join(string_list)
        return new_string
