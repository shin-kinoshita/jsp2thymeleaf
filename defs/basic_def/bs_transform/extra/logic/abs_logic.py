from abc import ABCMeta


class AbsLogic(metaclass=ABCMeta):
    def __init__(self, enable_attr=False, enable_string=False):
        self.enable_attr = enable_attr
        self.enable_string = enable_string

    def attr_operation(self, parser, tag, attr_key):
        raise NotImplementedError

    def string_operation(self, parser, tag, string):
        raise NotImplementedError

    def replace_attr_key(self, tag, old_attr_key, new_attr_key, comment_object):
        tag[new_attr_key] = tag.attrs.pop(old_attr_key)
        if comment_object is not None:
            for comment in comment_object:
                tag.insert_before(comment)

    def replace_attr_val(self, tag, attr_key, new_attr_val, comment_object):
        tag[attr_key] = new_attr_val
        if comment_object is not None:
            for comment in comment_object:
                tag.insert_before(comment)

    def replace_string(self, old_string, new_string, comment_object):
        old_string.replace_with(new_string)
        if comment_object is not None:
            for comment in comment_object:
                new_string.insert_before(comment)
