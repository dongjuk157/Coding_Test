N = input()

number = dict()
for char in N:
    if not char in number:
        number[char] = 0
    number[char] += 1

if ('6' in number) and ('9' in number):
    number['6'] += number['9']
    number['6'] = (number['6'] + 1)//2 
elif '6' in number:
    number['6'] = (number['6'] + 1)//2 
elif '9' in number:
    number['9'] = (number['9'] + 1)//2 

need=sorted(number.values(),reverse=True)
print(need[0])

