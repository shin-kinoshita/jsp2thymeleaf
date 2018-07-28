from .bs_transform.extra.logic.edit_linking_literal_logic import EditLinkingLiteralLogic
from .bs_transform.extra.logic.to_inline_logic import ToInlineLogic
from .bs_transform.extra.logic.to_th_logic import ToThLogic
from .bs_transform.extra.logic.transform_el_logic import TransformElLogic

from .bs_transform.extra.operation.attr_operation import AttrOperation
from .bs_transform.extra.operation.string_operation import StringOperation

from .bs_transform.tag.foreach_def import ForeachDef
from .bs_transform.tag.format_number_def import FormatNumberDef
from .bs_transform.tag.if_def import IfDef
from .bs_transform.tag.out_def import OutDef
from .bs_transform.tag.set_def import SetDef

from .other_transform.logic.transform_comment_logic import TransformCommentLogic

bs_extra_logic_def_list = [
   EditLinkingLiteralLogic(),
   ToInlineLogic(),
   ToThLogic(),
   TransformElLogic(),
]

bs_extra_operation_def_list = [
   AttrOperation(),
   StringOperation(),
]

bs_tag_def_list = [
   ForeachDef(),
   FormatNumberDef(),
   IfDef(),
   OutDef(),
   SetDef(),
]

other_logic_def_list = [
   TransformCommentLogic(),
]
