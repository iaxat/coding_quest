def descending_order():
    n = int(input('Enter the number: '))
    lst = list(str(n))
    lst_int = []
    lst_new = []

    for i in range(0,len(lst)):
        lst_int.append(int(lst[i]))

    lst_new = lst.sort(reverse=True)
    print(lst_new)
    


# The main function
descending_order()