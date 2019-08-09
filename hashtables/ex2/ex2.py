#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    current_dest = None

    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        if tickets[i].source is 'NONE':
            current_dest = tickets[i].destination
            route[0] = current_dest
    
    for i in range(1, length):
        next_loc = hash_table_retrieve(hashtable, current_dest)

        print(next_loc)
        route[i] = next_loc
        current_dest = next_loc



    return route
