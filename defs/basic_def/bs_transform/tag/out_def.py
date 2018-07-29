from bs4 import Tag

from common.comment.comment_object import CommentObject
from .abs_tag_def import AbsTagDef


class OutDef(AbsTagDef):
    def search_name(self):
        return "c:out"

    def search_attrs(self):
        return {}

    def search_string(self):
        return None

    def operate(self, parser, old_tag):
        comment_object = CommentObject(title="c:out")
        comment_object.set_old_tag(old_tag)

        if old_tag.has_attr("value"):
            self.operate_value(parser, old_tag, comment_object)

    def operate_value(self, parser, old_tag, comment_object):
        value_val = old_tag.attrs["value"]

        new_tag = Tag(parser, name="div", attrs=[("th:text", value_val)])
        new_tag.contents = old_tag.contents

        self.replace(old_tag, new_tag, comment_object)
