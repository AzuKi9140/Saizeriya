from typing import Dict


class MenuItem:
    """
    メニューアイテムを表すクラス。
    """

    type_prefixes: Dict[str, str] = {
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
        """
        MenuItemのインスタンスを初期化します。
        """
        self.id = id
        self.name = name
        self.category = category
        self.type = type
        self.price = price
        self.calorie = calorie
        self.salt = salt
        self.order_type = self.type_prefixes.get(self.type, "ZZ")

    def set_order_type(self, counter: int) -> None:
        """
        order_typeに連番を追加します。
        """
        self.order_type = f"{self.order_type}{counter:02}"
