def binary_search(data: list[int], left: int, right: int, x: int) -> int:
    # print(f"{left=}, {right=}")
    
    i = int(left + (right - left) / 2)
    # print(f"{i=}")

    if (data[i] == x):
        return i+1  # 配列の要素数で検索していたので+1
    
    if (data[i] < x):
        return binary_search(data, i+1, right, x)
    else:
        return binary_search(data, left, i-1, x)


def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    t = binary_search(a, 0, n-1, x)
    print(t)

if __name__ == "__main__":
    main()
