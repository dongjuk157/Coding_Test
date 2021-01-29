N = int(input())

words = dict()
for _ in range(N):
    word = input()
    len_word=len(word)
    for char in word:
        if not char in words:
            words[char] = 0
        words[char] += 10**(len_word - 1)
        len_word -= 1
words=sorted(words.items(),key=lambda x: x[1], reverse=True)

result = 0
for i in range(len(words)):
    result += words[i][1]*(9-i)

print(result)
