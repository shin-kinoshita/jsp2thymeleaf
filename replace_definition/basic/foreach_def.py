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
        if "var" in old_tag.attrs.keys() and "items" in old_tag.attrs.keys():
            var_val = old_tag.attrs["var"]
            items_val = old_tag.attrs["items"]
            new_tag = Tag(parser, name="div", attrs=[("th:each", "{0} : {1}".format(var_val, items_val))])
            new_tag.contents = old_tag.contents
            old_tag.replaceWith(new_tag)
