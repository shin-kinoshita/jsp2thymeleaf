from bs4 import Tag

from replace_definition.abs_def import AbsDef


class ForeachDef(AbsDef):
    def __init__(self):
        super().__init__()

    def search_name(self):
        return "c:foreach"

    def search_attrs(self):
        return {}

    def search_text(self):
        return None

    def operation(self, parser, old_tag):
        keys = old_tag.attrs.keys()

        if "var" in keys and "items" in keys:
            ForeachDef.iterate_list(parser, old_tag)

        if "var" in keys and "begin" in keys and "end" in keys:
            ForeachDef.iterate_number(parser, old_tag)

    @staticmethod
    def iterate_list(parser, old_tag):
        var_val = old_tag.attrs["var"]
        items_val = old_tag.attrs["items"]

        new_tag = Tag(parser, name="div", attrs=[("th:each", "{0} : {1}".format(var_val, items_val))])
        new_tag.contents = old_tag.contents

        old_tag.replaceWith(new_tag)

    @staticmethod
    def iterate_number(parser, old_tag):
        var_val = old_tag.attrs["var"]
        begin_val = old_tag.attrs["begin"]
        end_val = old_tag.attrs["end"]

        if "step" in old_tag.attrs.keys():
            step_val = old_tag.attrs["step"]
            attrs = [
                ("th:each", "{0} : ${{numbers.sequence({1}, {2}, {3})}}".format(var_val, begin_val, end_val, step_val))]
        else:
            attrs = [("th:each", "{0} : ${{numbers.sequence({1}, {2})}}".format(var_val, begin_val, end_val))]
        new_tag = Tag(parser, name="div", attrs=attrs)
        new_tag.contents = old_tag.contents

        old_tag.replaceWith(new_tag)
