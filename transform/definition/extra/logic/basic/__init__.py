from .transform_el_logic import TransformElLogic
from .to_th_logic import ToThLogic
from .to_inline_logic import ToInlineLogic
from .transform_comment_logic import TransformCommentLogic

logic_list = [
    TransformCommentLogic(),
    TransformElLogic(),
    ToThLogic(),
    ToInlineLogic(),
]
