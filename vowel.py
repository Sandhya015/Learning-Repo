def count_vowels_and_consonants(s):
    # Define vowels
    vowels = "aeiouAEIOU"
    
    # Initialize counters
    vowel_count = 0
    consonant_count = 0
    
    # Iterate through the string
    for char in s:
        # Check if the character is a letter
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Example usage
s = input("Enter a string: ")
vowels, consonants = count_vowels_and_consonants(s)

print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
