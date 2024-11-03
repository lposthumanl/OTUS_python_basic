
phone_book_menu = [
    "Open file",
    "Show all contacts",
    "Exit program",
]

file_actions_menu = [
    "Create contact",
    "Find contact",
    "Edit contact",
    "Delete contact",
    "Save file",
]

graphics_dl = "="
graphics_sl = "-"
main_menu_title = "Phone book menu"
file_menu_title = "File actions"


def show_menu(menu, menu_title):
    menu_items = {}
    menu_number = 1
    print(f"{graphics_dl * (len(menu_title) + 8)}\n    {menu_title} \n{graphics_sl * (len(menu_title) + 8)}")
    for item in menu:
        menu_items[menu_number] = item
        menu_number += 1
    for key, value in menu_items.items():
        print(f"{key} : {value}")
    print(graphics_dl * (len(menu_title) + 8), "\n")
    return menu_items


menu_items = show_menu(phone_book_menu, main_menu_title)
menu_item_choice = menu_items[int(input("Please select menu item. Enter a number: "))]
if menu_item_choice == "Open file":
    print("Opening the contacts file")
