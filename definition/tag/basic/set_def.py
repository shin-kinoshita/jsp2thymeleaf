import re

from bs4 import Tag

from definition.tag.abs_tag_def import AbsTagDef


class SetDef(AbsTagDef):
    def search_name(self):
        return "c:set"

    def search_attrs(self):
        return {}

    def search_string(self):
        return None

    def operate(self, parser, old_tag):
        if old_tag.has_attr("var") and old_tag.has_attr("value"):
            var_val = old_tag["var"]
            value_val = old_tag["value"]

            if not str.isnumeric(value_val) and not re.match(".*\$\{.*\}.*", value_val):
                value_val = "'{0}'".format(value_val)
            new_tag = Tag(parser, name="div", attrs=[("th:with", "{0}={1}".format(var_val, value_val))])
            new_tag.contents = old_tag.contents
            old_tag.replaceWith(new_tag)

