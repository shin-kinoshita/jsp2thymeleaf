from bs4 import BeautifulSoup
import re

from replace_definition.tag import tag_def_list


def transform(in_file, out_file):
    soup = BeautifulSoup(in_file, "html.parser")

    soup = transform_tag(soup)

    out_file.write(soup.prettify("utf-8"))


def transform_tag(parser):
    for tag_def in tag_def_list:
        tag_list = parser.find_all(
            name=re.compile("^" + tag_def.search_name(tag_def)),
            attrs=tag_def.search_attrs(tag_def),
            text=tag_def.search_text(tag_def)
        )
        for tag in tag_list:
            tag_def.operation(tag_def_list, parser, tag)
        parser = BeautifulSoup(parser.renderContents())
    return parser


def transform_value(parser):
    pass

