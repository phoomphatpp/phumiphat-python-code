""" เขียน function ชื่อ count_vowels_consonants ที่มีคุณสมบัติดังนี้:

รับ parameter text เป็น string
นับสระ (a, e, i, o, u) และพยัญชนะ (ไม่นับช่องว่างและตัวเลข)
return dictionary ที่มี vowels และ consonants counts
ไม่สนใจตัวใหญ่ตัวเล็ก (case insensitive) """


def count_vowels_consonants(text):
    # text= str(text)
    # text.lower(text)
    # vowels = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')
    cleaned_text = text.lower()

    vowels = 0
    consonants = 0
    for char in cleaned_text:
        if char in 'aeiou':
            vowels += 1
        else:
            consonants += 1

    return {
        "vowels": vowels,
        "consonants": consonants,
    }

result  = count_vowels_consonants("hello world 2")

print(result)