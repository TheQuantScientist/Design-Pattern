from __future__ import annotations
from abc import ABC, abstractmethod


# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass


# Concrete Factories (variants)
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


# Abstract Products
class Chair(ABC):
    @abstractmethod
    def sit_on(self) -> str:
        pass


class Sofa(ABC):
    @abstractmethod
    def lie_on(self) -> str:
        pass

    @abstractmethod
    def combine_with_chair(self, chair: Chair) -> str:
        pass


# Concrete Products (Modern variant)
class ModernChair(Chair):
    def sit_on(self) -> str:
        return "Sitting on a modern chair."


class ModernSofa(Sofa):
    def lie_on(self) -> str:
        return "Lying on a modern sofa."

    def combine_with_chair(self, chair: Chair) -> str:
        result = chair.sit_on()
        return f"Modern sofa works well with -> ({result})"


# Concrete Products (Victorian variant)
class VictorianChair(Chair):
    def sit_on(self) -> str:
        return "Sitting on a Victorian chair."


class VictorianSofa(Sofa):
    def lie_on(self) -> str:
        return "Lying on a Victorian sofa."

    def combine_with_chair(self, chair: Chair) -> str:
        result = chair.sit_on()
        return f"Victorian sofa works well with -> ({result})"


# Client code
def client_code(factory: FurnitureFactory) -> None:
    chair = factory.create_chair()
    sofa = factory.create_sofa()

    print(sofa.lie_on())
    print(sofa.combine_with_chair(chair), end="")


if __name__ == "__main__":
    print("Client: Using Modern Furniture Factory")
    client_code(ModernFurnitureFactory())

    print("\n")

    print("Client: Using Victorian Furniture Factory")
    client_code(VictorianFurnitureFactory())