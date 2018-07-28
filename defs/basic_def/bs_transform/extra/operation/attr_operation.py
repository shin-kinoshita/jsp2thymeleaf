from bs4 import BeautifulSoup

from .abs_operation import AbsOperation


class AttrOperation(AbsOperation):
    def operate(self, parser):
        for logic in self.logic_list:
            if not logic.enable_attr:
                continue
            tag_list = parser.find_all()
            for tag in tag_list:
                attr_key_list = tag.attrs.keys()
                for attr_key in attr_key_list:
                        logic.attr_operation(parser, tag, attr_key)
            parser = BeautifulSoup(parser.renderContents(), "html.parser")
        return parser
