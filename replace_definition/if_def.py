from bs4 import Tag

from replace_definition.abs_def import AbsDef


class IfDef(AbsDef):
    def __init__(self):
        super().__init__()

    def search_name(self):
        return "c:if"

    def search_attrs(self):
        return {}

    def search_text(self):
        return None

    def operation(self, parser, old_tag):
        test_val = old_tag.attrs["test"]
        new_tag = Tag(parser, name="div", attrs=[("th:if", test_val)])
        new_tag.contents = old_tag.contents
        old_tag.replaceWith(new_tag)

