#   1 2 3 4 printer
# 1 x      
# 2 x x
# 3 x   x
# 4 x x   x
# 5 x
# 6 x x x
# sec

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    total = 0
    c = 0
    while k > total:
        c += 1
        p = [i for i, x in enumerate(a) if c % x == 0]
        # print(f"{c=}: {p=}")
        total += len(p)
        
    print(c)

if __name__ == "__main__":
    main()
