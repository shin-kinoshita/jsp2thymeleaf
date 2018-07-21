from bs4 import Tag

from replace_definition.abs_def import AbsDef


class OutDef(AbsDef):
    def search_name(self):
        return "c:out"

    def search_attrs(self):
        return {}

    def search_string(self):
        return None

    def operation(self, parser, old_tag):
        keys = old_tag.attrs.keys()

        if "value" in keys:
            value_val = old_tag.attrs["value"]
            new_tag = Tag(parser, name="div", attrs=[("th:text", value_val)])
            new_tag.contents = old_tag.contents
            old_tag.replaceWith(new_tag)

