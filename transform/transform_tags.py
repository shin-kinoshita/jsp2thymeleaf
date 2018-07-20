from bs4 import BeautifulSoup, Tag
import re

from replace_definition import def_list


def transform_tags(in_file, out_file):
    soup = BeautifulSoup(in_file, "html.parser")

    for def_obj in def_list:
        tag_list = soup.find_all(
            name=re.compile("^" + def_obj.search_name(def_obj)),
            attrs=def_obj.search_attrs(def_obj),
            text=def_obj.search_text(def_obj)
        )
        for tag in tag_list:
            def_obj.operation(def_list, soup, tag)
        soup = BeautifulSoup(soup.renderContents())

    out_file.write(soup.prettify("utf-8"))
