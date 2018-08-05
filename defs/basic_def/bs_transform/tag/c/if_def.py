from bs4 import Tag

from common.comment.comment_object import CommentObject
from defs.basic_def.bs_transform.tag.abs_tag_def import AbsTagDef


class CIfDef(AbsTagDef):
    def __init__(self, comment_level=None):
        super(CIfDef, self).__init__(comment_level=comment_level)

    def search_name(self):
        return "c:if"

    def operate(self, parser, old_tag):
        comment_object = CommentObject(title=self.__class__.__name__, default_level=self.comment_level)
        comment_object.set_old_tag(old_tag)

        if old_tag.has_attr("test"):
            self.operate_test(parser, old_tag, comment_object)

    def operate_test(self, parser, old_tag, comment_object):
        test_val = old_tag["test"]

        new_tag = Tag(parser, name="div", attrs=[("th:if", test_val)])
        new_tag.contents = old_tag.contents

        self.replace_tag(old_tag, new_tag, comment_object)
