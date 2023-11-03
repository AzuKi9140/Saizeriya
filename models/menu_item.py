type_prefixes = {
    "salad": "SA",
    "appetizer": "AA",
    "pasta": "PA",
    "doria": "DG",
    "pizza": "PZ",
    "rice": "RP",
    "dessert": "DE",
    "drinkbar": "DB",
    "soup": "SU",
    "hamburg": "MT",
    "gratin": "DG",
    "alcohol": "AL",
    "chicken": "MT",
    "steak": "MT",
}


class MenuItem:
    def __init__(
        self,
        id: int,
        name: str,
        category: str,
        type: str,
        price: float,
        calorie: int,
        salt: float,
        order_type: str = None,
    ):
        self.id = id
        self.name = name
        self.category = category
        self.type = type
        self.price = price
        self.calorie = calorie
        self.salt = salt
        self.order_type = order_type

    def set_order_type(self):
        self.order_type = type_prefixes.get(
            self.type, "ZZ"
        )  # typeが辞書になければ"ZZ"をデフォルトとする
