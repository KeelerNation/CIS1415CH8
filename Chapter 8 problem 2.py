
#Adds numbers to a list
my_list = []
count = 0
while count < 9:
    number = int(input('Enter a number for a list:\n'))
    my_list.append(number)
    count += 1
print('The list:',my_list)

#Adds up the list

print('The sum:',sum(my_list))

#Gives the max of the list

print('The maximum:',max(my_list))

#Gives the minimum of the list

print('The minimum:',min(my_list))

#Gives a copy of the list

print('The copy of the list:',my_list[:])
