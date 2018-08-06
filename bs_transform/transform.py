from bs4 import BeautifulSoup

from defs import bs_transform_def


def transform(in_file, out_file):
    soup = BeautifulSoup(in_file, "html.parser")
    soup = transform_tag(soup)
    soup = transform_extra(soup)

    out_file.write(soup.prettify("utf-8"))


def transform_tag(parser):
    for tag_def in bs_transform_def.get_tag_def_list():
        tag_list = parser.find_all(
            name=tag_def.get_search_name()
        )
        for tag in tag_list:
            tag_def.operate(parser, tag)
        parser = BeautifulSoup(parser.renderContents(), "html.parser")
    return parser


def transform_extra(parser):
    for operation_def in bs_transform_def.get_extra_operation_def_list():
        parser = operation_def.operate(parser)
    return parser

