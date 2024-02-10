words = input().split()
palindrome = input()
palindromes = []

for word in words:
    if word == word[::-1]:
        palindromes.append(word)

palindrome_found_times = words.count(palindrome)

print(palindromes)
print(f"Found palindrome {palindrome_found_times} times")
