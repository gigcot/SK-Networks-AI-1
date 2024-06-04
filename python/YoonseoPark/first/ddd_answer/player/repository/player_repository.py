from abc import ABC, abstractmethod

class PlayerRepository(ABC):

    @abstractmethod
    def registerPlayer(self, nickname):
        pass

    @abstractmethod
    def findPlayerByNickname(self, nickname):
        pass

