#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    cur = 1
    hash_table_insert(ht, weights[0], 0)
    while cur < length:
        cur_w = weights[cur]
        hash_table_insert(ht, cur_w, cur)
        res = limit - cur_w
        the_other_part = hash_table_retrieve(ht, res)

        if res:
            if cur == 1:
                return(cur, 0)
            elif cur > the_other_part:
                return(cur, the_other_part)
            elif cur < the_other_part:
                return (the_other_part, cur)
        
        cur += 1

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
