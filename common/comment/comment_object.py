from configparser import ConfigParser

from bs4 import Comment, Tag

from common.comment.comment_level import CommentLevel
from common.comment.comment_template import CommentTemplate

config = ConfigParser()
config.read("config.ini")
COMMENT_LEVEL = CommentLevel(int(config['COMMENT']['CommentLevel']))


class CommentObject:
    def __init__(self, title=None, default_level=None):
        self.title = None
        self.old_tag = None
        self.old_string = None
        self.default_level = default_level
        self.comment_list = list()

        if title is not None:
            self.set_title(title)

        if self.default_level is None:
            self.default_level = CommentLevel.NORMAL

    def __iter__(self):
        if self.default_level > COMMENT_LEVEL and len(self.comment_list) == 0:
            return iter(list())
        if self.old_string is not None:
            self.comment_list.insert(0, self.old_string)
        if self.old_tag is not None:
            self.comment_list.insert(0, self.old_tag)
        if self.title is not None:
            self.comment_list.insert(0, self.title)
        return iter(self.comment_list)

    def set_title(self, title):
        title = CommentTemplate.title_template(title)
        self.title = Comment(self.format_comment(title, True))

    def set_old_tag(self, old_tag):
        old_tag = CommentTemplate.base_tag_template(Tag(name=old_tag.name, attrs=old_tag.attrs).__str__())
        self.old_tag = Comment(self.format_comment(old_tag, False))

    def set_old_string(self, old_string):
        old_string = CommentTemplate.base_string_template(old_string)
        self.old_string = Comment(self.format_comment(old_string, False))

    def add_comment(self, title, comment, with_todo=True, level=None):
        if level is None:
            level = self.default_level
        if level > COMMENT_LEVEL:
            return

        if title is not None:
            self.comment_list.append(Comment(self.format_comment(title, with_todo)))
        if comment is not None:
            comment_list = self.format_comment_list(comment.split("\n"))
            for comment in comment_list:
                self.comment_list.append(Comment(self.format_comment(comment, False)))

    def add_transformation_impossible_comment(self, title, message=None):
        title = CommentTemplate.transformation_impossible_template(title)
        self.add_comment(title, message, with_todo=True, level=CommentLevel.ESSENTIAL)

    def add_transformation_unreliable_comment(self, title, message=None):
        title = CommentTemplate.transformation_unreliable_template(title)
        self.add_comment(title, message, with_todo=True, level=CommentLevel.NORMAL)

    def add_hint_comment(self, title, message=None):
        title = CommentTemplate.hint_template(title)
        self.add_comment(title, message, with_todo=True, level=CommentLevel.NORMAL)

    def format_comment_list(self, comment_list):
        new_comment_list = list()
        for comment in comment_list:
            if comment.strip() == "":
                continue
            new_comment_list.append(comment)
        return new_comment_list

    def format_comment(self, comment, with_todo):
        comment = comment.strip()
        if with_todo:
            return "TODO " + comment
        return "     " + comment
