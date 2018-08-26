import re

from bs4 import Comment, NavigableString, Tag

from common.comment.comment_object import CommentObject
from .abs_logic import AbsLogic


class TransformElLogic(AbsLogic):
    def __init__(self, comment_level=None):
        super(TransformElLogic, self).__init__(
            enable_attr=True,
            enable_string=True,
            comment_level=comment_level
        )

        self.transform_info_list = [
            {'pattern': r"(.*)\$\{f:h\((.*)\)\}(.*)", 'method': self.transform_f_h},
            {'pattern': r"(.*)\$\{f:br\((.*)\)\}(.*)", 'method': self.transform_f_br},
        ]


    def attr_operation(self):
        comment_object = CommentObject(title=self.__class__.__name__, default_level=self.comment_level)
        comment_object.set_old_tag(self.tag)
        comment_object.add_transformation_unreliable_comment(
            "Check transformed text if base one contains multiple el expressions"
        )

        if isinstance(self.attr_val, list):
            self.attr_list_type_operation(self.transform_info_list, comment_object)
        else:
            self.attr_non_list_type_operation(self.transform_info_list, comment_object)

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
                self.replace_attr_val(new_attr_val, comment_object)

    def attr_non_list_type_operation(self, transform_info_list, comment_object):
        for transform_info in transform_info_list:
            pattern = transform_info['pattern']
            method = transform_info['method']

            if re.match(pattern, self.attr_val):
                new_attr_val = method(self.attr_val)
                self.replace_attr_val(new_attr_val, comment_object)

    def string_operation(self):
        comment_object = CommentObject(title=self.__class__.__name__, default_level=self.comment_level)
        comment_object.set_old_string(self.string)
        comment_object.add_transformation_unreliable_comment(
            "Check transformed text if base one contains multiple el expressions"
        )

        if isinstance(self.string, Comment):
            return

        for transform_info in self.transform_info_list:
            pattern = transform_info['pattern']
            method = transform_info['method']
            if re.match(pattern, self.string, flags=re.DOTALL):
                self.replace_string(method(self.string), comment_object)

    def transform_f_h(self, text):
        return NavigableString(re.sub(r"(.*)\$\{f:h\((.*)\)\}(.*)", r"\1${\2}\3", text, flags=re.DOTALL))

    def transform_f_br(self, text):
        pattern = r"(.*)\$\{f:br\((.*)\)\}(.*)"
        before_sentence = re.sub(pattern, r"\1", text, flags=re.DOTALL)
        sentence = re.sub(pattern, r"\2", text, flags=re.DOTALL)
        after_sentence = re.sub(pattern, r"\3", text, flags=re.DOTALL)

        loop_tag = Tag(
            self.parser,
            name="th:block",
            attrs={"th:each": "str, stat : ${{{0}.split('\\r\\n|\\r|\\n', -1)}}".format(sentence)}
        )
        loop_tag.append(NavigableString("[[${{str}}]]"))
        loop_tag.append(Tag(self.parser, name="br", attrs={"th:if": "${{!str.last}}"}))

        sentence_tag = Tag(self.parser, name="th:block", attrs={"th:if": "${{{0}}}".format(sentence)})
        sentence_tag.append(loop_tag)

        new_tag = Tag(self.parser, name="th:block")
        new_tag.append(before_sentence)
        new_tag.append(sentence_tag)
        new_tag.append(after_sentence)

        return new_tag
