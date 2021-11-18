def main():
    nums = [input() for _ in range(int(input()))]
    results = {}

    for i in nums:
        if len(i) == 1:
            num = int(i[0])
        else:
            num = int(i[0]) + int(i[-1])

        if num not in results:
            results[num] = 1
        else:
            results[num] += 1

    print(sorted(results, key=lambda x: (results[x], x), reverse=True)[0])


if __name__ == '__main__':
    main()
