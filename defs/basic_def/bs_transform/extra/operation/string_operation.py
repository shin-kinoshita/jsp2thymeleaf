from bs4 import BeautifulSoup

from .abs_operation import AbsOperation


class StringOperation(AbsOperation):
    def operate(self, parser):
        for logic in self.logic_list:
            if not logic.enable_string:
                continue
            string_list = parser.find_all(string=True)
            for string in string_list:
                logic.string_operation(parser, string.parent, string)
            parser = BeautifulSoup(parser.renderContents(), "html.parser")
        return parser
