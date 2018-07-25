import re

from other_transform.logic.abs_logic import AbsLogic


class TransformCommentLogic(AbsLogic):
    def operation(self, in_contents):
        return re.sub(
            r"(.*?)<%--(.*?)--%>(.*?)",
            r"\1<!--\2-->\3",
            in_contents,
            flags=re.DOTALL
        )
