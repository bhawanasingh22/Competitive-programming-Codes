#given a string S you've to find all amazing substring of S an amazing substring is one that start with vowel
# s = input()
# vowels = 'aeiouAEIOU'
# count = 0
# for i in range(len(s)):
#     if s[i] in vowels:
#         for j in range(i+1, len(s)+1):
#             count += 1
# print(count)

#find the number of occurrence of bob in string A consisting lowercase english alphabet

s =input()
count = 0
for i in range(len(s)-2):
    if s[i:i+3] == 'bob':
        count += 1
print(count)




