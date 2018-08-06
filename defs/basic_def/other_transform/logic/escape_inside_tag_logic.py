import re

from .abs_logic import AbsLogic


class EscapeInsideTagLogic(AbsLogic):
    def operation(self, in_contents):
        start_symbol_list = ['<', '</']
        end_symbol_list = ['>', '/>']
        first_depth_escape_list = ['<', '>', '/>', '</']
        second_depth_escape_list = ['\'', '\"']

        match_object_list = list()
        for symbol in set(start_symbol_list + end_symbol_list + first_depth_escape_list + second_depth_escape_list):
            match_object_list += self.find_match_object_list(symbol, in_contents)

        match_object_list = self.filter_match_object_list(match_object_list)

        is_inside_tag = False

        out_contents = ''
        inside_tag_count = 0
        prev_end_index = 0

        for match_object in match_object_list:
            symbol = match_object.group()
            if is_inside_tag:
                if symbol in start_symbol_list:
                    inside_tag_count += 1
                elif symbol in end_symbol_list:
                    if inside_tag_count > 0:
                        inside_tag_count -= 1
                    else:
                        is_inside_tag = False
                if is_inside_tag and inside_tag_count >= 0 and symbol in first_depth_escape_list:
                    out_contents += in_contents[prev_end_index:match_object.start()] + self.escape(symbol)
                elif is_inside_tag and inside_tag_count >= 1 and symbol in second_depth_escape_list:
                    out_contents += in_contents[prev_end_index:match_object.start()] + self.escape(symbol)
                else:
                    out_contents += in_contents[prev_end_index:match_object.start()] + symbol
            else:
                if symbol in start_symbol_list:
                    is_inside_tag = True
                out_contents += in_contents[prev_end_index:match_object.start()] + symbol

            # if not is_inside_tag and symbol in start_symbol_list:
            #     is_inside_tag = True
            #     out_contents += in_contents[prev_end_index:match_object.start()] + symbol
            #     continue
            # elif is_inside_tag and symbol in start_symbol_list:
            #     inside_tag_count += 1
            # elif is_inside_tag and symbol in end_symbol_list:
            #     if inside_tag_count > 0:
            #         inside_tag_count -= 1
            #     else:
            #         is_inside_tag = False
            #
            # if is_inside_tag and symbol in escape_symbol_list:
            #     out_contents += in_contents[prev_end_index:match_object.start()] + self.escape(symbol)
            prev_end_index = match_object.end()

        out_contents += in_contents[prev_end_index:]

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
                span = [start, end - 1]
                dup_list.append(match)
            elif self.is_inside(start, span) or self.is_inside(end - 1, span):
                if not self.is_inside(start, span):
                    span[0] = start
                elif not self.is_inside(end - 1, span):
                    span[1] = end - 1
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
        dup_list.sort(key=lambda obj: (obj.start(), -(obj.end() - obj.start())))
        return dup_list[0]

    def is_inside(self, val, span):
        if span[0] <= val <= span[1]:
            return True
        return False

    def escape(self, string):
        if string == '<':
            return '&lt;'
        if string == '</':
            return '&lt;/'
        if string == '>':
            return '&gt;'
        if string == '/>':
            return '/&gt;'
        if string == '\'':
            return '&apos;'
            # return '&#39;'
        if string == '\"':
            return '&quot;'
            # return '&quot;'
        if string == '&':
            return '&amp;'
        return '\{0}'.format(string)

