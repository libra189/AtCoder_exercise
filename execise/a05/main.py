def main():
    n, k = map(int, input().split(" "))

    count: int = 0
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            # 以下タイムアウト
            # if k <= x + y:
            #     continue
            # for z in range(1, n + 1):
            #     if k == x + y + z:
            #         count += 1

            # 解説より抜粋
            # x, yが決まった時点で式変換し、zを求める
            # zが1<=z<=nの場合、正しい
            z = k - x - y
            if 1 <= z and z <= n:
                count += 1


    print(count)

if __name__ == "__main__":
    main()
