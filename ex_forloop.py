#for loop examples


#ex-1 enumarete
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]

for num, name in enumerate(presidents, start=1):
    print("President {}: {}".format(num, name))

#ex-2 -zip
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for color, ratio in zip(colors, ratios):
    print("{}% {}".format(ratio * 100, color))

#ex-3 enumarate
new_lis = [2, 8, 1, 4, 6]
for x, new_val in enumerate(new_lis):
    print (x, ",",new_val)

#ex-4 len of list
my_lis = [6, 1, 9, 2] 
for new_indic in range(len(my_lis)): 
    print(new_indic, my_lis[new_indic])

#ex-5 zip
new_str = ['e', 'f', 'i']
 
for m in zip(range(len(new_str)), new_str):
    print(m)
print(type(m))

#ex-6 map
new_str2 = ['Germany', 'England', 'France']
 
new_out = map(lambda o: (o, new_str2[o]), range(len(new_str2))) #map function
print(list(new_out))

#ex-7 
for index in range(2,8):
    print("loop index range",index)

#ex-8
new_val = ["i", "m", "k"]
new_index = 0

for value in new_val:
   print(new_index, value)
   new_index += 1

#ex-9
new_list = ["e","u","o","p","g"]
print("Values in list with index:") 
for new_indices, new_val in enumerate(new_list, start=1): 
    print(list((new_indices, new_val)))

#ex-10
for item in range(10):
 print("* * * * * * * * * *", end="\n")
 
for item in range(4):
 print("\ | /  \ | /  \ | / ", end="\n")
 print(" | |    | |    | |  ", end="\n")
 print("/ | \  / | \  / | \ ", end="\n")

for item in range(17):
 if(item%3 == 0):
    print(item)
print("Done")

for item in range(0, 17, 3):
 print(item)
print("Done")

import random
 
count=random.randint(3,8)
for i in range(count):
 num=int(input("Enter a number: "))
 print(num**2)
 
#while(True):
#    x=1
