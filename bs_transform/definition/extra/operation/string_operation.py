from bs4 import BeautifulSoup

from .abs_operation import AbsOperation


class StringOperation(AbsOperation):
    def __init__(self, logic_list):
        super(StringOperation, self).__init__(logic_list)

    def operate(self, parser):
        for logic in self.logic_list:
            string_list = parser.find_all(string=True)
            for string in string_list:
                logic.string_operation(parser, string.parent, string)
            parser = BeautifulSoup(parser.renderContents(), "html.parser")
        return parser