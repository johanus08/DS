size_list = 6

def hash_func(value):
    global size_list
    return value%7

def map_hash2index(hash_return_value):
    return hash_return_value


def create_hash_table(list_values,main_list):
    for value in list_values:
        hash_return_value = hash_func(value)
        list_index = map_hash2index(hash_return_value)
        if list_values[list_index]:
            print("Collision detected")
        else:
            list_values[list_index] = value
            
list_values = [1,3,4,8,3]

main_list = [None for x in range(size_list)]
print(main_list)
create_hash_table(list_values,main_list)
print(main_list)
    
