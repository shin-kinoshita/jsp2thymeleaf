from definition.extra.logic.basic.transform_el_logic import TransformElLogic
from definition.extra.logic.basic.to_th_logic import ToThLogic
from definition.extra.logic.basic.to_inline_logic import ToInlineLogic

from definition.extra.operation.attr_operation import AttrOperation
from definition.extra.operation.string_operation import StringOperation

logic_list = [
    TransformElLogic(),
    ToThLogic(),
    ToInlineLogic(),
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
