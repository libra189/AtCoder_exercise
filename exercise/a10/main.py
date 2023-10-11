def main():
    n: int = int(input())
    a = list(map(int, input().split()))
    
    for _ in range(int(input())):
        l, r = map(int, input().split())
        l -= 1  # 配列の要素数に合わせるために-1
        
        t = a[0:l] + a[r:len(a)]
        print(max(t))

if __name__ == "__main__":
    main()
