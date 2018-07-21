import re


def attribute_operation(parser):
    tag_list = parser.find_all()

    for tag in tag_list:
        key_list = tag.attrs.keys()
        for key in key_list:
            if re.match("\$\{.*\}", tag[key]) and not key.startswith("th:"):
                value = tag.attrs.pop(key)
                tag.attrs["th:" + key] = value
