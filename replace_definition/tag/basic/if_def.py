from bs4 import Tag

from replace_definition.abs_def import AbsDef


class IfDef(AbsDef):
    def search_name(self):
        return "c:if"

    def search_attrs(self):
        return {}

    def search_string(self):
        return None

    def operation(self, parser, old_tag):
        if old_tag.has_attr("test"):
            test_val = old_tag["test"]
            new_tag = Tag(parser, name="div", attrs=[("th:if", test_val)])
            new_tag.contents = old_tag.contents
            old_tag.replaceWith(new_tag)

