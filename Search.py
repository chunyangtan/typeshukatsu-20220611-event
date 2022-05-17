def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    # 探索範囲[start, end]を指定（最初は配列全体）
    start = 0
    end = len(sorted_array) - 1
    mid = 0 # 中央値

    # 探索開始
    while start <= end:

        mid = (start + end) // 2 # 中央値を計算

        # 探索範囲中間の値 ＜ 探索対象の場合
        if sorted_array[mid] < target_number:
            start = mid +1 # 探索範囲を中央値以上に絞る

        # 探索範囲中間の値 ＞ 探索対象の場合
        elif sorted_array[mid] > target_number:
            end = mid - 1 # 探索範囲を中央値以下に絞る

        # 探索範囲中間の値が探索対象である場合
        else:
            return mid # 探索終了
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
