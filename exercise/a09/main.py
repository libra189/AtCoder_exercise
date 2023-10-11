def main():
    h, w, n = map(int, input().split())
    
    # 降雪マップを作製
    snow: list[list[int]] = [[0 for _ in range(h)] for _ in range(w)]
    # print(snow)
    
    for _ in range(n):
        p = list(map(int, input().split()))
        p = [i-1 for i in p]  # 配列要素数に合わせるために-1
        # print(p)
        
        for i in range(p[0], p[2]+1):
            for j in range(p[1], p[3]+1):
                snow[i][j] += 1
        
    for i in range(len(snow)):
        l = " ".join(map(str, snow[i]))  # int型の配列をjoinすることはできないため、str型に変換
        print(l)
        

if __name__ == "__main__":
    main()
