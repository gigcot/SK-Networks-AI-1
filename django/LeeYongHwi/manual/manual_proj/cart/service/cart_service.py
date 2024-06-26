from abc import ABC, abstractmethod


class CartService(ABC):
    @abstractmethod
    def cartRegister(self, cartData, accountId):
        pass