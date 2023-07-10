# Question
# 遊園地「ALGO-RESORT」では N(10) 日間にわたるイベントが開催され、 i 日目 (1≤i≤N) には Ai​ 人が来場しました。
# 以下の合計
# Q(5) 個の質問に答えるプログラムを作成してください。
# 1 個目の質問：L1​ 日目から　R1​ 日目までの合計来場者数は？
# 2 個目の質問：L2​ 日目から　R2​ 日目までの合計来場者数は？
# :
# Q(5) 個目の質問：LQ​ 日目から RQ​ 日目までの合計来場者数は？

def main():
    n, q = map(int, input().split())
    a = [int(i) for i in input().split()]

    for i in range(q):
        l, r = map(int, input().split())

        sum: int = 0
        for j in range(l - 1, r):
            sum += a[j]

        print(sum)

if __name__ == "__main__":
    main()
