from bs4 import BeautifulSoup

from .definition.extra import extra_operation_list
from .definition.tag import tag_def_list


def transform(in_file, out_file):
    soup = BeautifulSoup(in_file, "html.parser")

    soup = transform_tag(soup)
    soup = transform_extra(soup)

    out_file.write(soup.prettify("utf-8"))


def transform_tag(parser):
    for tag_def in tag_def_list:
        tag_list = parser.find_all(
            name=tag_def.get_search_name(tag_def),
            attrs=tag_def.get_search_attrs(tag_def),
            string=tag_def.get_search_string(tag_def)
        )
        for tag in tag_list:
            tag_def.operate(tag_def, parser, tag)
        parser = BeautifulSoup(parser.renderContents(), "html.parser")
    return parser


def transform_extra(parser):
    for extra_operation in extra_operation_list:
        parser = extra_operation.operate(parser)
    return parser

