def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    last = len(array)

    while True:

        # 先頭から末端に向かって基準値以上の値（left）を探索
        for left in range(0, last):

            # leftが見つかったら探索終了
            if array[left] >= pivot:
                break

        # 末端から先頭に向かって基準値未満の値（right）を探索
        for right in range(last - 1, left - 1, -1):

            # rightが見つかった場合
            if array[right] < pivot:

                # leftとrightを交換する
                array[left], array[right] = array[right], array[left]

                break # 探索終了

        # rightが見つからない（ぶつかった）場合
        if right == left:

            # 先頭でぶつかった（交換するものがなくなった）場合
            if left == 0:

                return array # このグループに対する処理が終了

            # 配列を２つのグループに分け，各グループに対して同じ処理を繰り返す
            array[0:left] = sort(array[0: left]) # 前半グループ
            array[left:last] = sort(array[left: last]) # 後半グループ

            # 前半後半に分けられていたグループそれぞれ処理が終了したため，配列を返却
            return array

    # ここまで記述

if __name__ == '__main__':
    main()
