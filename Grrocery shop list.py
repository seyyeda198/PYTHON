initial_items = ["milk", "bread", "eggs"]

def add_item(item):
    initial_items.append(item)

def remove_last_item():
    initial_items.pop()

add_item("rice")
print("Added item:", initial_items)

remove_last_item()
print("After removed:", initial_items)

display_item = lambda item: print("Item:", item)

for item in initial_items:
    display_item(item)

def count_characters(items):
    if len(items) == 0:
        return 0
    else:
        return len(items[0]) + count_characters(items[1:])

total = count_characters(initial_items)
print("Total characters:", total)