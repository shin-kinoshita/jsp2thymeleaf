from abc import ABCMeta, abstractmethod


class AbsLogic(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operation(self, in_file, out_file):
        raise NotImplementedError
