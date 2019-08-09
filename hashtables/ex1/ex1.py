#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    cur_index = 1

    hash_table_insert(ht, weights[0], 0)
    while cur_index < length:
        hash_table_insert(ht, weights[cur_index], cur_index)
        result = limit - weights[cur_index]
        the_other_part = hash_table_retrieve(ht, result)

        if the_other_part:
            if cur_index == 1:
                return (cur_index, 0)
            elif cur_index > the_other_part:
                return(cur_index, the_other_part)
            elif cur_index < the_other_part:
                return(the_other_part, cur_index)
        cur_index += 1

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
