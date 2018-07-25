from bs4 import Tag

from .abs_tag_def import AbsTagDef


class ForeachDef(AbsTagDef):
    def search_name(self):
        return "c:foreach"

    def search_attrs(self):
        return {}

    def search_string(self):
        return None

    def operate(self, parser, old_tag):
        if old_tag.has_attr("var") and old_tag.has_attr("items"):
            ForeachDef.iterate_list(parser, old_tag)

        if old_tag.has_attr("var") and old_tag.has_attr("begin") and old_tag.has_attr("end"):
            ForeachDef.iterate_number(parser, old_tag)

    @staticmethod
    def iterate_list(parser, old_tag):
        var_val = old_tag["var"]
        items_val = old_tag["items"]

        new_tag = Tag(parser, name="div", attrs=[("th:each", "{0} : {1}".format(var_val, items_val))])
        new_tag.contents = old_tag.contents

        old_tag.replaceWith(new_tag)

    @staticmethod
    def iterate_number(parser, old_tag):
        var_val = old_tag["var"]
        begin_val = old_tag["begin"]
        end_val = old_tag["end"]

        if old_tag.has_attr("step"):
            step_val = old_tag["step"]
            attrs = [
                ("th:each", "{0} : ${{numbers.sequence({1}, {2}, {3})}}".format(var_val, begin_val, end_val, step_val))]
        else:
            attrs = [("th:each", "{0} : ${{numbers.sequence({1}, {2})}}".format(var_val, begin_val, end_val))]
        new_tag = Tag(parser, name="div", attrs=attrs)
        new_tag.contents = old_tag.contents

        old_tag.replaceWith(new_tag)
