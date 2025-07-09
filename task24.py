def most_common_char(text: str) -> str:
    if not text:
        return ''
    counter = {}
    for ch in text:
        counter.setdefault(ch, 0)
        counter[ch] += 1
    mx = text[0]
    for ch in text:
        if counter[ch] > counter[mx]:
            mx = ch
    return mx
