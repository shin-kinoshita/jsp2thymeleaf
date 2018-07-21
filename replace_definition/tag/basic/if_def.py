from bs4 import Tag

from replace_definition.tag.abs_tag_def import AbsTagDef


class IfDef(AbsTagDef):
    def search_name(self):
        return "c:if"

    def search_attrs(self):
        return {}

    def search_text(self):
        return None

    def operation(self, parser, old_tag):
        keys = old_tag.attrs.keys()

        if "test" in keys:
            test_val = old_tag.attrs["test"]
            new_tag = Tag(parser, name="div", attrs=[("th:if", test_val)])
            new_tag.contents = old_tag.contents
            old_tag.replaceWith(new_tag)

