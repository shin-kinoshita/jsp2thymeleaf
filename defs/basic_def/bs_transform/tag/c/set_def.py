import re

from bs4 import Tag

from common.comment.comment_object import CommentObject
from defs.basic_def.bs_transform.tag.abs_tag_def import AbsTagDef


class CSetDef(AbsTagDef):
    def search_name(self):
        return "c:set"

    def search_attrs(self):
        return {}

    def search_string(self):
        return None

    def operate(self, parser, old_tag):
        comment_object = CommentObject(title="c:set")
        comment_object.set_old_tag(old_tag)

        if old_tag.has_attr("var") and old_tag.has_attr("value"):
            self.operate_var_value(parser, old_tag, comment_object)

    def operate_var_value(self, parser, old_tag, comment_object):
        comment_object.add_transformation_unreliable_comment("Check scope of defined variables", '''
            The defined variables are available just inside of the tag.
        ''')

        var_val = old_tag["var"]
        value_val = old_tag["value"]

        if not str.isnumeric(value_val) and not re.match(".*\$\{.*\}.*", value_val):
            value_val = "'{0}'".format(value_val)
        new_tag = Tag(parser, name="div", attrs=[("th:with", "{0}={1}".format(var_val, value_val))])
        new_tag.contents = old_tag.contents

        self.replace_tag(old_tag, new_tag, comment_object)
