def calculate_letter_statistics(string):
    letter_count = {}
    for letter in string:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return sorted(letter_count.items(), key=lambda x: x[1])

st = open('input.txt').readline()
sorted_statistics = calculate_letter_statistics(st)
output = open("output.txt","w")
for letter, count in sorted_statistics:
    output.write(letter + ":" + str(count)+ "\n")