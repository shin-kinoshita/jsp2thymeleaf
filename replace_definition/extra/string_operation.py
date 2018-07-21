import re

from bs4 import Tag


def string_operation(parser):
    string_list = parser.find_all(string=re.compile("\$\{.*\}"))

    for string in string_list:
        new_tag = Tag(parser, name="div", attrs=[("th:text", string)])
        string.replace_with(new_tag)

