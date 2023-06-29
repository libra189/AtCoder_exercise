def main():
    i = input().split(" ")
    r = [v for v in input().split(" ") if v == i[1]]

    if len(r) > 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
