
numbers = list(map(int, input().split()))

unique_number = list(set(numbers))


if len(unique_number) < 2:
    print(-1)
else:
    unique_number.sort(reverse=True)

    print(unique_number[1])
