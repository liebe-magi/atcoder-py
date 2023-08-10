def main():
    n = int(input())
    p = list(map(int, input().split()))

    m = max(p)
    count = p.count(p[0])

    if p[0] != m:
        print(m - p[0] + 1)
    else:
        if count == 1:
            print(0)
        else:
            print(1)


main()
