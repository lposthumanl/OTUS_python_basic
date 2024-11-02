
phone_book_menu = [
    "open file",
    "save file",
    "show all contacts",
    "create contact",
    "find contact",
    "edit contact",
    "delete contact",
    "exit program",
]
graphics_dl = "====================="
graphics_sl = "---------------------"
def show_menu(menu):
    menu_number = 1
    print(f"{graphics_dl}\n   Phone book menu \n{graphics_sl}")
    for position in menu:
        # position = menu[menu_number-1]
        print(f"{menu_number} : {position}")
        menu_number +=1
    print(graphics_dl)


show_menu(phone_book_menu)