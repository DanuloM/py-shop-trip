import dataclasses
import json
import math
from typing import List
from app.car import Car
from app.shop import Shop


@dataclasses.dataclass
class Customer:
    name: str
    products: dict[str, int]
    location: list[int]
    money: int
    car: Car

    @staticmethod
    def get_customer_info() -> List["Customer"]:
        customers = []
        with open("app/config.json", "r") as file:
            file_info = json.load(file)

        _customers = file_info["customers"]
        for i in _customers:
            car_data = i["car"]
            car = Car(
                brand=car_data["brand"],
                fuel_consumption=car_data["fuel_consumption"]
            )
            customer = Customer(
                name=i["name"],
                products=i["product_cart"],
                location=i["location"],
                money=i["money"],
                car=car
            )
            customers.append(customer)

        return customers

    def calculate_distance(self, shop: Shop) -> int | float:
        distance = math.dist(shop.location, self.location)
        return distance
