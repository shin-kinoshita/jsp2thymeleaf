from bs4 import Tag


class ForeachDef:
    def __init__(self):
        self.old_name = "c:foreach"
        self.old_attrs = {}
        self.old_text = None

    def operation(self, parser, old_tag):
        if "var" in old_tag.attrs.keys() and "items" in old_tag.attrs.keys():
            var_val = old_tag.attrs["var"]
            items_val = old_tag.attrs["items"]
            new_tag = Tag(parser, name="div", attrs=[("th:each", "{0} : {1}".format(var_val, items_val))])
            new_tag.contents = old_tag.contents
            old_tag.replaceWith(new_tag)
