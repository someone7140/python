import pandas as pd

# サンプルデータの作成
df = pd.DataFrame(
    {
        "group1": ["A", "A", "B", "B", "C", "A", "D", "B", "E"],
        "group2": ["X", "Y", "X", "Y", "X", "S", "C", "A", "K"],
        "value": [10, 20, 30, 40, 50, 70, 70, 80, 9],
    }
)

# group1でgroupbyして上位2件を取得
grouped = df.groupby("group1")["value"].sum().nlargest(2)

# 対象のgroupとvalueを出力
for i, v in grouped.items():
    print("group1: ", i, "value: ", v)
