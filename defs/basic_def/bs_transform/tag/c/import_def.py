from common.comment.comment_object import CommentObject
from defs.basic_def.bs_transform.tag.abs_tag_def import AbsTagDef


class CImportDef(AbsTagDef):
    def __init__(self, comment_level=None):
        super(CImportDef, self).__init__(comment_level=comment_level)

    def search_name(self):
        return "c:import"

    def operate(self, parser, old_tag):
        comment_object = CommentObject(title=self.__class__.__name__, default_level=self.comment_level)
        comment_object.add_transformation_impossible_comment(
            "Replace c:import tag with fragment attribute manually"
        )

        self.replace_tag(old_tag, old_tag, comment_object)
