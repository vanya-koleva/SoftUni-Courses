def find_sums(nums):
    positive_sum = sum(num for num in nums if num > 0)
    negative_sum = sum(num for num in nums if num < 0)

    result = f"{negative_sum}\n{positive_sum}\n"

    if abs(negative_sum) > positive_sum:
        result += "The negatives are stronger than the positives"
    else:
        result += "The positives are stronger than the negatives"

    return result


numbers = [int(x) for x in input().split()]
print(find_sums(numbers))
