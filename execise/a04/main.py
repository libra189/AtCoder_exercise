import math

def binary(n: int) -> list[str]:
    if n == 0:
        return [0]

    res: list[str] = []
    while n != 0:
        b = n % 2
        res.append(str(b))
        n = math.floor(n / 2)

    res.reverse()
    return res


def main():
    n = int(input())
    res: list[str] = binary(n)
    print("".join(res).zfill(10))

    # 解説に記載されていた回答
    # N = int(input())
    #
    # # 上の桁から順番に「2 進法に変換した値」を求める
    # res: list[str] = []
    # for x in [9,8,7,6,5,4,3,2,1,0]:
    #     wari = (2 ** x)
    #     res.append(str((N // wari) % 2))

    # print("".join(res).zfill(10))

if __name__ == "__main__":
    main()
