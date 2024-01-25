basic_types = [True, 47, 3.14, 3j, "Testing", ["Pizza", "Burgers", "Nachos"]]


def find_type(list_of_types):

    for x in list_of_types:
        print(type(x))


find_type(basic_types)
