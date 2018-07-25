from .logic.basic import logic_list as basic_logic_list
from .logic.custom import logic_list as custom_logic_list

from .operation.attr_operation import AttrOperation
from .operation.string_operation import StringOperation

logic_list = basic_logic_list + custom_logic_list

attr_logic_list = list()
string_logic_list = list()

for logic in logic_list:
    if logic.enable_attr:
        attr_logic_list.append(logic)
    if logic.enable_string:
        string_logic_list.append(logic)

extra_operation_list = [
    AttrOperation(attr_logic_list),
    StringOperation(string_logic_list),
]
