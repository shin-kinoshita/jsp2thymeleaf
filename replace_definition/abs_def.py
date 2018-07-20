from abc import ABCMeta, abstractmethod


class AbsDef(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def search_name(self):
        raise NotImplementedError

    @abstractmethod
    def search_attrs(self):
        raise NotImplementedError

    @abstractmethod
    def search_text(self):
        raise NotImplementedError

    @abstractmethod
    def operation(self, parser, old_tag):
        raise NotImplementedError

