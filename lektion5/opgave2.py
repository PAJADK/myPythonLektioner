""" """

min_param = [1, 2, 8]
def min_tal(min_list):
    for summen in min_list:
        summen = sum(min_list)
    return summen

print("Summen er: " + str(min_tal(min_param)))



def min_tal2(min_list):

    min_list.append(min_tal(min_param))
    print(min_list)

min_tal2(min_param)


