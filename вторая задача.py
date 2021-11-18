def main():
    nums = [int(input()) for _ in range(int(input()))]
    result = 0

    for i in range(len(nums)):
        num1 = nums[i]
        for j in range(i, len(nums)):
            num2 = nums[j]
            if (num1 + num2) % 7 == 0:
                result += 1

    print(result)


if __name__ == '__main__':
    main()
