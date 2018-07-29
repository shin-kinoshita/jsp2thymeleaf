from bs4 import Tag

from common.comment.comment_object import CommentObject
from .abs_tag_def import AbsTagDef


class IfDef(AbsTagDef):
    def search_name(self):
        return "c:if"

    def search_attrs(self):
        return {}

    def search_string(self):
        return None

    def operate(self, parser, old_tag):
        comment_object = CommentObject(title="c:if")
        comment_object.set_old_tag(old_tag)

        if old_tag.has_attr("test"):
            self.operate_test(parser, old_tag, comment_object)

    def operate_test(self, parser, old_tag, comment_object):
        test_val = old_tag["test"]

        new_tag = Tag(parser, name="div", attrs=[("th:if", test_val)])
        new_tag.contents = old_tag.contents

        self.replace_tag(old_tag, new_tag, comment_object)
