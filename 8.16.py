count = 1
weight_list = []
while count < 5:
    weight_input = float(input('Enter weight %d:\n' % count))
    weight_list.append(weight_input)
    count += 1
print('Weights:',weight_list)


weight_average = float(sum(weight_list)/4)
print('')

print('Average weight: %.2f' % weight_average)
print('Max weight: %.2f' % max(weight_list))

print('')

#Weight in Pounds
weight_index = int(input('Enter a list index (1 - 4):\n'))
if weight_index == 1:
    print('Weight in pounds: %.2f' % weight_list[0])
if weight_index == 2:
    print('Weight in pounds: %.2f' % weight_list[1])
if weight_index == 3:
    print('Weight in pounds: %.2f' % weight_list[2])
if weight_index == 4:
    print('Weight in pounds: %.2f' % weight_list[3])

#weight in kilograms
if weight_index == 1:
    weight_kilograms = float(weight_list[0] / 2.2)
    print('Weight in kilograms: %.2f' % weight_kilograms)
if weight_index == 2:
    weight_kilograms = float(weight_list[1] / 2.2)
    print('Weight in kilograms: %.2f' % weight_kilograms)
if weight_index == 3:
    weight_kilograms = float(weight_list[2] / 2.2)
    print('Weight in kilograms: %.2f' % weight_kilograms)
if weight_index == 4:
    weight_kilograms = float(weight_list[3] / 2.2)
    print('Weight in kilograms: %.2f' % weight_kilograms)


weight_sorted = weight_list.sort()
print('')
print('Sorted list:',weight_list)