from mip import BINARY, Model, maximize, xsum


def solve_menu_problem(menu_items, budget):
    # モデルの作成
    m = Model("Saizeriya")

    # 変数の作成
    x = {item.id: m.add_var(name=item.name, var_type=BINARY) for item in menu_items}

    # order_typeの種類を表す変数の作成
    y = {
        order_type: m.add_var(var_type=BINARY)
        for order_type in set(item.order_type for item in menu_items)
    }

    # 制約の追加（予算制約）
    m += xsum(item.price * x[item.id] for item in menu_items) <= budget

    # 制約の追加（order_typeの種類）
    for order_type in y:
        m += y[order_type] <= xsum(
            x[item.id] for item in menu_items if item.order_type == order_type
        )

    # 目的関数の追加（order_typeの種類最大化）
    m.objective = maximize(xsum(y.values()))

    # 最適化問題を解く
    m.optimize()

    # 選択されたメニューアイテムを返す
    return [item for item in menu_items if x[item.id].x > 0.5]
