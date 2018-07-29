import re

from bs4 import NavigableString

from common.comment.comment_object import CommentObject
from .abs_tag_def import AbsTagDef


class FormatNumberDef(AbsTagDef):
    def search_name(self):
        return "fmt:formatnumber"

    def search_attrs(self):
        return {}

    def search_string(self):
        return None

    def operate(self, parser, old_tag):
        comment_object = CommentObject(title="fmt:formatNumber")
        comment_object.set_old_tag(old_tag)

        if old_tag.has_attr("value") and old_tag.has_attr("pattern"):
            self.operate_value_pattern(parser, old_tag, comment_object)

    def operate_value_pattern(self, parser, old_tag, comment_object):
        comment_object.add_transformation_unreliable_comment("Check number parameters", '''
            Number parameters of #numbers could be incorrect.
        ''')

        value_val = old_tag["value"]
        pattern_val = old_tag["pattern"]

        if re.match(r"\${(.*)}", value_val):
            value_val = re.sub(r"\${(.*)}", r"\1", value_val)

        new_string = ""
        if "," in pattern_val and "#" in pattern_val:
            new_string = NavigableString("${{#numbers.formatInteger({0}, 1, 'COMMA')}}".format(value_val))
        elif "," in pattern_val and "0" in pattern_val:
            count = pattern_val.count("0")
            new_string = NavigableString("${{#numbers.formatInteger({0}, {1}, 'COMMA')}}".format(value_val, count))
        elif "." in pattern_val and "#" in pattern_val:
            decimal_count = pattern_val.split(".")[1].count("#")
            new_string = NavigableString("${{#numbers.formatDecimal({0}, 1, {1})}}".format(value_val, decimal_count))
        elif "." in pattern_val and "0" in pattern_val:
            integer_count = pattern_val.split(".")[0].count("0")
            decimal_count = pattern_val.split(".")[1].count("0")
            new_string = NavigableString("${{#numbers.formatInteger({0}, {1}, {2})}}".format(value_val, integer_count, decimal_count))

        self.replace_tag(old_tag, new_string, comment_object)
