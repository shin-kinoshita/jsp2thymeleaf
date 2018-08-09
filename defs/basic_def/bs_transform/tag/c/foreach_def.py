from bs4 import Tag

from common.comment.comment_object import CommentObject
from defs.basic_def.bs_transform.tag.abs_tag_def import AbsTagDef


class CForeachDef(AbsTagDef):
    def __init__(self, comment_level=None):
        super(CForeachDef, self).__init__(comment_level=comment_level)

    def search_name(self):
        return "c:foreach"

    def operate(self, parser, old_tag):
        comment_object = CommentObject(title=self.__class__.__name__, default_level=self.comment_level)
        comment_object.set_old_tag(old_tag)

        if old_tag.has_attr("var") and old_tag.has_attr("items"):
            self.operate_var_items(parser, old_tag, comment_object)
        elif old_tag.has_attr("var") and old_tag.has_attr("begin") and old_tag.has_attr("end"):
            self.operate_var_begin_end(parser, old_tag, comment_object)

    def operate_var_items(self, parser, old_tag, comment_object):
        var_val = old_tag["var"]
        items_val = old_tag["items"]

        if old_tag.has_attr("varstatus"):
            var_status_val = old_tag["varstatus"]
            attrs = {"th:each": "{0}, {1} : {2}".format(var_val, var_status_val, items_val)}
        else:
            attrs = {"th:each": "{0} : {1}".format(var_val, items_val)}

        new_tag = Tag(parser, name="th:block", attrs=attrs)
        new_tag.contents = old_tag.contents

        self.replace_tag(old_tag, new_tag, comment_object)

    def operate_var_begin_end(self, parser, old_tag, comment_object):
        var_val = old_tag["var"]
        begin_val = old_tag["begin"]
        end_val = old_tag["end"]

        if old_tag.has_attr("step"):
            step_val = old_tag["step"]
            attrs = {"th:each": "{0} : ${{numbers.sequence({1}, {2}, {3})}}".format(var_val, begin_val, end_val, step_val)}
        else:
            attrs = {"th:each": "{0} : ${{numbers.sequence({1}, {2})}}".format(var_val, begin_val, end_val)}
        new_tag = Tag(parser, name="div", attrs=attrs)
        new_tag.contents = old_tag.contents

        self.replace_tag(old_tag, new_tag, comment_object)
