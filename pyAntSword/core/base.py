import abc

class Base(abc.ABC):
    
    @abc.abstractmethod
    def encoder():
        pass
    
    @abc.abstractmethod
    def decode():
        pass
    
    @abc.abstractmethod
    def complete():
        pass
    
    