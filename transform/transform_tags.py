from bs4 import BeautifulSoup, Tag
import re

from replace_definition.if_def import IfDef
from replace_definition.foreach_def import ForeachDef

DEF_LIST = [
    IfDef(),
    ForeachDef(),
]


def transform_tags(in_file, out_file):
    soup = BeautifulSoup(in_file, "html.parser")

    for def_obj in DEF_LIST:
        tag_list = soup.find_all(
            name=re.compile("^" + def_obj.search_name()),
            attrs=def_obj.search_attrs(),
            text=def_obj.search_text()
        )
        for tag in tag_list:
            def_obj.operation(soup, tag)
        soup = BeautifulSoup(soup.renderContents())

    out_file.write(soup.prettify("utf-8"))
