# start

# list_even = all even numb added
# list_odd = all odd numb added
# create a loop that outputs even or odd
# add new lists to a new ampty (above)

list_even = []
list_odd = []
list1 = [1, 2, 3, 4, 5, 6, 7]

for item in list1:
    if item % 2 == 0:
        list_even.insert(0, item)
    else:
        list_odd.insert(0, item)

print(f'the list of even is: {list_even}')
print(f'the list of odd is: {list_odd}')

# stop