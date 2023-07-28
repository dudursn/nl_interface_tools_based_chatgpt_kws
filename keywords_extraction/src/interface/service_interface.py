from abc import ABC, abstractmethod

class ServiceInterface(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def execute(self, opt):
        raise NotImplementedError("Please Implement this method")