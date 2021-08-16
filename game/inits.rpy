############################################################## Inits ##############################################################

init python:
    chnana = 1
    def change_nana(nana_points):
        chnana += nana_points
        if chnana < 1:
            chnana = 1

init python:
    chayame = 1
    def change_ayame(ayame_points):
        chayame += ayame_points
        if chayame < 1:
            chayame = 1

init python:
    chmayo = 1
    def change_mayo(mayo_points):
        chmayo += mayo_points
        if chmayo < 1:
            chmayo = 1

init python:
    chhana = 1
    def change_hana(hana_points):
        chhana += hana_points
        if chhana < 1:
            chhana = 1

init python:
    def change_time(value):
        global time_of_day
        for i in range(value):
            time_of_day += 1
            if time_of_day > 24:
                time_of_day = 1
                if current_label != "house":
                    Jump("day_end")()




# init python:
#     config.overlay_screens.append("sleep_time")

init python:
    config.overlay_screens.append("show_time")

init python:
    config.overlay_screens.append("show_label_name")
