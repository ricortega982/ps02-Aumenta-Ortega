import copy
nested_list = [[1, 2], [3, 4]]
alias_nested = copy.deepcopy(nested_list)
alias_nested [0][1] = 99

print (f"Original nested list: {nested_list}")
print (f"Aliased nested list: {alias_nested}")