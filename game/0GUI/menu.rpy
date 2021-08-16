# init -100 python:
#     class menus:
#         def __init__(self, lst = []):
#             self.lst = lst
#         def add(self, x):
#             self.list.append(x)

# default mm_menu = menus(
#     [
#         [_("START"), Start()],
#         [_("Load"), ShowMenu("load")],
#         [_("Settings"), ShowMenu("preferences")],
#         [_("Credits"), ShowMenu("credits")],
#         [_("Gallery"), ShowMenu("gallery")],
#         [_("QUIT"), Quit(confirm = not main_menu)],
#     ],
# )
# default nav_menu = menus(
#     [
#         [_("RETURN"), Return()],
#         [_("Save"), ShowMenu("save")],
#         [_("Load"), ShowMenu("load")],
#         [_("History"), ShowMenu("history")],
#         [_("Settings"), ShowMenu("preferences")],
#         [_("Credits"), ShowMenu("credits")],
#         [_("Gallery"), ShowMenu("gallery")],
#         [_("Help"), ShowMenu("help")],
#         [_("MAIN MENU"), MainMenu(), "mm"],
#         [_("QUIT"), Quit(confirm=not main_menu)],
#     ],
# )
# default q_menu = menus(
#     [
#         [_("RETURN"), Return()],
#         [_("Save"), ShowMenu("save")],
#         [_("Settings"), ShowMenu("preferences")],
#         [_("History"), ShowMenu("history")],
#         [_("Back"), Rollback()],
#         [_("Skip"), Skip() alternate Skip(fast=True, confirm=True)],
#         [_("Auto"), Preference("auto-forward", "toggle")],
#         [_("Q.Save"), QuickSave()],
#         [_("Q.Load"), QuickLoad()],
#     ],
# )

# screen menu(m = mm_menu):
#     style_prefix "menu"
#     frame:
#         background None
#         vbox:
#             for i in m.lst:
#                 if (main_menu and "mm" in i) or (not main_menu and "nav" in i):
#                     pass
#                 else:
#                     button:
#                         at btn
#                         text i.[0]
#                         action i.[1]