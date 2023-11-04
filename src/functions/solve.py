from typing import List

from mip import BINARY, Model, maximize, xsum

from src.models.menu_item import MenuItem


def order_type_to_num(order_type: str) -> int:
    """
    文字列のorder_typeを数値に変換します。
    order_type: 文字列のorder_type
    return: 数値に変換されたorder_type
    """
    return (
        (ord(order_type[0]) - ord("A")) * 26 + (ord(order_type[1]) - ord("A")) + 1
    ) * 256 + int(order_type[2:], 16)


def solve_menu_problem(
    menu_items: List[MenuItem], budget: int, max_items_per_genre: int
) -> List[MenuItem]:
    """
    メニュー問題を解き、最適なメニューアイテムのリストを返します。
    menu_items: MenuItemのリスト
    budget: 予算
    max_items_per_genre: ジャンルごとの最大アイテム数
    return: 最適なメニューアイテムのリスト
    """
    m = Model("Saizeriya")
    x = {item.id: m.add_var(name=item.name, var_type=BINARY) for item in menu_items}

    m += xsum(item.price * x[item.id] for item in menu_items) <= budget

    genres = set(item.order_type[:2] for item in menu_items)
    for genre in genres:
        m += (
            xsum(x[item.id] for item in menu_items if item.order_type.startswith(genre))
            <= max_items_per_genre
        )

    m.objective = maximize(
        xsum(order_type_to_num(item.order_type) * x[item.id] for item in menu_items)
    )

    m.optimize()

    return [item for item in menu_items if x[item.id].x > 0.5]
