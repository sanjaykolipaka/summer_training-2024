# Input = "tu5g7k1h8"
#         "g5g8gd6h3"

# output = largest possible even integer from above number
            # 875316



# s1 = "tu5g7k1h8"
# s2 = "g5g8gd6h3"
# s3 =""
# for i in s1:
#     if i.isnumeric() and i not in s3:
#         s3 += i
# for i in s2:
#     if i.isnumeric() and i not in s3:
#         s3 += i
# s3 = (sorted(s3,reverse = True))
# print(''.join(s3))
# i = len(s3)-1
# while i > 0:
#     if int(s3[-1]) % 2 == 0:
#         break
#     s3[-1] , s3[i-1] = s3[i-1], s3[-1] 
#     i -= 1
# print("".join(s3))



dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"

# Split the sentence string into a list of words
l = sentence.split()

# Iterate through each word in the dictionary
for i in dictionary:
    # Iterate through each word in the list of sentence words
    for index, j in enumerate(l):
        # If the word from dictionary is a substring of the sentence word, replace it
        if i in j:
            l[index] = i

print(l)
