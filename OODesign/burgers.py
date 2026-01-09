from enum import Enum, IntEnum
from abc import ABC, abstractmethod


########### IntEnum ####################
class ErrorCode(IntEnum):
    TIMEOUT = 500
    NOT_FOUND = 404
    SUCCESS = 200

print(ErrorCode.TIMEOUT > 450)
# Output: True (because ErrorCode.TIMEOUT acts like the integer 500)

########################################
class Burgers(Enum):
    CHEESE = "CHEESE"
    DELUXE_CHEESE = "DELUXE_CHEESE"
    VEGAN = "VEGAN"
    DELUXE_VEGAN = "DELUXE_VEGAN"


class Burger(ABC):

    def __init__(self):
        self.name = ""
        self.bread = ""
        self.sauce = ""
        self.toppings = []

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def serve(self):
        pass

    def get_name(self):
        return self.name


class CheeseBurger(Burger):

    def __init__(self):
        super().__init__()
        self.name = "Cheese Burger"

    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass


class DeluxeCheeseBurger(Burger):

    def __init__(self):
        super().__init__()
        self.name = "Deluxe Cheese Burger"

    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass


class VeganBurger(Burger):

    def __init__(self):
        super().__init__()
        self.name = "Vegan Burger"

    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass


class DeluxeVeganBurger(Burger):

    def __init__(self):
        super().__init__()
        self.name = "DeluxeVegan Burger"
        # set other attributes...

    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass


class BurgerStore(ABC):

    @abstractmethod
    def create_burger(self, item: Burgers) -> Burger:
        pass

    def order_burger(self, type: Burgers) -> Burger:
        burger = self.create_burger(type)
        print(f"--- Making a {burger.get_name()} ---")
        burger.prepare()
        burger.cook()
        burger.serve()
        return burger


class CheeseBurgerStore(BurgerStore):

    def create_burger(self, item: Burgers) -> Burger:
        if item == Burgers.CHEESE:
            return CheeseBurger()
        elif item == Burgers.DELUXE_CHEESE:
            return DeluxeCheeseBurger()
        else:
            return None


class VeganBurgerStore(BurgerStore):

    def create_burger(self, item: Burgers) -> VeganBurger | DeluxeVeganBurger | None:
        if item == Burgers.VEGAN:
            return VeganBurger()
        elif item == Burgers.DELUXE_VEGAN:
            return DeluxeVeganBurger()
        else:
            return None


cheese_store = CheeseBurgerStore()
vegan_store = VeganBurgerStore()

burger = cheese_store.order_burger(Burgers.CHEESE)
print(f"Ethan ordered a {burger.get_name()}")
burger = vegan_store.order_burger(Burgers.VEGAN)
print(f"Joel ordered a {burger.get_name()}")
