from collections import defaultdict
from typing import List

from src.functions.fetch import fetch_menu_data
from src.functions.solve import solve_menu_problem
from src.models.menu_item import MenuItem


def main():
    # データベースのパスを指定
    db_path: str = "data/saizeriya.db"

    # データを抽出
    menu_items: List[MenuItem] = fetch_menu_data(db_path)

    # ユーザーからの予算入力を受け取る
    budget: int = int(input("あなたの予算を入力してください: "))

    # ジャンルごとの最大アイテム数を入力
    max_items_per_genre: int = int(input("ジャンルごとの最大アイテム数を入力してください: "))

    # solve_menu_problem関数を使用して最適なメニューを解く
    selected_menu_items: List[MenuItem] = solve_menu_problem(
        menu_items, budget, max_items_per_genre
    )

    # 選択されたメニューアイテムをジャンルでグループ化
    grouped_menu_items: defaultdict = defaultdict(list)
    for item in selected_menu_items:
        grouped_menu_items[item.order_type[:2]].append(item)

    # グループ化したメニューアイテムを出力
    total_cost: int = 0
    for genre, items in grouped_menu_items.items():
        print(f"ジャンル: {genre}, メニューの個数: {len(items)}")
        genre_cost: int = sum(item.price for item in items)
        total_cost += genre_cost
        for item in items:
            print(f" - {item.name}, 価格: {item.price}")
        print(f"ジャンル {genre} の合計金額: {genre_cost}")
    print(f"全体の合計金額: {total_cost}")


if __name__ == "__main__":
    main()
