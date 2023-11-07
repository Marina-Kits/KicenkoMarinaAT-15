def making_palindromes(letters):
    letter_count = {}
    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    odd_count = 0
    odd_letter = ''
    for letter, count in letter_count.items():
        if count % 2 != 0:
            odd_count += 1
            odd_letter = letter
    if odd_count > 1:
        return "Невозможно составить палиндром"
    palindrome = ''
    for letter, count in letter_count.items():
        if count % 2 == 0:
            palindrome += letter * (count // 2)
    return palindrome + odd_letter + palindrome[::-1]
print(making_palindromes("wflfl"))
print(making_palindromes("ssppvv"))
print(making_palindromes("aopspa"))