from simple_term_menu import TerminalMenu

def main():
    l = ["Cat", "Dog"]
    menu = TerminalMenu(l, multi_select=True, show_multi_select_hint=True, multi_select_select_on_accept=False, multi_select_empty_ok=True)
    menu_indices = menu.show()
    print(menu_indices)
    print(menu.chosen_menu_entries)

main()