from bs4 import Comment


class CommentList:
    def __init__(self, header=None, footer=None, comment_info_list=None):
        self.header = None
        self.footer = None
        self.comment_list = list()

        if header is not None:
            self.header = Comment(self.format_comment(header, True))
        if footer is not None:
            self.footer = Comment(self.format_comment(footer, False))
        if comment_info_list is not None:
            self.set_comment_info_list(comment_info_list)

    def __iter__(self):
        if self.header is not None:
            self.comment_list.insert(0, self.header)
        if self.footer is not None:
            self.comment_list.append(self.footer)
        return iter(self.comment_list)

    def set_header(self, comment):
        self.header = self.format_comment(comment, True)

    def set_footer(self, comment):
        self.footer = self.format_comment(comment, False)

    def set_comment_info_list(self, comment_info_list):
        for info in comment_info_list:
            comment = info[0]
            with_todo = info[1]
            self.comment_list.append(Comment(self.format_comment(comment, with_todo)))

    def append(self, comment, with_todo=True):
        comment = self.format_comment(comment, with_todo)
        self.comment_list.append(Comment(comment))

    def pop(self, index=-1):
        return self.comment_list.pop(index)

    def format_comment(self, comment, with_todo):
        if with_todo:
            return "TODO " + comment
        return comment
