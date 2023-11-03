from collections import defaultdict

from src.functions.fetch import fetch_menu_data
from src.functions.solve import solve_menu_problem


def main():
    # データベースのパスを指定
    db_path = "data/saizeriya.db"

    # データを抽出
    menu_items = fetch_menu_data(db_path)

    # ユーザーからの予算入力を受け取る
    budget = int(input("あなたの予算を入力してください: "))

    # solve_menu_problem関数を使用して最適なメニューを解く
    selected_menu_items = solve_menu_problem(menu_items, budget)
    print(selected_menu_items)

    # 選択されたメニューアイテムをorder_typeでグループ化
    grouped_menu_items = defaultdict(list)
    for item in selected_menu_items:
        grouped_menu_items[item.order_type].append(item)

    # グループ化したメニューアイテムを出力
    for order_type, items in grouped_menu_items.items():
        print(f"オーダータイプ: {order_type}, メニューの個数: {len(items)}")
        for item in items:
            print(f" - {item.name}")
    # 最適化問題によって出てきたorder_typeの個数を表示
    print(f"オーダータイプの総数: {len(grouped_menu_items)}")


if __name__ == "__main__":
    main()
