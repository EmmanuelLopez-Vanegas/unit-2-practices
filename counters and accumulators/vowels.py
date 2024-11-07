list = 'You are not a sigma '
vowels = "aeiouAEIOU"
vowel_count = 0
for char in list:
        if char in vowels:
            vowel_count += 1

print(vowel_count)