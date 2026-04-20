from __future__ import annotations
from abc import ABC, abstractmethod


# Product interface
class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass


# Concrete Products
class Truck(Transport):
    def deliver(self) -> str:
        return "Delivering goods by land using a truck."


class Ship(Transport):
    def deliver(self) -> str:
        return "Delivering goods by sea using a ship."


# Creator
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self) -> str:
        # Factory method is called here
        transport = self.create_transport()

        # Business logic using the product
        return f"Logistics: {transport.deliver()}"


# Concrete Creators
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()


# Client code
def client_code(logistics: Logistics) -> None:
    print(logistics.plan_delivery())


if __name__ == "__main__":
    print("App: Using Road Logistics")
    client_code(RoadLogistics())

    print("\nApp: Using Sea Logistics")
    client_code(SeaLogistics())