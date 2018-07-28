import re

from bs4 import NavigableString

from common.comment_list import CommentList
from .abs_tag_def import AbsTagDef


class FormatNumberDef(AbsTagDef):
    def search_name(self):
        return "fmt:formatnumber"

    def search_attrs(self):
        return {}

    def search_string(self):
        return None

    def operate(self, parser, old_tag):
        comment_list = CommentList(
            header="jsp2thymeleaf comment begin: fmt:formatNumber",
            footer="jsp2thymeleaf comment end: fmt:formatNumber"
        )
        if old_tag.has_attr("value") and old_tag.has_attr("pattern"):
            value_val = old_tag["value"]
            pattern_val = old_tag["pattern"]
            if re.match(r"\${(.*)}", value_val):
                value_val = re.sub(r"\${(.*)}", r"\1", value_val)

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

            old_tag.replace_with(new_string)

