import sqlite3
from typing import List

from src.models.menu_item import MenuItem


def fetch_menu_data(db_path: str) -> List[MenuItem]:
    rows = fetch_menu_rows(db_path)
    menu_items = create_menu_items(rows)
    return menu_items


def fetch_menu_rows(db_path: str):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, name, category, type, price, calorie, salt FROM menu"
        )
        rows = cursor.fetchall()

    return rows


def create_menu_items(rows):
    menu_items = [MenuItem(*row) for row in rows]
    for item in menu_items:
        item.set_order_type()

    return menu_items
