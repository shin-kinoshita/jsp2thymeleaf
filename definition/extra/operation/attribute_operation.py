from bs4 import BeautifulSoup

from definition.extra.operation.abs_operation import AbsOperation


class AttrOperation(AbsOperation):
    def __init__(self, logic_list):
        super(AttrOperation, self).__init__(logic_list)

    def operate(self, parser):
        tag_list = parser.find_all()

        for tag in tag_list:
            attr_key_list = tag.attrs.keys()
            for attr_key in attr_key_list:
                for logic in self.logic_list:
                    if logic.enable_attr:
                        logic.attr_operation(parser, tag, attr_key)
        parser = BeautifulSoup(parser.renderContents())
        return parser
