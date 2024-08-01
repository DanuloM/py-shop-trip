import dataclasses
import json
from typing import List


@dataclasses.dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    @staticmethod
    def get_shop_info() -> List["Shop"]:
        shops = []
        with open("app/config.json", "r") as file:
            file_data = json.load(file)

        _shops = file_data["shops"]

        for i in _shops:
            shop = Shop(
                name=i["name"],
                location=i["location"],
                products=i["products"]
            )
            shops.append(shop)
        return shops
