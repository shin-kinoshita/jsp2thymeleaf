import re

from bs4 import Comment, NavigableString

from common.comment.comment_object import CommentObject
from .abs_logic import AbsLogic


class TransformElLogic(AbsLogic):
    def __init__(self):
        super(TransformElLogic, self).__init__(enable_attr=True, enable_string=True)

    def attr_operation(self, parser, tag, attr_key):
        comment_object = CommentObject(title="Transform el notation")
        comment_object.set_old_tag(tag)
        comment_object.add_transformation_unreliable_comment(
            "Check transformed text if base one contains multiple el expressions",
            '''
            Multiple el expressions within one attribute value, are not supported.
            In that case, transformation could not be executed properly.
            '''
        )

        attr_val = tag[attr_key]
        if isinstance(attr_val, list):
            is_replace = False
            new_attr_val = list()
            for i, val in enumerate(attr_val):
                if re.match(r"(.*)\$\{(.*)f:h\((.*)\)(.*)\}(.*)", val):
                    is_replace = True
                    val = self.transform_f_h(val)
                new_attr_val.append(val)
            if is_replace:
                self.replace_attr_val(tag, attr_key, new_attr_val, comment_object)
        else:
            if re.match(r"(.*)\$\{(.*)f:h\((.*)\)(.*)\}(.*)", attr_val):
                new_attr_val = self.transform_f_h(attr_val)
                self.replace_attr_val(tag, attr_key, new_attr_val, comment_object)

    def string_operation(self, parser, tag, string):
        comment_object = CommentObject(title="Transform el expression")
        comment_object.set_old_string(string)
        comment_object.add_transformation_unreliable_comment(
            "Check transformed text if base one contains multiple el expressions",
            '''
            Multiple el expressions within one line text, are not supported.
            In that case, transformation could not be executed properly.
            '''
        )

        if isinstance(string, Comment):
            return
        if re.match(r"(.*)\$\{(.*)f:h\((.*)\)(.*)\}(.*)", string, flags=re.DOTALL):
            self.replace_string(string, self.transform_f_h(string), comment_object)

    def transform_f_h(self, text):
        return NavigableString(re.sub(r"(.*)\$\{(.*)f:h\((.*)\)(.*)\}(.*)", r"\1${\2\3\4}\5", text, flags=re.DOTALL))

