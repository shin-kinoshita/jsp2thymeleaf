from .bs_transform.extra.logic.edit_linking_literal_logic import EditLinkingLiteralLogic
from .bs_transform.extra.logic.to_inline_logic import ToInlineLogic
from .bs_transform.extra.logic.to_th_logic import ToThLogic
from .bs_transform.extra.logic.transform_el_logic import TransformElLogic

from .bs_transform.extra.operation.attr_operation import AttrOperation
from .bs_transform.extra.operation.string_operation import StringOperation

from .bs_transform.tag.c.foreach_def import CForeachDef
from .bs_transform.tag.c.if_def import CIfDef
from .bs_transform.tag.c.out_def import COutDef
from .bs_transform.tag.c.set_def import CSetDef
from .bs_transform.tag.fmt.format_number_def import FmtFormatNumberDef
from .bs_transform.tag.html.option_def import HtmlOptionDef
from .bs_transform.tag.html.select_def import HtmlSelectDef

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
   CForeachDef(),
   CIfDef(),
   COutDef(),
   CSetDef(),
   FmtFormatNumberDef(),
   HtmlOptionDef(),
   HtmlSelectDef(),
]

other_logic_def_list = [
   TransformCommentLogic(),
]
