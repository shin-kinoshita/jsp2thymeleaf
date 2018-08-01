from bs4 import Tag

from common.comment.comment_object import CommentObject
from defs.basic_def.bs_transform.tag.abs_tag_def import AbsTagDef


class HtmlOptionDef(AbsTagDef):
    def search_name(self):
        return "html:option"

    def search_attrs(self):
        return {}

    def search_string(self):
        return None

    def operate(self, parser, old_tag):
        comment_object = CommentObject(title="html:option")
        comment_object.set_old_tag(old_tag)

        attrs = old_tag.attrs
        if old_tag.has_attr("styleid"):
            attrs["id"] = old_tag.attrs.pop("styleid")
        if old_tag.has_attr("styleclass"):
            attrs["class"] = old_tag.attrs.pop("styleclass")

        new_tag = Tag(parser, name="option", attrs=attrs)
        new_tag.contents = old_tag.contents

        self.replace_tag(old_tag, new_tag, comment_object)
