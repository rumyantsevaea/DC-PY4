def delete(list_, index=None):
    if index == None:
        newlist = list_[:-1]
        return newlist
    else:
        newlist = list_[:index] + list_[index + 1:]
        return newlist


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
