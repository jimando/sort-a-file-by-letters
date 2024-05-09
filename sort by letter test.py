def soccer():
    letter_to_sort = input("what letter would you like to sort the list into ")
    letter_to_sort = str(letter_to_sort)
    for x in fruits:
        if letter_to_sort in x:
            newlist.append(x)
    print(newlist)

fruits = ["apple","banana","pear","cherry"]
newlist = []
soccer()