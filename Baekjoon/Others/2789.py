string = input()

geomyeol = 'CAMBRIDGE'

for char in string:
    if not char in geomyeol:
        print(char,end='')

# word =input()
# sensored = "CAMBRIDGE"
# for sensor in sensored:
#     if sensor in word:
#         word = word.replace(sensor,"")
# print(word)

# words = list(map(str, input()))
# univ = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

# for word in words:   words = [L,O,V,A] 
#     for sensored in univ:
#         if word == sensored:
#             words.remove(word)
        
# print(''.join(words))