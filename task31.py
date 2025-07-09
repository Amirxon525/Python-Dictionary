def count_letters(text: str) -> dict[str, int]:
    result = {}
    for char in text:
        if char.isalpha():  # Faqat harflarni hisoblash
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    return result
