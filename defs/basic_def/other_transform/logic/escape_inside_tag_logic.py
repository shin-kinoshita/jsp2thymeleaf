import re

from .abs_logic import AbsLogic


class EscapeInsideTagLogic(AbsLogic):
    def operation(self, in_contents):
        start_symbol_list = ['<']
        end_symbol_list = ['>', '/>']
        escape_symbol_list = ['<', '>', '/>', '\'', '\"']

        match_object_list = list()
        for symbol in set(start_symbol_list + end_symbol_list + escape_symbol_list):
            match_object_list += self.find_match_object_list(symbol, in_contents)

        match_object_list = self.filter_match_object_list(match_object_list)

        is_inside_tag = False

        out_contents = in_contents
        inside_tag_count = 0

        for match_object in match_object_list:
            symbol = match_object.group()
            if is_inside_tag and symbol in start_symbol_list:
                inside_tag_count += 1

            if is_inside_tag and symbol in end_symbol_list:
                if inside_tag_count > 0:
                    inside_tag_count -= 1
                else:
                    is_inside_tag = False

            if is_inside_tag and symbol in escape_symbol_list:
                out_contents = self.escape(match_object.start(), out_contents)

            if not is_inside_tag and symbol in start_symbol_list:
                is_inside_tag = True

        return out_contents

    def find_match_object_list(self, symbol, string):
        return list(re.finditer(symbol, string))

    def filter_match_object_list(self, match_list):
        new_match_list = list()
        match_list.sort(key=lambda obj: obj.start())

        i = 0
        span = [0, 0]
        dup_list = list()
        while i < len(match_list):
            match = match_list[i]
            start, end = match.span()
            if len(dup_list) == 0:
                span = [start, end]
                dup_list.append(match)
            elif self.is_inside(start, span) or self.is_inside(end, span):
                if not self.is_inside(start, span):
                    span[0] = start
                elif not self.is_inside(end, span):
                    span[1] = end
                dup_list.append(match)
            else:
                symbol = self.select_symbol(dup_list)
                if symbol is not None:
                    new_match_list.append(symbol)
                dup_list = list()
                continue
            i += 1

        symbol = self.select_symbol(dup_list)
        if symbol is not None:
            new_match_list.append(symbol)

        return new_match_list

    def select_symbol(self, dup_list):
        if len(dup_list) == 0:
            return
        dup_list.sort(lambda obj: (obj.start(), -(obj.end() - obj.start())))
        return dup_list[0]

    def is_inside(self, val, span):
        if span[0] <= val <= span[1]:
            return True
        return False

    def escape(self, index, string):
        return string[:index] + '\\' + string[index:]

