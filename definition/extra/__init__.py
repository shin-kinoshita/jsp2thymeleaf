from definition.extra.logic.basic.to_th_logic import ToThLogic
from definition.extra.logic.basic.to_th_text_logic import ToThTextLogic

from definition.extra.operation.attribute_operation import AttrOperation
from definition.extra.operation.string_operation import StringOperation

logic_list = [
    ToThLogic(),
    ToThTextLogic(),
]

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