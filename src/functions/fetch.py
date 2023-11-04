import sqlite3
from collections import defaultdict
from typing import List

from src.models.menu_item import MenuItem


def fetch_menu_data(db_path: str) -> List[MenuItem]:
    """
    データベースからメニューデータを取得し、MenuItemのリストを返します。
    """
    rows = fetch_menu_rows(db_path)

    # 行をMenuItemのインスタンスに変換
    menu_items = [MenuItem(*row) for row in rows]

    # order_typeごとにMenuItemをグループ化
    grouped_items = defaultdict(list)
    for item in menu_items:
        grouped_items[item.order_type].append(item)

    # 各グループに対して連番を割り当てる
    for order_type_items in grouped_items.values():
        for i, item in enumerate(order_type_items, start=1):
            item.set_order_type(i)

    return menu_items


def fetch_menu_rows(db_path: str) -> List[tuple]:
    """
    データベースからメニューの行を取得し、タプルのリストを返します。
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, name, category, type, price, calorie, salt FROM menu"
        )
        rows = cursor.fetchall()

    return rows
