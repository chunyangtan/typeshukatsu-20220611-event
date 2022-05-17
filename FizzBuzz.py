for num in range(1, 101):
    string = ''

    # ここから記述

    # 15の倍数（3の倍数かつ５の倍数）
    if num % 3 == 0 and num % 5 == 0:
        string = 'FizzBuzz'
    # ３の倍数
    elif num % 3 == 0:
        string = 'Fizz'
    # 5の倍数
    elif num % 5 == 0:
        string = 'Buzz'
    # それ以外の場合
    else:
        string = num
    # ここまで記述

    print(string)
