def unique_consonants(input_string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    consonant_count = {}
    unique_count = 0

    for char in input_string:
        if char in consonants:
            if char.lower() in consonant_count:
                consonant_count[char.lower()] += 1
            else:
                consonant_count[char.lower()] = 1

    for count in consonant_count.values():
        if count == 1:
            unique_count += 1

    return unique_count

input1 = "cat"
print(unique_consonants(input1))  # Output: 2

input2 = "cataract"
print(unique_consonants(input2))  # Output: 1
