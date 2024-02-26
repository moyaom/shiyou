from collections import deque

def replace_chars(s, k):
    # 滑动窗口记录前k个字符
    window = deque(maxlen=k)
    result = ''
    for char in s:
        if char in window:
            result += '-'
        else:
            result += char
        window.append(char)
    return result

print(replace_chars('abcdefaxc', 10))
print(replace_chars('abcdefaxcqwertba', 10))
