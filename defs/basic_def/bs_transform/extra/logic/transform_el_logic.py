import re

from bs4 import Comment, NavigableString

from common.comment.comment_object import CommentObject
from .abs_logic import AbsLogic


class TransformElLogic(AbsLogic):
    def __init__(self, comment_level=None):
        super(TransformElLogic, self).__init__(
            enable_attr=True,
            enable_string=True,
            comment_level=comment_level
        )

    def attr_operation(self, parser, tag, attr_key):
        self.tag = tag
        self.attr_key = attr_key
        self.attr_val = tag[attr_key]
        comment_object = CommentObject(title=self.__class__.__name__, default_level=self.comment_level)
        comment_object.set_old_tag(tag)
        comment_object.add_transformation_unreliable_comment(
            "Check transformed text if base one contains multiple el expressions"
        )

        transform_info_list = [
            {'pattern': r"(.*)\$\{(.*)f:h\((.*)\)(.*)\}(.*)", 'method': self.transform_f_h},
        ]
        if isinstance(self.attr_val, list):
            self.attr_list_type_operation(transform_info_list, comment_object)
        else:
            self.attr_non_list_type_operation(transform_info_list, comment_object)

    def attr_list_type_operation(self, transform_info_list, comment_object):
        for transform_info in transform_info_list:
            pattern = transform_info['pattern']
            method = transform_info['method']

            is_replace = False
            new_attr_val = list()
            for i, val in enumerate(self.attr_val):
                if re.match(pattern, val):
                    is_replace = True
                    val = method(val)
                new_attr_val.append(val)
            if is_replace:
                self.replace_attr_val(self.tag, self.attr_key, new_attr_val, comment_object)

    def attr_non_list_type_operation(self, transform_info_list, comment_object):
        for transform_info in transform_info_list:
            pattern = transform_info['pattern']
            method = transform_info['method']

            if re.match(pattern, self.attr_val):
                new_attr_val = method(self.attr_val)
                self.replace_attr_val(self.tag, self.attr_key, new_attr_val, comment_object)

    def string_operation(self, parser, tag, string):
        comment_object = CommentObject(title=self.__class__.__name__, default_level=self.comment_level)
        comment_object.set_old_string(string)
        comment_object.add_transformation_unreliable_comment(
            "Check transformed text if base one contains multiple el expressions"
        )

        if isinstance(string, Comment):
            return

        transform_info_list = [
            { 'pattern': r"(.*)\$\{(.*)f:h\((.*)\)(.*)\}(.*)", 'method': self.transform_f_h },
        ]
        for transform_info in transform_info_list:
            pattern = transform_info['pattern']
            method = transform_info['method']
            if re.match(pattern, string, flags=re.DOTALL):
                self.replace_string(string, method(string), comment_object)

    def transform_f_h(self, text):
        return NavigableString(re.sub(r"(.*)\$\{(.*)f:h\((.*)\)(.*)\}(.*)", r"\1${\2\3\4}\5", text, flags=re.DOTALL))
