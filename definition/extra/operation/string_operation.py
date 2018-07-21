from bs4 import BeautifulSoup

from definition.extra.operation.abs_operation import AbsOperation


class StringOperation(AbsOperation):
    def __init__(self, logic_list):
        super(StringOperation, self).__init__(logic_list)

    def operate(self, parser):
        string_list = parser.find_all(string=True)

        for string in string_list:
            for logic in self.logic_list:
                logic.string_operation(parser, string.parent, string)
        parser = BeautifulSoup(parser.renderContents())
        return parser
