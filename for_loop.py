#Code that explains basic working of for loop
#By- Anshul Jindal

num = [1,2,3,4,5]
word = ['cat', 'dog', 'horse']
num_word = [1,2,3,'cat','dog']
for w in num:
    print(w, end = ',')
print()
for w in word:
    print(w, len(w), end = '..')
print()
for w in num_word:
    print(w, end = '-')
