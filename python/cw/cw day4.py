fruits = ['orange', 'apple', 'banana']
vegetables = ['carrot', 'tomato', 'onion' ]
beverages = ['water', 'beer', 'wine']

fruits.append('grapes')
vegetables.insert(1, 'beans')
beverages.pop()

inventory = [fruits, vegetables, beverages]
print(inventory)

two_fruits = fruits[:2]
print(two_fruits)

last_vege = vegetables[-1]
print(last_vege)

fruits_len = [len(i) for i in fruits]
print(fruits_len)

print(f"\nIs water in beverages: {'water' in beverages}\n")

tuple_items = []
tuple_items.append(fruits[0])
tuple_items.append(vegetables[0])
tuple_items.append(beverages[0])

tuple_items = tuple(tuple_items)
print(tuple_items)