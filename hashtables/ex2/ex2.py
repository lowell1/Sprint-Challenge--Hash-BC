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

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    route = []
    next_dest = hash_table_retrieve(hashtable, "NONE")

    while next_dest != "NONE":
        new_ticket = Ticket(next_dest, hash_table_retrieve(hashtable, next_dest))
        route += [new_ticket.source]
        next_dest = new_ticket.destination

    print(route)


    return route