
inventory = []

def add_item(item):
    inventory.append(item)


def count_items(items):
    if not items:
        return 0
    else:
        return 1 + count_items(items[1:])


def main():
    add_item("dog food")
    add_item("cat toy")
    add_item("bird seed")
    add_item("fish tank")

    total = count_items(inventory)
    print("Total Items:", total)

    show_item = lambda item: print(f"Item in Stock: {item}")

    for item in inventory:
        show_item(item)


main()
