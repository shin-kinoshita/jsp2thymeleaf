from abc import ABCMeta, abstractmethod


class AbsOperation(metaclass=ABCMeta):
    def set_logic_list(self, logic_list):
        self.logic_list = logic_list

    @abstractmethod
    def operate(self, parser):
        raise NotImplementedError
