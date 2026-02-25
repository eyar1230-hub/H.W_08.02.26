# start

# create empty list - capital_latter_start
# create aloop that find strings that starts with CP letters
#   copy to - capital_latter_start
#   print(capital_latter_start)

capital_latter_start = []
list1 = ["Hello", "world", "Python", "java", "Code"]

for item in list1:
    if item.istitle():
        capital_latter_start.append(item)
print(capital_latter_start)


# stop