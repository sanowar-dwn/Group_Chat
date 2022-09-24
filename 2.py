# initializing string
test_string = "This is a hate speech"

# initializing test list
test_list = ['hate', 'religion']

# printing original string
# print("The original string : " + test_string)

# printing original list
# print("The original list : " + str(test_list))

test_string = test_string.split(" ")

flag = 0
for i in test_string:
    for j in test_list:
        if i == j:
            flag = 1
            break
if flag == 1:
    print("Your text violates our standards")
else:
    print("String does not contains the list element")
