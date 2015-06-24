---
layout: post
categories: lectures
title: Python odds and ends
---

# Python odds and ends

A grab bag of interesting Python features.

## Named parameters

Named parameters are useful for functions with more than one argument. We
can pass parameters in any order as long as we provide their names.

    def combine(a, b, c):
        print(a, b, c)

    my_value = 42
    combine(my_value, c = 2, b = 3)

## Sorting

Sorting a list by any `key` value. In this example we sort tuples by the
player's jersey number stored in tuple index 1.

    import random
    def by_random(item):
        print("by_random called with item: ", item)
        return random.randint(0, 100)


    players = [
        ('Manning', 18, 39),
        ('Brady', 12, 37),
        ('Brees', 9, 36),
    ]

    def by_jersey(player):
        jersey = player[1]
        return jersey

    players.sort(key = by_jersey)
    print("sorted players", players)


    values = [ 5, 1, 3, 2, 4 ]
    values.sort(key = by_random)
    print("sorted values", values)



## Hash table

Python provides a built-in `Dictionary` class for storing key value pairs.
Let's investigate how to build our own based on the Hash table data structure.


    class HashTable:
        def __init__(self):
            self.capacity = 10
            self.load_factor = 0.75
            self.buckets = [ [] for i in range(0, self.capacity) ]
            print(self.buckets)

        def get(self, key):
            some_huge_number = hash(key)
            index = some_huge_number % self.capacity

            chain = self.buckets[index]
            for entry in chain:
                if entry[0] == key:
                    return entry[1]

            return None


        def set(self, key, value):

            # if current_size / self.capacity > 0.75:
            #     rehash()

            some_huge_number = hash(key)
            index = some_huge_number % self.capacity

            ordered_keys.append(key)

            evicted = False
            chain = self.buckets[index]
            print("chain is", chain)
            # evict previous value for key
            for entry in chain:
                if entry[0] == key:
                    evicted = True
                    entry[1] = value
                    break

            # brand new key
            if not evicted:
                chain.append([key, value])

            # self.buckets[index] = value

        def __str__(self):
            return str(self.buckets)


    players = HashTable()
    players.set("Manning", 18)
    players.set("Brady", 12)
    players.set("Brees", 9)
    print("Tom's number is", players.get("Brady"))
    print("Drew's number is", players.get("Brees"))
    print("Peyton's number is", players.get("Manning"))

    print(players)
