def main():
    h, w = map(int, input().split())
    x: list[list[int]] = [list(map(int, input().split())) for i in range(h)]

    for _ in range(int(input())):
        p = list(map(int, input().split()))
        p = [i -1 for i in p]  # 配列要素数に合わせるために-1
        
        total: int = 0
        for v in range(p[0], p[2]+1):
            # print(x[v][p[1]:p[3]+1])
            total += sum(x[v][p[1]:p[3]+1])
        
        print(total)
        
    
if __name__ == "__main__":
    main()
