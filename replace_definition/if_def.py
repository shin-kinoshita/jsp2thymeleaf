from bs4 import Tag


class IfDef:
    def __init__(self):
        self.old_name = "c:if"
        self.old_attrs = {}
        self.old_text = None

    def operation(self, parser, old_tag):
        test_val = old_tag.attrs["test"]
        new_tag = Tag(parser, name="div", attrs=[("th:test", test_val)])
        new_tag.contents = old_tag.contents
        old_tag.replaceWith(new_tag)

