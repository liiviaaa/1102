#First we read the file with the three digit numbers 
f_obj = open ("three_digit_numbers.txt", 'r') 
#Now we save the numbers in the file as a list. To do this we read the file as a single string , 
# replace the line breaks with a space, remove white space from both ends then finally split the sring into a list.
list_one = f_obj. read().replace("\n", " ") .strip() .split(" ")
f_obj.close() #Close the file since we don't need it anymore
# For each number in our list we replace it with its equivalent as an integer.
for i in range (len(list_one)): 
    list_one[i] = int(list_one[i])
list_one.sort() #Now we sort the list in ascending order
n_obj = open("sorted_numbers.txt",'w') #Create/edit the sorted list file 
#For each number in the sorted list we write the number to the file including a line break
for x in list_one:
    n_obj.write(f"{x}\n")
n_obj.close() #Save and Close the created/edited file 
missing_list = [] #Created empty list to be populated by the missing numbers 
#For every number between 300-500, if the number is not in the original list add it to the missing number list 
for i in range (300,500):
    if i not in list_one:
        missing_list.append(i)
print ("The missing values are:", missing_list)