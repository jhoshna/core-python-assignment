def add(menu, item):
    if item not in menu:
        menu.append(item)
    else:
        print(f"{item} is already in the menu.")
    return menu


def remove(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} is not in the menu.")
    return menu


def check(menu, item):
    if item in menu:
        return f"{item} is available."
    else:
        return f"{item} is not available."


m = ["Pizza", "Burger", "Pasta", "Salad"]

# Actions
a = "Tacos"
r = "Salad"
c = "Pizza"

m = add(m, a)
m = remove(m, r)
status = check(m, c)

print("Updated menu:", m)
print("Availability:", status)
