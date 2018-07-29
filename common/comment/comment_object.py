from bs4 import Comment, Tag

from common.comment.comment_template import CommentTemplate


class CommentObject:
    def __init__(self, title=None):
        self.header = None
        self.footer = None
        self.comment_list = list()

        if title is not None:
            self.set_title(title)

    def __iter__(self):
        if self.header is not None:
            self.comment_list.insert(0, self.header)
        if self.footer is not None:
            self.comment_list.append(self.footer)
        return iter(self.comment_list)

    def set_title(self, title):
        header = CommentTemplate.header_template(title)
        footer = CommentTemplate.footer_template(title)
        self.header = Comment(self.format_comment(header, True))
        self.footer = Comment(self.format_comment(footer, True))

    def set_old_tag(self, old_tag):
        old_tag_title = CommentTemplate.base_tag_template("")
        self.add_comment(old_tag_title, Tag(name=old_tag.name, attrs=old_tag.attrs).__str__(), with_todo=True)

    def set_old_string(self, old_string):
        old_tag_title = CommentTemplate.base_string_template("")
        self.add_comment(old_tag_title, old_string, with_todo=True)

    def add_comment(self, title, comment, with_todo=True):
        if title is not None:
            self.comment_list.append(Comment(self.format_comment(title, with_todo)))
        if comment is not None:
            comment_list = self.format_comment_list(comment.split("\n"))
            for comment in comment_list:
                self.comment_list.append(Comment(self.format_comment(comment, False)))

    def add_transformation_impossible_comment(self, title, message):
        title = CommentTemplate.transformation_impossible_template(title)
        self.add_comment(title, message, with_todo=True)

    def add_transformation_unreliable_comment(self, title, message):
        title = CommentTemplate.transformation_unreliable_template(title)
        self.add_comment(title, message, with_todo=True)

    def add_hint_comment(self, title, message):
        title = CommentTemplate.hint_template(title)
        self.add_comment(title, message, with_todo=True)

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
