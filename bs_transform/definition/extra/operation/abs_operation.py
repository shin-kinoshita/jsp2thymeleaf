from abc import ABCMeta, abstractmethod


class AbsOperation(metaclass=ABCMeta):
    def __init__(self, logic_list):
        self.logic_list = logic_list

    @abstractmethod
    def operate(self, parser):
        raise NotImplementedError
